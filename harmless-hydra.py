import tkinter as tk
import random

class MainWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Virus")
        self.geometry("300x200")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        self.open_new_windows()

    def open_new_windows(self):
        for _ in range(2):
            new_window = tk.Toplevel(self)
            new_window.title("New Window")
            new_window.geometry(f"{random.randint(100, 400)}x{random.randint(100, 300)}")

if __name__ == "__main__":
    main_window = MainWindow()
    main_window.mainloop()
