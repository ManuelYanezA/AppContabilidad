# Multiple classes module for screens

import tkinter as tk
from constants import style, config

class Home(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background = style.BACKGROUND)
        self.controller = controller
        self.workMode = tk.StringVar(self, value="Calculo IVA")

        self.init_widgets()
    
    def move_to_IVA(self):
        self.controller.show_frame(CalculoIVA)
    def move_to_Previred(self):
        self.controller.show_frame(UsuariosPrevired)

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
        optionsFrame = tk.Frame(self)
        optionsFrame.configure(background=style.COMPONENT)
        optionsFrame.pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True,
            padx = 22,
            pady = 11
        )
        tk.Label(
            optionsFrame,
            text= "Elija un modo de trabajo",
            justify= tk.CENTER,
            **style.STYLE
        ).pack(
            side= tk.TOP,
            fill= tk.X,
            padx= 22,
            pady= 11
        )

        #for(key, value) in config.MODES.items():
        #    tk.Radiobutton(
        #        optionsFrame,
        #        text = key,
        #        variable = self.workMode,
        #        value=value,
        #        activebackground = style.BACKGROUND,
        #        activeforeground = style.TEXT,
        #        **style.STYLE
        #    ).pack(
        #        side = tk.LEFT,
        #        fill = tk.BOTH,
        #        expand = True,
        #        padx = 5,
        #        pady = 5
        #    )
        
        tk.Button(
            self,
            text = "Cálculo de IVA",
            command = self.move_to_IVA,
            **style.STYLE,
            relief = tk.FLAT,
            activebackground = style.BACKGROUND,
            activeforeground = style.TEXT,
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx = 22,
            pady = 11
        )
        tk.Button(
            self,
            text = "Lista Usuarios Previred",
            command = self.move_to_Previred,
            **style.STYLE,
            relief = tk.FLAT,
            activebackground = style.BACKGROUND,
            activeforeground = style.TEXT,
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx = 22,
            pady = 11
        )

class CalculoIVA(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background = "green")
        self.controller = controller

        self.init_widgets()
    
    def init_widgets(self):
        tk.Label(
            self,
            text = "Cálculo de IVA",
            justify = tk.CENTER,
            **style.STYLE
        ).pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True,
            padx = 22,
            pady = 11
        )

class UsuariosPrevired(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background = "blue")
        self.controller = controller

        self.init_widgets()
    
    def init_widgets(self):
        tk.Label(
            self,
            text = "Lista de Usuarios Previred",
            justify = tk.CENTER,
            **style.STYLE
        ).pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True,
            padx = 22,
            pady = 11
        )