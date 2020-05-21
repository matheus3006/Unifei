from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self,nome, endereco, idade, listaDisc):
        #Construtor
        self.__nome = nome
        self.__endereco = endereco
        self.__idade = idade
        self.__listaDisc = listaDisc

    def getNome(self):
        return self.__nome
    
    def getEndereco(self):
        return self.__endereco
    
    def getIdade(self):
        return self.__idade
    
    @abstractmethod
    def printDescricao(self):
        pass

    def getListaDisc(self):
        return self.__listaDisc

    def insereDisc(self, disc):
        self.__listaDisc.append(disc)

class Professor(Pessoa):
    #Construtor
    def __init__(self, nome, endereco, idade, titulacao, listaDisc):
        #Chama construtor da superclasse
        super().__init__(nome, endereco, idade, listaDisc)
        self.__titulacao = titulacao
    
    def getTitulacao(self):
        return self.__titulacao
    
    def printDescricao(self):
        print('Nome: {}.'.format(self.getNome()))
        print('Endereço: {}.'.format(self.getEndereco()))
        print('Idade: {}.'.format(self.getIdade()))
        print('Titulação: {}.'.format(self.getTitulacao()))
        print('Disciplina(s) ministrada(s):')
        listaDisc = self.getListaDisc()
        for disc in listaDisc:
            print('Nome: {} - Carga horária: {}'.format(disc.getNomeDisc(), disc.getCargaHoraria()))

class Aluno(Pessoa):
    #Construtor
    def __init__(self, nome, endereco, idade, curso, listaDisc):
        #Chama o construtor da superclasse
        super().__init__(nome, endereco, idade, listaDisc)
        self.__curso = curso
    
    def getCurso(self):
        return self.__curso
    
    def printDescricao(self):
        print('Nome: {}.'.format(self.getNome()))
        print('Endereço: {}.'.format(self.getEndereco()) )
        print('Idade: {}.'.format(self.getIdade()))
        print('Curso: {}.'.format(self.getCurso()))
        print('Disciplinas cursadas:')
        listaDisc = self.getListaDisc()       
        for disc in listaDisc:
            print('Nome: {} - Carga horária: {}'.format(disc.getNomeDisc(), disc.getCargaHoraria()))

class Disciplina():
    def __init__(self, nomeDisc, cargaHoraria):
        self.__nomeDisc = nomeDisc
        self.__cargaHoraria = cargaHoraria

    def getNomeDisc(self):
        return self.__nomeDisc

    def getCargaHoraria(self):
        return self.__cargaHoraria

disc1 = Disciplina('Programação OO', 64)   
disc2 = Disciplina('Estrutura de dados', 64)   
disc3 = Disciplina('Contabilidade', 64)   
listaDisc1 = [disc1, disc2]
listaDisc2 = [disc2, disc3]

prof = Professor('Joao', 'Av. BPS, 1303', 33, 'doutorado', [])
prof.insereDisc(disc1)
prof.insereDisc(disc2)
prof.printDescricao()
print()
aluno = Aluno('Pedro', 'Av. Cesario Alvin, 234', 20, 'SIN', [])
aluno.insereDisc(disc2)
aluno.insereDisc(disc3)
aluno.printDescricao()  
aluno.insereDisc(disc1) 
aluno.printDescricao()  

