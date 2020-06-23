import tkinter as tk
from tkinter import messagebox

class Janela:

    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title('Checklist')

        self.frame1 = tk.Frame(self.janela)
        self.frame2 = tk.Frame(self.janela)
        self.frameFinal = tk.Frame(self.janela)

        self.pergunta = tk.Label(self.frame1, text = ('Qual das frases abaixo pertence ao "Seu Madruga" do seriado Chaves?'),
        font = ('Arial', 12))
        self.pergunta.pack()

        self.cbv1 = tk.IntVar()
        self.cbv2 = tk.IntVar()
        self.cbv3 = tk.IntVar()
        self.cbv4 = tk.IntVar()

        self.cbv1.set(0)
        self.cbv2.set(0)
        self.cbv3.set(0)
        self.cbv4.set(0)

        self.cb1 = tk.Checkbutton(self.frame2, text = '(a) Pague o aluguel!', variable = self.cbv1)
        self.cb2 = tk.Checkbutton(self.frame2, text = '(b) Só não te dou outra porque...', variable = self.cbv2)
        self.cb3 = tk.Checkbutton(self.frame2, text = '(c) Venha tesouro, não se misture com essa gentalha!', variable = self.cbv3)
        self.cb4 = tk.Checkbutton(self.frame2, text = '(d) Foi sem querer querendo...', variable = self.cbv4)

        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()

        self.botaoEnviar = tk.Button(self.frameFinal, text = 'Enviar', font = ('Arial black', 10), command = self.Enviar)
        self.botaoEnviar.pack(side = 'left')
        self.botaoSair = tk.Button(self.frameFinal, text = 'Sair', font = ('Arial black', 10), command = self.janela.destroy)
        self.botaoSair.pack(side = 'left')

        self.frame1.pack()
        self.frame2.pack()
        self.frameFinal.pack()

        tk.mainloop()
    
    def Enviar(self):
        self.correção = 'Sua resposta está '

        if self.cbv2.get() == 1:
            self.correção = self.correção + ' correta!\nProvavelmente você é um fã deste seriado...'
            messagebox.showinfo('Gabarito', self.correção)
        else:
            self.correção = self.correção + ' errada!\nProvavelmente você não assistiu ao seriado...\n' + 'Resposta correta: alternativa (b)'
            messagebox.showinfo('Gabarito', self.correção)        

def ChamaJanela():
    Janela()

ChamaJanela()