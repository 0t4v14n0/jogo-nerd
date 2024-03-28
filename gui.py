import tkinter as tk
from tkinter import PhotoImage

class MinhaApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("JOGO-NERD")
        self.geometry("500x500")
        
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        
        self.pagina_atual = None
        self.mostrar_pagina(PaginaInicial)
    
    def mostrar_pagina(self, pagina):
        nova_pagina = pagina(self.container, self)
        if self.pagina_atual is not None:
            self.pagina_atual.destroy()
        self.pagina_atual = nova_pagina
        self.pagina_atual.grid(row=0, column=0, sticky="nsew")
        
class PaginaInicial(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        self.img_menup = PhotoImage(file="imagens/inicio.png")

        self.labelfundo = tk.Label(self, image=self.img_menup)
        self.labelfundo.pack()

        submit_button = tk.Button(self, text="INICIAR", command=lambda: controller.mostrar_pagina(Dificuldade))
        submit_button.place(x=200, y=400,width=100,height=20)

class Dificuldade(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        def mostrar_selecao():
            # Obtém o valor selecionado
            selecionado = var.get()
    
            # Dificuldade
            if   selecionado == 1:
                print("Dificuldade selecionada: Fácil")
            elif selecionado == 2:
                print("Dificuldade selecionada: Médio")
            elif selecionado == 3:
                print("Dificuldade selecionada: Difícil")
            elif selecionado == 4:
                print("Dificuldade selecionada: NERD")

            controller.mostrar_pagina(game)
    

        self.img_menup = PhotoImage(file="imagens/fnada.png")

        self.labelfundo = tk.Label(self, image=self.img_menup)
        self.labelfundo.pack()

        var = tk.IntVar()

        self.radio1 = tk.Radiobutton(self, text="Fácil", variable=var, value=1)
        self.radio1.place(x=100, y=300,width=100,height=20)

        self.radio2 = tk.Radiobutton(self, text="Médio", variable=var, value=2)
        self.radio2.place(x=100, y=350,width=100,height=20)

        self.radio3 = tk.Radiobutton(self, text="Difícil", variable=var, value=3)
        self.radio3.place(x=100, y=400,width=100,height=20)

        self.radio3 = tk.Radiobutton(self, text="Nerd", variable=var, value=4)
        self.radio3.place(x=100, y=450,width=100,height=20)

        self.selecionar_button = tk.Button(self, text="Selecionar", command=mostrar_selecao)
        self.selecionar_button.place(x=300, y=400,width=100,height=20)

class game(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        print ('ola')

if __name__ == "__main__":
    app = MinhaApp()
    app.mainloop()
    
