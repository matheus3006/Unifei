import tkinter as tk

class Qualquer:

    def __init__(self):

        self.janela = tk.Tk()
        self.janela.title('Nomeei a janela')
        self.janela.rotulo = tk.Label(self.janela, text = "Rotulei a janela")
        self.janela.rotulo.pack()
        self.janela.mainloop()

def funcaoQualquer():
    Qualquer()

funcaoQualquer()