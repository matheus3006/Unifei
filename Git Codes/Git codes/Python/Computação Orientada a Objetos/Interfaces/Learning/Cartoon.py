import tkinter as tk

class MyFunction:
    #Construtor
    def __init__(self):
        #Criar a janela
        self.jan = tk.Tk()

        #Nomear a janela
        self.jan.title('Heróis da Cartoon Network')

        #Criar 2 frames
        self.frameBase = tk.Frame(self.jan)
        self.frameTopo = tk.Frame(self.jan)

        #Rotular frame base
        self.MtRx = tk.Label(self.frameBase, text = ('Mutante Rex'), font = ('Arial Black', 50))
        self.Ben = tk.Label(self.frameBase, text = ('Ben 10'), font = ('Arial Black', 50))
        self.Max = tk.Label(self.frameBase, text = ('Max Steel'), font = ('Arial Black', 50))

        #Rotular frame topo
        self.meninas = tk.Label(self.frameTopo, text = ('Meninas super poderosas'), font = ('Arial Black', 30))
        self.espia = tk.Label(self.frameTopo, text = (' As 3 espiãs demais'), font = ('Arial Black', 30))

        #Empacotar rótulos nos frames
        self.MtRx.pack()
        self.Ben.pack()
        self.Max.pack()
        self.meninas.pack(side = 'left')
        self.espia.pack(side = 'left')

        #Empacotar frames na janela
        self.frameBase.pack()
        self.frameTopo.pack()

        #Rodar a janela
        self.jan.mainloop()
    
def Call():
    MyFunction()

Call()
