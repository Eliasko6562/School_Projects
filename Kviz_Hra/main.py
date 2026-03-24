"""
Main entry point for Kviz_Hra application
"""

import tkinter as tk
from tkinter import messagebox
from data_loader import DataLoader
import ui
import config


def main():
    """Main application entry point"""
    
    # Load questions
    loader = DataLoader()
    
    if not loader.load_questions():
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror(
            "Chyba",
            f"Nepodařilo se načíst otázky z: {config.QUESTIONS_FILE}\n\n"
            "Ujistěte se, že soubor existuje a je validní JSON."
        )
        root.destroy()
        return

    questions = loader.get_all_questions()
    
    if not questions:
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror(
            "Chyba",
            "V souboru s otázkami nejsou žádné otázky."
        )
        root.destroy()
        return

    # Show question selection
    root = tk.Tk()
    root.title("Kviz Hra - Výběr Otázky")
    root.geometry("400x300")

    label = tk.Label(
        root,
        text="Vyberte otázku:",
        font=("Arial", 12, "bold")
    )
    label.pack(pady=10)

    # Listbox with questions
    listbox = tk.Listbox(root, font=("Arial", 10))
    listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    for i, q in enumerate(questions):
        listbox.insert(tk.END, f"{i+1}. {q.title} ({q.category})")

    # Select first by default
    listbox.selection_set(0)

    def start_game():
        selection = listbox.curselection()
        if not selection:
            messagebox.showwarning("Výběr", "Vyberte prosím otázku.")
            return

        question_index = selection[0]
        selected_question = questions[question_index]
        root.destroy()
        
        # Run the game
        ui.run_game(selected_question)

    button = tk.Button(
        root,
        text="Spustit Hru",
        command=start_game,
        font=("Arial", 11),
        bg="#00AA00",
        fg="white",
        padx=20,
        pady=10
    )
    button.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
