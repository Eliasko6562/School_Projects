import tkinter as tk
import random as rand
from tkinter import simpledialog  as sd
from tkinter import colorchooser as cc

try:
    from files.happiness.data_loader import load_data as ld
except:
    pass

class App: 
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Demo GUI")
        self.root.geometry("800x600")
        
        self.canvas = tk.Canvas(self.root, width=800, height=600, bg="white")
        self.canvas.pack(fill="both", expand=True)
        
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        m_tasks = tk.Menu(menubar, tearoff=False)
        m_tasks.add_command(label="Exit", command=self.root.destroy)
        menubar.add_cascade(label="System", menu=m_tasks)
        
        m_colors = tk.Menu(menubar, tearoff=False)
        m_colors.add_command(label="Red", command=lambda: self.set_bg("red"))
        m_colors.add_command(label="Green", command=lambda: self.set_bg("green"))
        m_colors.add_command(label="Blue", command=lambda: self.set_bg("blue"))
        menubar.add_cascade(label="Colors", menu=m_colors)
        
        m_entertainment = tk.Menu(menubar, tearoff=False)
        m_entertainment.add_command(label="Magické Čáry", command=lambda: self.magic_barcode(25, 100))
        m_entertainment.add_command(label="Šachovnice", command=lambda: self.chessboard_dialog())
        m_entertainment.add_command(label="Terč", command=lambda: self.set_bg("blue"))
        menubar.add_cascade(label="Entertainment", menu=m_entertainment)
        
    def _canvas_size(self) -> tuple:
        w = self.canvas.winfo_width() or self.root.winfo_width() or 640
        h = self.canvas.winfo_height() or 600
        return w, h
        
    def magic_barcode(self, min: int, max:int) -> None:
        self.reset()
        x = 0
        w, h = self._canvas_size()
        while x < w:
            width = rand.randint(min , max)
            color = f"#{rand.randint(0x0, 0xffffff):06x}"
            self.canvas.create_line(x, 0, x, h, fill=color, width=width)
            x += width
            
    def chessboard(self, size: int = 8, color1: str="black", color2: str="white") -> None:
        self.reset()
        self.canvas.config(bg="white")
        w, h = self._canvas_size()
        cell_x = w / size
        cell_y = h / size
        for y in range(size):
            for x in range(size):
                color = color1 if (x + y) % 2 == 0 else color2
                self.canvas.create_rectangle(x * cell_x, y * cell_y, x * cell_x + cell_x,y * cell_y + cell_y, fill=color)
            
    def chessboard_dialog(self):
        size = sd.askinteger(title="Šachovnice",
                            prompt="Zadej počet polí",
                            minvalue=2,
                            maxvalue=20,
                            initialvalue=8,
                            parent=self.root)
        color1 = cc.askcolor(title="Vyber pozadí")[1]
        color2 = cc.askcolor(title="Vyber barvu")[1]
        self.chessboard(size=size, color1=color1, color2=color2)
        
    def set_bg(self, color: str) -> None:
        self.canvas.config(background=color)   
        
    def reset(self) -> None:
        self.canvas.delete("all") 
        self.canvas.config(bg="white")    
        
    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    App().run()