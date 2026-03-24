"""
Main game logic for Kviz_Hra
"""

import threading
import time
from typing import Callable, Optional
from models import GameState, Question
import config


class QuizGame:
    """Manages the main game logic and state"""

    def __init__(self, question: Question, state_callback: Optional[Callable] = None):
        """
        Initialize a new game.
        
        Args:
            question: The Question object to play
            state_callback: Optional callback function called when state changes
        """
        self.question = question
        self.state = GameState(question)
        self.state_callback = state_callback
        self.running = False
        self.timer_thread = None
        self._notify_state()

    def start(self):
        """Start the game and timer"""
        self.running = True
        self.state.start_time = time.time()
        self._start_timer()
        self._notify_state()

    def stop(self):
        """Stop the game"""
        self.running = False
        if self.timer_thread:
            self.timer_thread.join(timeout=1)
        self._notify_state()

    def _start_timer(self):
        """Start the countdown timer in a background thread"""
        self.timer_thread = threading.Thread(target=self._timer_loop, daemon=True)
        self.timer_thread.start()

    def _timer_loop(self):
        """Background loop for the timer"""
        while self.running and not self.state.is_time_expired():
            time.sleep(0.5)
            self._notify_state()

        if self.running and self.state.is_time_expired():
            self.end_game("timeout")

    def reveal_cell(self, cell_index: int) -> dict:
        """
        Reveal a cell in the grid.
        
        Args:
            cell_index: Index of cell to reveal (0-15)
        
        Returns:
            Dict with result information
        """
        if not (0 <= cell_index < 16):
            return {"success": False, "message": "Invalid cell index"}

        if not self.state.can_reveal_cell(cell_index):
            return {"success": False, "message": "Cell already revealed"}

        if self.state.is_time_expired():
            return {"success": False, "message": "Time expired"}

        success = self.state.reveal_cell(cell_index)
        
        result = {
            "success": success,
            "cell_index": cell_index,
            "points": self.state.current_points,
            "cost": self.state.attempts[-1].cost if self.state.attempts else 0
        }

        self._notify_state()
        return result

    def use_letter_hint(self) -> dict:
        """
        Use a letter hint to reveal the next letter.
        
        Returns:
            Dict with result information
        """
        if self.state.is_time_expired():
            return {"success": False, "message": "Time expired"}

        if self.state.letter_hints_used >= self.state.question.get_answer_length():
            return {"success": False, "message": "All letters already revealed"}

        success = self.state.use_letter_hint()
        
        result = {
            "success": success,
            "hint_string": self.state.get_hint_string(),
            "hints_used": self.state.letter_hints_used,
            "points": self.state.current_points,
            "cost": self.state.attempts[-1].cost if self.state.attempts else 0
        }

        self._notify_state()
        return result

    def submit_answer(self, user_answer: str) -> dict:
        """
        Submit an answer to the puzzle.
        
        Args:
            user_answer: The user's answer string
        
        Returns:
            Dict with result information
        """
        if self.state.is_time_expired():
            return {"success": False, "message": "Time expired", "correct": False}

        is_correct = self.state.submit_answer(user_answer)

        result = {
            "success": True,
            "correct": is_correct,
            "submitted_answer": user_answer,
            "correct_answer": self.state.question.answer,
            "points": self.state.current_points,
            "cost": self.state.attempts[-1].cost if self.state.attempts else 0
        }

        if is_correct:
            self.end_game("completed")

        self._notify_state()
        return result

    def end_game(self, reason: str = "user_quit"):
        """
        End the game.
        
        Args:
            reason: Reason for ending ("timeout", "completed", "user_quit")
        """
        self.state.game_over = True
        self.state.game_end_reason = reason
        self.running = False
        if self.timer_thread:
            self.timer_thread.join(timeout=1)
        self._notify_state()

    def get_state_dict(self) -> dict:
        """Get the current game state as a dictionary"""
        return self.state.to_dict()

    def get_hint_string(self) -> str:
        """Get the current hint string (e.g., "A______ T______")"""
        return self.state.get_hint_string()

    def get_remaining_time(self) -> float:
        """Get remaining time in seconds"""
        return self.state.get_remaining_time()

    def get_current_points(self) -> int:
        """Get current points"""
        return self.state.current_points

    def get_revealed_cells(self) -> list:
        """Get list of revealed cell indices"""
        return self.state.revealed_cells.copy()

    def is_game_over(self) -> bool:
        """Check if game is over"""
        return self.state.game_over or self.state.is_time_expired()

    def _notify_state(self):
        """Call the state callback if registered"""
        if self.state_callback:
            try:
                self.state_callback(self.get_state_dict())
            except Exception as e:
                print(f"Error in state callback: {e}")
