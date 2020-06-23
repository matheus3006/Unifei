import tkinter as tk

class Jan:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title('Personagens da Cartoon Network')

        self.frame1 = tk.Frame(self.janela)
        self.frame2 = tk.Frame(self.janela)
        self.frame3 = tk.Frame(self.janela)

        self.rotulo1 = tk.Label(self.frame1, text = ('Mutante Rex'), font = ('Arial Black', 22))
        self.rotulo2 = tk.Label(self.frame2, text = ('Ben 10'), font = ('Arial Black', 22))
        self.rotulo3 = tk.Label(self.frame3, text = ('Max Steel'), font = ('Arial Black', 22))

        self.rotulo1.pack(side = 'top')
        self.rotulo2.pack(side = 'top')
        self.rotulo3.pack(side = 'top')
        self.frame1.pack(side = 'top')
        self.frame2.pack(side = 'top')
        self.frame3.pack(side = 'top')
        
        self.janela.mainloop()

def ChamaJan():
    Jan()

ChamaJan()
