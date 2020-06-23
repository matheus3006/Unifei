import tkinter as tk

class FazAlgo:

    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Minha janela")
        #Vou criar um frame
        self.frame = tk.Frame(self.janela)
        #Vou criar um rotulo para o frame da janela
        self.rotulo = tk.Label(self.frame, text = ('Rótulo'), font = ('Aria Black', 32))
        #Vou empacotar o rotulo
        self.rotulo.pack(side = 'top')
        #Vou empacotar o frame
        self.frame.pack()
        #Vou por a janela em loop
        self.janela.mainloop()

def main():
    FazAlgo()

main()
