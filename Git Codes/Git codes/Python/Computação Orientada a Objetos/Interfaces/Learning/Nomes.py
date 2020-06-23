import tkinter as tk

class Janela:

    def __init__(self):

        self.janela = tk.Tk()
        self.janela.title('Nomes:')

        #Criando frames
        self.frameTopo = tk.Frame(self.janela)
        self.frameBase = tk.Frame(self.janela)

        #Rotulando frames
        self.nome1 = tk.Label(self.frameTopo, text = ('João Lucas Ribeiro'), font = ("Arial", 14))
        self.nome2 = tk.Label(self.frameBase, text = ('Diana Cristina dos Santos Borges'), font = ("Arial", 14))

        #Empacotando rotulos dos frames como uma lista
        self.nome1.pack(side = "top")
        self.nome2.pack(side = "top")

        #Empacotando os frames
        self.frameTopo.pack(side = "top")
        self.frameBase.pack(side = "top")

        #Pondo a janela em loop
        self.janela.mainloop()

def Chama():
    Janela()

Chama()