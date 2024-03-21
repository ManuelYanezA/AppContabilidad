# Multiple classes module for screens

import tkinter as tk
from constants import style

class Home(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background = style.BACKGROUND)
        self.controller = controller
        self.screenName = tk.StringVar(self, value="Principal")

        self.init_widgets()
    
    def init_widgets(self):
        tk.Label(
            self,
            text = "App Contabilidad",
            justify = tk.CENTER,
            **style.STYLE
        ).pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True,
            padx = 22,
            pady = 11
        )

class Test(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background = style.BACKGROUND)
        self.controller = controller