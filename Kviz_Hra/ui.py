"""
User Interface for Kviz_Hra using Tkinter
"""

import tkinter as tk
from tkinter import messagebox, font
from PIL import Image, ImageTk
import os
from typing import Optional
import config
from game import QuizGame
from models import Question
import image_processor


class GameWindow:
    """Main application window"""

    def __init__(self, root: tk.Tk, game: QuizGame, image: Image.Image):
        self.root = root
        self.game = game
        self.original_image = image
        self.running = False
        self.button_images = {}  # Cache for button images
        self.answer_var = tk.StringVar()

        # Configure window
        self.root.title(config.WINDOW_TITLE)
        self.root.geometry(f"{config.WINDOW_WIDTH}x{config.WINDOW_HEIGHT}")
        self.root.resizable(False, False)

        # Set up UI
        self._create_ui()
        self._update_timer()

    def _create_ui(self):
        """Create all UI elements"""
        # Title
        title_frame = tk.Frame(self.root, bg=config.COLOR_INFO_BG)
        title_frame.pack(fill=tk.X, padx=10, pady=10)

        title = tk.Label(
            title_frame,
            text=config.GAME_TITLE,
            font=("Arial", 24, "bold"),
            bg=config.COLOR_INFO_BG
        )
        title.pack()

        # Info bar (score and time)
        info_frame = tk.Frame(self.root, bg=config.COLOR_INFO_BG)
        info_frame.pack(fill=tk.X, padx=10, pady=5)

        # Points label
        self.points_label = tk.Label(
            info_frame,
            text=f"{config.TEXT_SCORE} {self.game.get_current_points()}",
            font=config.FONT_POINTS,
            bg=config.COLOR_INFO_BG,
            fg=config.COLOR_TEXT
        )
        self.points_label.pack(side=tk.LEFT, padx=20)

        # Timer label
        self.timer_label = tk.Label(
            info_frame,
            text=f"{config.TEXT_TIME_REMAINING} 10:00",
            font=config.FONT_TIMER,
            bg=config.COLOR_INFO_BG,
            fg=config.COLOR_TEXT
        )
        self.timer_label.pack(side=tk.RIGHT, padx=20)

        # Question info
        info_text_frame = tk.Frame(self.root, bg=config.COLOR_INFO_BG)
        info_text_frame.pack(fill=tk.X, padx=10, pady=5)

        q_info = tk.Label(
            info_text_frame,
            text=f"Otázka: {self.game.question.title}",
            font=config.FONT_LABEL,
            bg=config.COLOR_INFO_BG,
            wraplength=400,
            justify=tk.LEFT
        )
        q_info.pack(anchor=tk.W)

        # Image grid
        grid_frame = tk.Frame(self.root, bg=config.COLOR_INFO_BG)
        grid_frame.pack(pady=10)

        self.grid_canvas = tk.Canvas(
            grid_frame,
            width=config.IMAGE_SIZE[0],
            height=config.IMAGE_SIZE[1],
            bd=0,
            highlightthickness=0
        )
        self.grid_canvas.pack()

        self.grid_background_image = ImageTk.PhotoImage(self.original_image)
        self.grid_canvas.create_image(0, 0, anchor=tk.NW, image=self.grid_background_image)
        self.grid_canvas.bind("<Button-1>", self._on_canvas_click)

        self._update_grid()

        # Answer hint
        hint_frame = tk.Frame(self.root, bg=config.COLOR_INFO_BG)
        hint_frame.pack(fill=tk.X, padx=10, pady=10)

        hint_label = tk.Label(
            hint_frame,
            text="Řešení:",
            font=config.FONT_LABEL,
            bg=config.COLOR_INFO_BG
        )
        hint_label.pack(anchor=tk.W)

        self.hint_display = tk.Label(
            hint_frame,
            text=self.game.get_hint_string(),
            font=("Courier", 16, "bold"),
            bg=config.COLOR_INFO_BG,
            fg=config.COLOR_TEXT
        )
        self.hint_display.pack(anchor=tk.W, pady=5)

        # Input and buttons
        input_frame = tk.Frame(self.root, bg=config.COLOR_INFO_BG)
        input_frame.pack(fill=tk.X, padx=10, pady=10)

        input_label = tk.Label(
            input_frame,
            text=config.TEXT_ENTER_ANSWER,
            font=config.FONT_LABEL,
            bg=config.COLOR_INFO_BG
        )
        input_label.pack(anchor=tk.W)

        self.answer_input = tk.Entry(
            input_frame,
            textvariable=self.answer_var,
            font=config.FONT_ANSWER_INPUT,
            width=40
        )
        self.answer_input.pack(fill=tk.X, pady=5)
        self.answer_input.bind("<Return>", lambda e: self._on_submit_answer())
        self.answer_var.trace_add("write", self._on_answer_change)

        # Buttons frame
        buttons_frame = tk.Frame(self.root, bg=config.COLOR_INFO_BG)
        buttons_frame.pack(fill=tk.X, padx=10, pady=10)

        btn_submit = tk.Button(
            buttons_frame,
            text=config.TEXT_SUBMIT_ANSWER,
            command=self._on_submit_answer,
            font=config.FONT_MAIN,
            bg="#00AA00",
            fg="white"
        )
        btn_submit.pack(side=tk.LEFT, padx=5)

        btn_reveal = tk.Button(
            buttons_frame,
            text=config.TEXT_REVEAL_CELL,
            command=self._on_reveal_button,
            font=config.FONT_MAIN
        )
        btn_reveal.pack(side=tk.LEFT, padx=5)

        btn_hint = tk.Button(
            buttons_frame,
            text=config.TEXT_LETTER_HINT,
            command=self._on_hint_button,
            font=config.FONT_MAIN
        )
        btn_hint.pack(side=tk.LEFT, padx=5)

        btn_quit = tk.Button(
            buttons_frame,
            text=config.TEXT_QUIT_GAME,
            command=self._on_quit,
            font=config.FONT_MAIN,
            bg="#AA0000",
            fg="white"
        )
        btn_quit.pack(side=tk.RIGHT, padx=5)

        # Status label
        self.status_label = tk.Label(
            self.root,
            text="",
            font=config.FONT_LABEL,
            bg=config.COLOR_INFO_BG,
            fg=config.COLOR_TEXT
        )
        self.status_label.pack(fill=tk.X, padx=10, pady=5)

        self.running = True
        self.game.start()

    def _update_grid(self):
        """Update the canvas overlay for the hidden tiles."""
        self.grid_canvas.delete("cell_overlay")

        revealed = self.game.get_revealed_cells()
        cell_width = config.IMAGE_SIZE[0] // config.GRID_SIZE
        cell_height = config.IMAGE_SIZE[1] // config.GRID_SIZE

        for row in range(config.GRID_SIZE):
            for col in range(config.GRID_SIZE):
                cell_index = row * config.GRID_SIZE + col
                if cell_index in revealed:
                    continue

                left = col * cell_width
                top = row * cell_height
                right = left + cell_width
                bottom = top + cell_height

                self.grid_canvas.create_rectangle(
                    left, top, right, bottom,
                    fill=config.COLOR_HIDDEN,
                    outline=config.COLOR_TEXT,
                    width=1,
                    tags=("cell_overlay", f"cell_{cell_index}")
                )

    def _update_hint_display(self):
        """Update the hint label based on current typed input and revealed letters."""
        typed_text = self.answer_var.get() if hasattr(self, 'answer_var') else ""
        if typed_text:
            self.hint_display.config(text=self._build_live_preview(typed_text))
        else:
            self.hint_display.config(text=self.game.get_hint_string())

    def _build_live_preview(self, typed_answer: str) -> str:
        """Build a live preview of the answer filling blanks as the user types."""
        typed_letters = [ch for ch in typed_answer if ch != " "]
        typed_idx = 0
        revealed_count = getattr(self.game.state, 'letter_hints_used', 0)
        current_revealed = 0
        result = ""

        for char in self.game.question.answer:
            if char == " ":
                result += "   "
            elif current_revealed < revealed_count:
                result += char + " "
                current_revealed += 1
            elif typed_idx < len(typed_letters):
                result += typed_letters[typed_idx].upper() + " "
                typed_idx += 1
            else:
                result += "_ "

        return result.rstrip()

    def _on_answer_change(self, *args):
        """Update hint preview when the answer input changes."""
        self._update_hint_display()

    def _on_canvas_click(self, event):
        """Handle clicks on the image canvas, revealing the clicked tile."""
        if self.game.is_game_over():
            messagebox.showwarning("Game Over", "Hra již skončila.")
            return

        cell_width = config.IMAGE_SIZE[0] // config.GRID_SIZE
        cell_height = config.IMAGE_SIZE[1] // config.GRID_SIZE

        col = event.x // cell_width
        row = event.y // cell_height

        if col < 0 or col >= config.GRID_SIZE or row < 0 or row >= config.GRID_SIZE:
            return

        cell_index = row * config.GRID_SIZE + col
        result = self.game.reveal_cell(cell_index)

        if result["success"]:
            self._update_grid()
            cost = result.get("cost", 0)
            if cost < 0:
                self.status_label.config(
                    text=f"Odkryto políčko. Cena: {cost} bodů",
                    fg=config.COLOR_TEXT
                )
            else:
                self.status_label.config(
                    text="Odkryto políčko (zdarma)",
                    fg=config.COLOR_TEXT
                )
        else:
            self.status_label.config(
                text=result.get("message", "Chyba"),
                fg=config.COLOR_WRONG
            )

    def _update_timer(self):
        """Update timer display"""
        if not self.running:
            return

        remaining = self.game.get_remaining_time()
        
        if remaining <= 0:
            remaining = 0
            if not self.game.is_game_over():
                self.game.end_game("timeout")
                self._show_game_over()

        minutes = int(remaining // 60)
        seconds = int(remaining % 60)
        self.timer_label.config(text=f"{config.TEXT_TIME_REMAINING} {minutes}:{seconds:02d}")

        # Update points
        self.points_label.config(text=f"{config.TEXT_SCORE} {self.game.get_current_points()}")

        # Update hint string
        self._update_hint_display()

        if self.running:
            self.root.after(200, self._update_timer)

    def _on_cell_click(self, cell_index: int):
        """Handle cell click in the grid"""
        if self.game.is_game_over():
            messagebox.showwarning("Game Over", "Hra již skončila.")
            return

        result = self.game.reveal_cell(cell_index)

        if result["success"]:
            self._update_grid()
            cost = result.get("cost", 0)
            if cost < 0:
                self.status_label.config(
                    text=f"Odkryto políčko. Cena: {cost} bodů",
                    fg=config.COLOR_TEXT
                )
            else:
                self.status_label.config(
                    text="Odkryto políčko (zdarma)",
                    fg=config.COLOR_TEXT
                )
        else:
            self.status_label.config(
                text=result.get("message", "Chyba"),
                fg=config.COLOR_WRONG
            )

    def _on_reveal_button(self):
        """Handle reveal button - let user click a cell"""
        self.status_label.config(
            text="Klikněte na políčko, které chcete odkrýt",
            fg=config.COLOR_TEXT
        )

    def _on_hint_button(self):
        """Handle letter hint button"""
        if self.game.is_game_over():
            messagebox.showwarning("Game Over", "Hra již skončila.")
            return

        result = self.game.use_letter_hint()

        if result["success"]:
            cost = result.get("cost", 0)
            self.status_label.config(
                text=f"Nápověda: {result.get('hint_string')}. Cena: {cost} bodů",
                fg=config.COLOR_TEXT
            )
        else:
            self.status_label.config(
                text=result.get("message", "Chyba"),
                fg=config.COLOR_WRONG
            )

    def _on_submit_answer(self):
        """Handle answer submission"""
        if self.game.is_game_over():
            messagebox.showwarning("Game Over", "Hra již skončila.")
            return

        answer = self.answer_input.get().strip()
        if not answer:
            messagebox.showwarning("Prázdná odpověď", "Zadejte prosím odpověď.")
            return

        result = self.game.submit_answer(answer)

        if result["success"]:
            if result["correct"]:
                messagebox.showinfo(
                    "Správně!",
                    f"Správná odpověď: {result['correct_answer']}\nFinální skóre: {result['points']} bodů"
                )
                self._show_game_over()
            else:
                cost = result.get("cost", 0)
                messagebox.showwarning(
                    "Chybná odpověď",
                    f"Chybně! Odpověď byla: {result['correct_answer']}\nZtraceli jste {-cost} bodů\nSoučasné skóre: {result['points']} bodů"
                )
                self.answer_input.delete(0, tk.END)
        else:
            messagebox.showerror("Chyba", result.get("message", "Neznámá chyba"))

    def _on_quit(self):
        """Handle quit button"""
        if messagebox.askyesno("Konec hry", "Opravdu chcete skončit? Vaše skóre se uloží."):
            self.game.end_game("user_quit")
            self._show_game_over()

    def _show_game_over(self):
        """Show game over screen"""
        self.running = False
        
        final_points = self.game.get_current_points()
        reason = self.game.state.game_end_reason
        
        reason_text = {
            "timeout": "Čas vypršel",
            "completed": "Úspěšně vyřešena",
            "user_quit": "Ukončena hráčem"
        }.get(reason, "Neznámý důvod")

        messagebox.showinfo(
            "Konec hry",
            f"Hra skončila\nDůvod: {reason_text}\nFinální skóre: {final_points} bodů"
        )

        # Save results
        from data_loader import DataLoader
        loader = DataLoader()
        loader.save_results(self.game.get_state_dict())

        self.root.destroy()

    def on_state_change(self, state_dict: dict):
        """Callback for game state changes"""
        if self.running:
            self.root.after(0, self._update_grid)


def create_placeholder_image():
    """Create a placeholder image if no real image available"""
    img = Image.new('RGB', config.IMAGE_SIZE, color=(200, 200, 200))
    return img


def run_game(question: Question):
    """Main function to run the game"""
    root = tk.Tk()

    # Load or create image
    try:
        if question.image_path and os.path.exists(question.image_path):
            image = image_processor.load_image(question.image_path)
            image = image_processor.resize_image(image)
        else:
            image = create_placeholder_image()
    except Exception as e:
        print(f"Error loading image: {e}")
        image = create_placeholder_image()

    # Create game
    game = QuizGame(question, state_callback=None)

    # Create UI
    window = GameWindow(root, game, image)
    game.state_callback = window.on_state_change

    root.mainloop()
