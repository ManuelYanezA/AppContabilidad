# Multiple classes module for screens

import tkinter as tk
from constants import style

class Home(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background = style.BACKGROUND)
        self.controller = controller

class Test(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background = style.BACKGROUND)
        self.controller = controller