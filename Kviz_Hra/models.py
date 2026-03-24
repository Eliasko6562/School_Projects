"""
Data models for Kviz_Hra application
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional
from datetime import datetime
import json
import config


@dataclass
class Question:
    """Represents a single question/puzzle in the game"""
    id: str
    title: str
    image_path: str
    answer: str
    category: str
    difficulty: int
    description: str = ""

    def get_answer_length(self) -> int:
        """Get the length of the answer"""
        return len(self.answer)

    def validate_answer(self, user_answer: str) -> bool:
        """Check if user's answer matches (case-insensitive)"""
        if config.VALIDATE_ANSWERS:
            return user_answer.strip().lower() == self.answer.strip().lower()
        return False

    def to_dict(self) -> Dict:
        """Convert to dictionary"""
        return {
            "id": self.id,
            "title": self.title,
            "image_path": self.image_path,
            "answer": self.answer,
            "category": self.category,
            "difficulty": self.difficulty,
            "description": self.description
        }


@dataclass
class Attempt:
    """Represents a single action/attempt in the game"""
    timestamp: float
    action_type: str  # "cell_reveal", "letter_hint", "answer_submission"
    points_before: int
    points_after: int
    cost: int
    details: Dict = field(default_factory=dict)

    def to_dict(self) -> Dict:
        """Convert to dictionary"""
        return {
            "timestamp": self.timestamp,
            "action_type": self.action_type,
            "points_before": self.points_before,
            "points_after": self.points_after,
            "cost": self.cost,
            "details": self.details
        }


@dataclass
class GameState:
    """Represents the current state of a game"""
    question: Question
    start_time: float = field(default_factory=lambda: datetime.now().timestamp())
    current_points: int = config.STARTING_POINTS
    revealed_cells: List[int] = field(default_factory=list)
    letter_hints_used: int = 0
    attempts: List[Attempt] = field(default_factory=list)
    game_over: bool = False
    game_end_reason: Optional[str] = None  # "timeout", "user_quit", "completed"
    correct_answer_given: bool = False

    def get_elapsed_time(self) -> float:
        """Get elapsed time in seconds"""
        return datetime.now().timestamp() - self.start_time

    def get_remaining_time(self) -> float:
        """Get remaining time in seconds"""
        remaining = config.GAME_DURATION - self.get_elapsed_time()
        return max(0, remaining)

    def is_time_expired(self) -> bool:
        """Check if game time has expired"""
        return self.get_remaining_time() <= 0

    def get_next_cell_cost(self) -> int:
        """Calculate the cost of revealing the next cell"""
        cells_revealed = len(self.revealed_cells)
        if cells_revealed == 0:
            return config.FIRST_CELL_COST
        return -cells_revealed

    def get_next_letter_hint_cost(self) -> int:
        """Calculate the cost of the next letter hint"""
        if self.letter_hints_used == 0:
            return config.FIRST_LETTER_HINT_COST
        return -(self.letter_hints_used + 1)

    def can_reveal_cell(self, cell_index: int) -> bool:
        """Check if a cell can be revealed"""
        return cell_index not in self.revealed_cells

    def reveal_cell(self, cell_index: int) -> bool:
        """
        Reveal a cell. Returns True if successful, False if already revealed.
        Updates points accordingly.
        """
        if not self.can_reveal_cell(cell_index):
            return False

        cost = self.get_next_cell_cost()
        points_before = self.current_points
        self.current_points = max(config.MINIMUM_POINTS, self.current_points + cost)
        
        self.revealed_cells.append(cell_index)
        self.revealed_cells.sort()

        attempt = Attempt(
            timestamp=self.get_elapsed_time(),
            action_type="cell_reveal",
            points_before=points_before,
            points_after=self.current_points,
            cost=cost,
            details={"cell_index": cell_index}
        )
        self.attempts.append(attempt)
        return True

    def use_letter_hint(self) -> bool:
        """
        Use a letter hint. Returns True if successful.
        Updates points and hint count.
        """
        if self.letter_hints_used >= self.question.get_answer_length():
            return False

        cost = self.get_next_letter_hint_cost()
        points_before = self.current_points
        self.current_points = max(config.MINIMUM_POINTS, self.current_points + cost)
        
        self.letter_hints_used += 1

        attempt = Attempt(
            timestamp=self.get_elapsed_time(),
            action_type="letter_hint",
            points_before=points_before,
            points_after=self.current_points,
            cost=cost,
            details={"hint_number": self.letter_hints_used}
        )
        self.attempts.append(attempt)
        return True

    def submit_answer(self, user_answer: str) -> bool:
        """
        Submit an answer. Returns True if correct, False if wrong.
        Updates points and game state accordingly.
        """
        points_before = self.current_points
        is_correct = self.question.validate_answer(user_answer)
        
        if not is_correct:
            cost = config.WRONG_ANSWER_COST
            self.current_points = max(config.MINIMUM_POINTS, self.current_points + cost)
        else:
            cost = 0
            self.correct_answer_given = True
            self.game_over = True
            self.game_end_reason = "completed"

        attempt = Attempt(
            timestamp=self.get_elapsed_time(),
            action_type="answer_submission",
            points_before=points_before,
            points_after=self.current_points,
            cost=cost,
            details={"answer": user_answer, "correct": is_correct}
        )
        self.attempts.append(attempt)
        return is_correct

    def get_hint_string(self) -> str:
        """
        Get the current hint string showing revealed letters with individual underscores.
        E.g., "A _ _ _   T _ _ _ _ _" for "Alan Turing"
        """
        answer = self.question.answer
        result = ""
        revealed_count = self.letter_hints_used
        
        current_revealed = 0
        for i, char in enumerate(answer):
            if char == " ":
                result += "   "  # Three spaces between words for better separation
            elif current_revealed < revealed_count:
                result += char + " "
                current_revealed += 1
            else:
                result += "_ "
        
        # Remove trailing space
        return result.rstrip()

    def to_dict(self) -> Dict:
        """Convert game state to dictionary for saving"""
        return {
            "question_id": self.question.id,
            "start_time": self.start_time,
            "elapsed_time": self.get_elapsed_time(),
            "remaining_time": self.get_remaining_time(),
            "current_points": self.current_points,
            "revealed_cells": self.revealed_cells,
            "letter_hints_used": self.letter_hints_used,
            "attempts": [a.to_dict() for a in self.attempts],
            "game_over": self.game_over,
            "game_end_reason": self.game_end_reason,
            "correct_answer_given": self.correct_answer_given
        }
