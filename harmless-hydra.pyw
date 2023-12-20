# STILL TO DO
# make windows teleport to random places
# have original window actually close when closed - make it look like it at least

import tkinter as tk
from random import randint

root = tk.Tk()
root.geometry = ('400x300')
root.title('Virus')

def create():
    root = tk.Tk()
    root.geometry = ('400x300')
    root.title('Virus')
    root.protocol("WM_DELETE_WINDOW", create)
    root = tk.Tk()
    root.geometry = ('400x300')
    root.title('Virus')
    root.protocol("WM_DELETE_WINDOW", create)

root.protocol("WM_DELETE_WINDOW", create)
root.mainloop()
