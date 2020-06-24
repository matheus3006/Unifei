import tkinter as tk
from tkinter import messagebox

class Disciplina:

    def __init__(self, codigo, nome):
        self.__codigo = codigo
        self.__nome = nome

    def getCodigo(self):
        return self.__codigo
    
    def getNome(self):
        return self.__nome
    
class LimiteInsereDisciplinas(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Disciplina")
        self.controle = controle

        self.frameCode = tk.Frame(self)
        self.frameNome = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCode.pack()
        self.frameNome.pack()
        self.frameButton.pack()
      
        self.labelCode = tk.Label(self.frameCode,text="Código: ")
        self.labelNome = tk.Label(self.frameNome,text="Nome:    ")
        self.labelCode.pack(side="left")
        self.labelNome.pack(side="left")  

        self.inputCode = tk.Entry(self.frameCode, width=20)
        self.inputCode.pack(side="left")
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")             
      
        self.buttonSubmit = tk.Button(self.frameButton ,text="Cadastrar", font = ('Arial Black', 8))      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.cadastraHandler)
      
        self.buttonClear = tk.Button(self.frameButton ,text="Clear", font = ('Arial Black', 8))      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)  

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído", font = ('Arial Black', 8))      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)
    
class LimiteMostraDisciplinas():
    def __init__(self, str):
        messagebox.showinfo('Lista de disciplinas', str)
    
class CtrlDisciplina():       
    def __init__(self):
        self.listaDisciplinas = []
         
    def insereDisciplinas(self):
        self.limiteInsc = LimiteInsereDisciplinas(self)
    
    def mostraDisciplinas(self):
        if len(self.listaDisciplinas) == 0:
            str = "Não há disciplinas cadastradas"
            self.limiteLista = LimiteMostraDisciplinas(str)
        else:
            str = "Código -- Nome\n"
            for disc in self.listaDisciplinas:
                str += disc.getCodigo() + ' -- ' + disc.getNome() + '\n'
            self.limiteLista = LimiteMostraDisciplinas(str)
    
    def cadastraHandler(self, event):
        if len(self.limiteInsc.inputCode.get()) == 0 or len(self.limiteInsc.inputNome.get()) == 0:
            self.limiteInsc.mostraJanela('Falha', 'Preencha todos os campos!')
        else:
            Code = self.limiteInsc.inputCode.get()
            nome = self.limiteInsc.inputNome.get()
            disciplina = Disciplina(Code, nome)
            self.listaDisciplinas.append(disciplina)
            self.limiteInsc.mostraJanela('Sucesso', 'Disciplina cadastrada!')
            self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteInsc.inputCode.delete(0, len(self.limiteInsc.inputCode.get()))
        self.limiteInsc.inputNome.delete(0, len(self.limiteInsc.inputNome.get()))
        
    def fechaHandler(self, event):
        self.limiteInsc.destroy()