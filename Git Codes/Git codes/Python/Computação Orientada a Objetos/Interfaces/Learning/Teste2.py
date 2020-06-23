import tkinter as tk

class FazAlgo:

    def __init__(self):

        self.janela = tk.Tk()
        self.janela.title('Surpresa!')
        self.rotulo = tk.Label(self.janela, text = "Shazam!", font = ("Arial Bold", 54))
        self.rotulo.pack()
        self.janela.mainloop()

def Funcao():
    FazAlgo()

Funcao()