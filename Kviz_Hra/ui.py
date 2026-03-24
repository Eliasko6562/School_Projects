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

        self.grid_buttons = []
        for row in range(config.GRID_SIZE):
            button_row = []
            for col in range(config.GRID_SIZE):
                cell_index = row * config.GRID_SIZE + col
                btn = tk.Button(
                    grid_frame,
                    command=lambda idx=cell_index: self._on_cell_click(idx)
                )
                btn.grid(row=row, column=col, padx=2, pady=2)
                button_row.append(btn)

            self.grid_buttons.append(button_row)

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
            font=config.FONT_ANSWER_INPUT,
            width=40
        )
        self.answer_input.pack(fill=tk.X, pady=5)
        self.answer_input.bind("<Return>", lambda e: self._on_submit_answer())

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
        """Update grid button appearance based on revealed cells"""
        revealed = self.game.get_revealed_cells()
        
        for row in range(config.GRID_SIZE):
            for col in range(config.GRID_SIZE):
                cell_index = row * config.GRID_SIZE + col
                is_revealed = cell_index in revealed

                if is_revealed:
                    # Show the actual image cell when revealed
                    cells = image_processor.get_grid_cells(self.original_image)
                    cell_img = cells[cell_index]
                    button_img = cell_img.resize(
                        (config.CELL_SIZE, config.CELL_SIZE),
                        Image.Resampling.LANCZOS
                    )
                else:
                    # Show solid color tile when not revealed (completely hide the image)
                    button_img = Image.new('RGB', (config.CELL_SIZE, config.CELL_SIZE), config.COLOR_HIDDEN)

                # Convert to PhotoImage
                photo = ImageTk.PhotoImage(button_img)
                self.button_images[cell_index] = photo

                btn = self.grid_buttons[row][col]
                btn.config(image=photo)
                btn.image = photo  # Keep reference

                # Disable already revealed buttons
                if is_revealed:
                    btn.config(state=tk.DISABLED)

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
        self.hint_display.config(text=self.game.get_hint_string())

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

        self.root.quit()

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
