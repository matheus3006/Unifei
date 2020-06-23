import tkinter as tk

#EXEMPLO 2:
class Exemplo:
    #Construtor
    def __init__(self):
        #Cria uma janela
        self.janela = tk.Tk()
        #Nomeia a janela
        self.janela.title('Segundo teste')
        #Atribui um rótulo a essa janela e passa a própria janela como argumento, depois um testo
        self.rotulo = tk.Label(self.janela, text = "Olha, funciona!")
        #Chama um método pack(), que é um pacote
        self.rotulo.pack()
        #Chama o mainloop para renderizar a janela na tela
        self.janela.mainloop()

def renderiza():
    Exemplo()

renderiza()