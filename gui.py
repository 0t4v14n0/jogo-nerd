import tkinter as tk
from tkinter import PhotoImage
from models.calcular import Calcular

dificuldade_global = 0
pontos = 0

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

        submit_button = tk.Button(self, text="INICIAR", command=lambda: controller.mostrar_pagina(Dificuldade),font=("Arial", 30))
        submit_button.place(x=160, y=400)

class Dificuldade(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        def mostrar_selecao():

            # Obtém o valor selecionado
            selecionado = var.get()

            global dificuldade_global

            # Dificuldade
            if selecionado == 1:
                dificuldade_global = 1
                print("Dificuldade selecionada: Fácil")
            elif selecionado == 2:
                dificuldade_global = 2
                print("Dificuldade selecionada: Médio")
            elif selecionado == 3:
                dificuldade_global = 3
                print("Dificuldade selecionada: Difícil")
            elif selecionado == 4:
                dificuldade_global = 4
                print("Dificuldade selecionada: NERD")

            controller.mostrar_pagina(Game)
    

        self.img_menup = PhotoImage(file="imagens/fnada.png")

        self.labelfundo = tk.Label(self, image=self.img_menup)
        self.labelfundo.pack()

        var = tk.IntVar()

        self.radio1 = tk.Radiobutton(self, text="Fácil", variable=var, value=1,font=("Arial", 20))
        self.radio1.place(x=50, y=250)

        self.radio2 = tk.Radiobutton(self, text="Médio", variable=var, value=2,font=("Arial", 20))
        self.radio2.place(x=50, y=300)

        self.radio3 = tk.Radiobutton(self, text="Difícil", variable=var, value=3,font=("Arial", 20))
        self.radio3.place(x=50, y=350)

        self.radio3 = tk.Radiobutton(self, text="Nerd", variable=var, value=4,font=("Arial", 20))
        self.radio3.place(x=50, y=400)

        self.selecionar_button = tk.Button(self, text="Selecionar", command=mostrar_selecao,font=("Arial", 20))
        self.selecionar_button.place(x=280, y=400)

class Game(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        self.img_menup = PhotoImage(file="imagens/fnadaa.png")

        self.labelfundo = tk.Label(self, image=self.img_menup)
        self.labelfundo.pack()

        def atuponto():
            newponto = "Voce tem "+ str(pontos) +" pontos"
            self.texto_dinamico = tk.Label(self, text= newponto, font=("Arial", 15))
            self.texto_dinamico.place(x=300, y=10)
            return
        
        def enviar_resu():
            global pontos 
            resposta = self.entrada_texto.get()
            if calc.checar_resultado(int(resposta)):
               pontos = pontos + 1
               atuponto()
            print("enviado:", resposta)

        calc: Calcular = Calcular(dificuldade_global)
        print (calc)

        atuponto()

        self.texto_dinamico = tk.Label(self, text=calc.mostrar_operacao(), font=("Arial", 30))
        self.texto_dinamico.place(x=50, y=300)

        self.entrada_texto = tk.Entry(self,font=("Arial", 30))
        self.entrada_texto.place(x=250, y=300,width=150)

        self.botao_enviar = tk.Button(self, text="Enviar", command=enviar_resu,font=("Arial", 20))
        self.botao_enviar.place(x=100, y=350)

class Continuar(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

if __name__ == "__main__":
    app = MinhaApp()
    app.mainloop()
