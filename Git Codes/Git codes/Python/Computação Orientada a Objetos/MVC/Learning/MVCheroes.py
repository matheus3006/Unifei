import tkinter as tk
from tkinter import messagebox

#Primeiro de tudo, criar uma classe modelo
class ModelHero():
    def __init__(self, nome, identSecreta):
        self.__nome = nome
        self.__identSecreta = identSecreta

    def getNome(self):
        return self.__nome
    
    def getIdentSecreta(self):
        return self.__identSecreta

#Depois, criar uma view, que é a visão que o usuário final terá (interface)
class View():
    def __init__(self, master, controller):
        self.controller = controller
        self.frame = tk.Frame(master)
        self.frame.pack()
        
        #Cria um viewPanel, passando referência da janela pricipal e do controller
        self.viewPanel = ViewPanel(master, controller)

#Aqui é onde se cria a visão da janela
class ViewPanel():
    def __init__(self, root, controller):
        self.controller = controller
        self.janela = tk.Frame(root)
        self.janela.pack()
        self.frameNome = tk.Frame(self.janela)
        self.frameNome.pack()
        self.frameIdent = tk.Frame(self.janela)
        self.frameIdent.pack()
        self.frameButtons = tk.Frame(self.janela)
        self.frameButtons.pack()

        self.labelNome = tk.Label(self.frameNome, text = 'Nome:                      ')
        self.labelNome.pack(side = 'left')
        self.labelIdent = tk.Label(self.frameIdent, text = 'Identidade secreta: ')
        self.labelIdent.pack(side = 'left')

        self.inputNome = tk.Entry(self.frameNome, width = 20)
        self.inputNome.pack(side = 'left')
        self.inputIdent = tk.Entry(self.frameIdent, width = 20)
        self.inputIdent.pack(side = 'left')

        self.buttonCadastrar = tk.Button(self.frameButtons, text = 'Cadastrar', font = ('Arial black', 8))
        self.buttonCadastrar.pack(side = 'left')
        self.buttonCadastrar.bind("<Button>", controller.CadastrarHandler)

        self.buttonClear = tk.Button(self.frameButtons, text = 'Clear', font = ('Arial black', 8))
        self.buttonClear.pack(side = 'left')
        self.buttonClear.bind("<Button>", controller.clearHandler)

        self.buttonHeroes = tk.Button(self.frameButtons, text = 'Mostrar Heróis', font = ('Arial black', 8))
        self.buttonHeroes.pack(side = 'left')
        self.buttonHeroes.bind("<Button>", controller.HeroesHandler)

        self.buttonExit = tk.Button(self.frameButtons, text = 'Exit', font = ('Arial black', 8))
        self.buttonExit.pack(side = 'left')
        self.buttonExit.bind("<Button>", controller.exitHandler)
        
    def MostraMensagem(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)

#Por fim, criar a classe controller
class Controller():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('300x100')
        self.listaHerois = []

        self.view = View(self.root, self)

        self.root.title("Cadastro de heróis")

        self.root.mainloop()

    def CadastrarHandler(self, event):
        if len(self.view.viewPanel.inputNome.get()) == 0 or len(self.view.viewPanel.inputIdent.get()) == 0:
            self.message = 'Preencha todos os campos!'
            self.view.viewPanel.MostraMensagem('Falha', self.message)
        else:
            self.message = 'Seu cadastro foi realizado!'
            HeroName = self.view.viewPanel.inputNome.get()
            HeroIdent = self.view.viewPanel.inputIdent.get()
            heroi = ModelHero(HeroName, HeroIdent)
            self.listaHerois.append(heroi)
            self.view.viewPanel.MostraMensagem('Sucesso', self.message)
            self.clearHandler(event)

    def clearHandler(self, event):
        self.view.viewPanel.inputNome.delete(0, len(self.view.viewPanel.inputNome.get()))
        self.view.viewPanel.inputIdent.delete(0, len(self.view.viewPanel.inputIdent.get()))
    
    def HeroesHandler(self, event):
        if len(self.listaHerois) == 0:
            self.message = 'Não há heróis cadastrados'
            self.view.viewPanel.MostraMensagem('Lista de heróis\n', self.message)
        else:
            for hero in self.listaHerois:
                self.message = hero.getNome() + ' - ' + hero.getIdentSecreta() + '\n' 
            self.view.viewPanel.MostraMensagem('Lista de heróis\n', self.message)

    def exitHandler(self, event):
        self.root.destroy()

if __name__ == '__main__':
    c = Controller()
