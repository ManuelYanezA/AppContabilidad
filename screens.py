# Multiple classes module for screens

import tkinter as tk
from tkinter import *
from tkinter import ttk
from constants import style, config
import locale

class Home(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background = style.BACKGROUND_WINDOW)
        self.controller = controller
        self.workMode = tk.StringVar(self, value="Calculo IVA")

        self.init_widgets()
    
    def move_to_IVA(self):
        self.controller.show_frame(CalculoIVA)
    def move_to_Previred(self):
        self.controller.show_frame(UsuariosPrevired)

    def init_widgets(self):
        optionsFrame = tk.Frame(self)
        optionsFrame.configure(background=style.COMPONENT_TEXT)
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
            **style.BUTTON_STYLE,
            relief = tk.FLAT,
            activebackground = style.BACKGROUND_WINDOW,
            activeforeground = style.TEXT_FG,
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
            **style.BUTTON_STYLE,
            relief = tk.FLAT,
            #activebackground = style.BACKGROUND_WINDOW,
            #activeforeground = style.TEXT_FG,
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx = 22,
            pady = 11
        )

class CalculoIVA(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background = style.BACKGROUND_WINDOW)
        self.controller = controller

        self.result_precio_bruto = 0
        self.result_valor_neto = 0
        self.result_IVA_A = 0
        self.result_IVA_B = 0

        locale.setlocale(locale.LC_ALL, 'es_CL.UTF-8') #Activar formato para números como divisa CLP

        for i in range(3):
            self.grid_columnconfigure(i, weight=1)
        for i in range(6):
            self.grid_rowconfigure(i, weight=1)

        self.init_widgets()
    
    def calcularIVA(self):
        try:
            value = int(self.precio_Bruto.get())
            self.result_valor_neto = round(value * 1.19)
            self.result_IVA_A = round(value * 0.19)
            self.label_valor_neto.config(text= "$ " + locale.format_string("%d", self.result_valor_neto, grouping=True))
            self.label_iva_A.config(text= "$ " + locale.format_string("%d", self.result_IVA_A, grouping=True))
        except ValueError:
            print("ERROR: Must be an Integer")
    
    def calcularPrecioBruto(self):
        try:
            value = int(self.valor_Neto.get())
            self.result_precio_bruto = round(value / 1.19)
            self.result_IVA_B = round(self.result_precio_bruto * 0.19)
            self.label_precio_bruto.config(text= "$ " + locale.format_string("%d", self.result_precio_bruto, grouping=True))
            self.label_iva_B.config(text= "$ " + locale.format_string("%d", self.result_IVA_B, grouping=True))
        except ValueError:
            print("ERROR: Must be an Integer")

    def init_widgets(self):
        #Label de Precio en bruto (Sin IVA)
        tk.Label(
            self,
            text = "Monto Neto",
            justify = tk.CENTER,
            **style.STYLE
        ).grid(
            column=0,
            row=0,
            sticky=tk.NSEW,
            padx=22,
            pady=11
        )

        #Label Valor Neto (Precio Bruto + IVA)
        tk.Label(
            self,
            text = "Monto Total",
            justify = tk.CENTER,
            **style.STYLE
        ).grid(
            column=2,
            row=0,
            sticky=tk.NSEW,
            padx=22,
            pady=11
        )

        #Entrada para precio bruto
        self.precio_Bruto = tk.StringVar()
        precio_Bruto_Entry = tk.Entry(self, width = 20, textvariable = self.precio_Bruto)
        precio_Bruto_Entry.grid(
            column=0,
            row=1,
            sticky=tk.N,
            ipady=2
        )

        #Entrada para valor neto
        self.valor_Neto = tk.StringVar()
        valor_Neto_Entry = tk.Entry(self, width = 20, textvariable = self.valor_Neto)
        valor_Neto_Entry.grid(
            column=2,
            row=1,
            sticky=tk.N,
            ipady=2
        )

        tk.Button(
            self,
            text="Calcular IVA",
            command=self.calcularIVA,
            **style.BUTTON_STYLE,
            relief = tk.FLAT,
        ).grid(
            column=0,
            row=2,
            sticky=tk.N,
            padx=2,
            pady=2
        )

        tk.Button(
            self,
            text="Calcular Monto Neto",
            command=self.calcularPrecioBruto,
            **style.BUTTON_STYLE,
            relief = tk.FLAT,
        ).grid(
            column=2,
            row=2,
            sticky=tk.N,
            padx=2,
            pady=2
        )

        tk.Label(
            self,
            text = "Monto Total",
            justify = tk.CENTER,
            **style.STYLE
        ).grid(
            column=0,
            row=3,
            sticky=tk.S,
            padx=2,
            pady=2
        )

        self.label_precio_bruto = tk.Label(
            self,
            text = "$ " + str(self.result_precio_bruto),
            justify = tk.CENTER,
            **style.STYLE
        )
        self.label_precio_bruto.grid(
            column=2,
            row=4,
            sticky=tk.N,
            padx=2,
            pady=2
        )

        tk.Label(
            self,
            text = "Monto Neto",
            justify = tk.CENTER,
            **style.STYLE
        ).grid(
            column=2,
            row=3,
            sticky=tk.S,
            padx=2,
            pady=2
        )

        self.label_valor_neto = tk.Label(
            self,
            text = "$ " + str(self.result_valor_neto),
            justify = tk.CENTER,
            **style.STYLE
        )
        self.label_valor_neto.grid(
            column=0,
            row=4,
            sticky=tk.N,
            padx=2,
            pady=2
        )

        tk.Label(
            self,
            text = "IVA",
            justify = tk.CENTER,
            **style.STYLE
        ).grid(
            column=0,
            row=5,
            sticky=tk.S,
            padx=2,
            pady=2
        )

        tk.Label(
            self,
            text = "IVA",
            justify = tk.CENTER,
            **style.STYLE
        ).grid(
            column=2,
            row=5,
            sticky=tk.S,
            padx=2,
            pady=2
        )

        self.label_iva_A = tk.Label(
            self,
            text = "$ " + str(self.result_IVA_A),
            justify = tk.CENTER,
            **style.STYLE
        )
        self.label_iva_A.grid(
            column=0,
            row=6,
            sticky=tk.N,
            padx=2,
            pady=2
        )

        self.label_iva_B = tk.Label(
            self,
            text = "$ " + str(self.result_IVA_B),
            justify = tk.CENTER,
            **style.STYLE
        )
        self.label_iva_B.grid(
            column=2,
            row=6,
            sticky=tk.N,
            padx=2,
            pady=2
        )

        ttk.Separator(
            self,
            orient='vertical'
        ).grid(
            column=1,
            row=0,
            rowspan=8,
            sticky=tk.NS
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