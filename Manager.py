# Unique class module

import tkinter as tk


class Manager(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("App Contabilidad")