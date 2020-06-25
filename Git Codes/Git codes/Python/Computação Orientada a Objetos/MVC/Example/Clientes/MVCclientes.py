import tkinter as tk
from tkinter import messagebox

# M = Model              
# V = View | Cria-se uma view principal, e outras views para cada janela diferente
# C = Controller        

#Exceptions de tratamento de email
class UsernameDuplicado(Exception):
    pass

class EmailInvalido(Exception):
    pass

class ModelCliente():
    def __init__(self, nome, email):
        self.__nome = nome
        self.__email = email

    def getNome(self):
        return self.__nome

    def getEmail(self):
        return self.__email

class View():
    # Master é a janela principal e o controller controla a view
    def __init__(self, master, controller):
        self.controller = controller
        self.frame = tk.Frame(master)
        self.frame.pack()
        self.viewPanel = ViewPanel(master, controller)

class ViewPanel():
    # Root é a janela principal e o controller controla a viewPanel
    def __init__(self, root, controller):
        self.controller = controller
        self.janela = tk.Frame(root)
        self.janela.pack()
        self.frame1 = tk.Frame(self.janela)
        self.frame2 = tk.Frame(self.janela)
        self.frame1.pack()
        self.frame2.pack()
      
        self.labelInfo1 = tk.Label(self.frame1,text="Nome: ")
        self.labelInfo2 = tk.Label(self.frame2,text="Email:  ")
        self.labelInfo1.pack(side="left")
        self.labelInfo2.pack(side="left")  

        self.inputText1 = tk.Entry(self.frame1, width=24)
        self.inputText1.pack(side="left")
        self.inputText2 = tk.Entry(self.frame2, width=24)
        self.inputText2.pack(side="left")             
      
        self.buttonSubmit = tk.Button(self.janela,text="Enter", font = ('Arial Black', 8))      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controller.enterHandler)
      
        self.buttonClear = tk.Button(self.janela,text="Clear", font = ('Arial Black', 8))      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controller.clearHandler)         
    
        self.buttonClientes = tk.Button(self.janela, text = 'Mostra clientes', font = ('Arial Black', 8))
        self.buttonClientes.pack(side = 'left')
        self.buttonClientes.bind("<Button>", controller.clientesHandler)

        self.buttonSair = tk.Button(self.janela, text = 'Sair', font = ('Arial black', 8))
        self.buttonSair.pack(side = 'left')
        self.buttonSair.bind("<Button>", controller.exitHandler)

    def mostraJanela(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)

class Controller():        
    def __init__(self):
        self.root = tk.Tk()
        self.listaClientes = []

        # Cria a View passando referência da janela principal
        # de si próprio
        self.view = View(self.root, self)

        self.root.title("Exemplo MVC")
        # Inicia o mainloop()
        self.root.mainloop()

    def enterHandler(self, event):
        if len(self.view.viewPanel.inputText1.get()) == 0 or len(self.view.viewPanel.inputText2.get()) == 0:
            self.message = 'Preencha os campos obrigatórios!'
            self.view.viewPanel.mostraJanela('Falha', self.message)
        else:
            nomeCliente = self.view.viewPanel.inputText1.get()
            emailCliente = self.view.viewPanel.inputText2.get()
            try:
                emailPartes = emailCliente.split('@')
                if len(emailPartes) != 2 or not emailPartes[1]:
                    raise EmailInvalido()
            except EmailInvalido:
                self.view.viewPanel.mostraJanela('Falha', "'%s' nao é um endereço de email válido" % emailCliente)
            
            else:
                cliente = ModelCliente(nomeCliente, emailCliente)
                self.listaClientes.append(cliente)
                self.view.viewPanel.mostraJanela('Sucesso', 'Cliente cadastrado com sucesso')
                self.clearHandler(event)

    def clearHandler(self, event):
        self.view.viewPanel.inputText1.delete(0, len(self.view.viewPanel.inputText1.get()))
        self.view.viewPanel.inputText2.delete(0, len(self.view.viewPanel.inputText2.get()))

    def clientesHandler(self, event):
        self.message = 'Clientes cadastrados:\n'
        if len(self.listaClientes) == 0:
            self.message = 'Ainda não há clientes cadastrados'
            self.view.viewPanel.mostraJanela('Lista de Clientes', self.message)
        else:
            for cliente in self.listaClientes:
                self.message += cliente.getNome() + ' - ' + cliente.getEmail() + "\n"
            self.view.viewPanel.mostraJanela('Lista de clientes', self.message)
    
    def exitHandler(self, event):
        self.root.destroy()

if __name__ == '__main__':
    c = Controller()