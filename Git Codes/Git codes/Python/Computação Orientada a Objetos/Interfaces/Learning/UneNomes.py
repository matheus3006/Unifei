import tkinter as tk

class Formulario:

    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Formulário teste")

        self.enunciado = tk.Frame(self.janela)
        self.entrada1 = tk.Frame(self.janela)
        self.entrada2 = tk.Frame(self.janela)
        self.resultado = tk.Frame(self.janela)

        self.explicaLabel = tk.Label(self.enunciado, text = ('Digite dois nomes para uní-los!'), font = ('Arial', 14))
        self.explicaLabel.pack()
        self.inputLabel = tk.Label(self.entrada1, text = ('Digite um nome:'), font = ('Arial', 14))
        self.inputLabel.pack(side = 'left')
        self.inputLabel2 = tk.Label(self.entrada2, text = ('Digite outro nome:'), font = ('Arial', 14))
        self.inputLabel2.pack(side = 'left')
        self.resultLabel = tk.Label(self.resultado, text = (' '), font = ('Arial black', 20))
        self.resultLabel.pack()

        self.input = tk.Entry(self.entrada1, width = 30)
        self.input.pack(side = 'left')
        self.input2 = tk.Entry(self.entrada2, width = 30)
        self.input2.pack(side = 'left')

        self.enunciado.pack()
        self.entrada1.pack()
        self.entrada2.pack()
        self.resultado.pack()

        self.botaoFundir = tk.Button(self.janela, text = ('Fundir'), font = ('Arial black', 10), command = self.Fundir)
        self.botaoFundir.pack(side = 'left')
        self.botaoLimpar = tk.Button(self.janela, text = ('Limpar'), font = ('Arial black', 10), command = self.Limpar)
        self.botaoLimpar.pack(side = 'left')
        self.botaoFinalizar = tk.Button(self.janela, text = ('Finalizar'), font = ('Arial black', 10), command = self.janela.destroy)
        self.botaoFinalizar.pack(side = 'left')
        tk.mainloop()

    def Fundir(self):
        self.resultLabel["text"] = self.input.get() + ' ' + self.input2.get() + '!'
    
    def Limpar(self):
        self.input.delete(0, len(self.input.get()))
        self.input2.delete(0, len(self.input2.get()))
        self.resultLabel["text"] = " "

def CallFormulario():
    Formulario()

CallFormulario()