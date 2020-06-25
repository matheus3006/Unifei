import tkinter as tk

class GUI:

    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title('Filósofos')
    
        self.botão1 = tk.Button(self.janela, text = ('Nietzsche'), font = ('Arial black', 10), command = self.processaB1)
        self.botão2 = tk.Button(self.janela, text = (' Sócrates '), font = ('Arial black', 10), command = self.processaB2)
        self.botãoClear = tk.Button(self.janela, text = ('Limpar'), font = ('Arial black', 10), command = self.clear)
        self.botaoSair = tk.Button(self.janela, text = 'Sair', font = ('Arial black', 10), command = self.sair)

        self.label = tk.Label(self.janela, text = ('Escolha um filósofo e receba uma citação...'), font = ('Arial', 13))
        self.space1 = tk.Label(self.janela, text = ('    '))
        self.space2 = tk.Label(self.janela, text = ('    '))

        self.botão1.pack()
        self.botão2.pack()
        self.space1.pack()
        self.label.pack()
        self.space2.pack()
        self.botãoClear.pack()
        self.botaoSair.pack()

        tk.mainloop()

    def processaB1(self):
        self.label.configure(text = 'Aquele que tem um porquê para viver pode suportar quase qualquer como.', font = ('Arial', 13))
    
    def processaB2(self):
        self.label.configure(text = 'Para se encontrar, pense por conta própria.', font = ('Arial', 13))
    
    def clear(self):
        self.label["text"] = "Escolha um filósofo e receba uma citação..."
    
    def sair(self):
        self.janela.destroy()
    
def main():
    GUI()

main()