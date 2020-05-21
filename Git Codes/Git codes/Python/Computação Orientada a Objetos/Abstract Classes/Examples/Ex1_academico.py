from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self,nome, endereco, idade):
        #Construtor
        self.__nome = nome
        self.__endereco = endereco
        self.__idade = idade
    
    def getNome(self):
        return self.__nome
    
    def getEndereco(self):
        return self.__endereco
    
    def getIdade(self):
        return self.__idade
    
    @abstractmethod
    def printDescricao(self):
        pass

class Professor(Pessoa):
    #Construtor
    def __init__(self, nome, endereco, idade, titulacao):
        #Chama construtor da superclasse
        super().__init__(nome, endereco, idade)
        self.__titulacao = titulacao
    
    def getTitulacao(self):
        return self.__titulacao
    
    def printDescricao(self):
        print('Nome: {}.'.format(self.getNome()))
        print('Endereço: {}.'.format(self.getEndereco()))
        print('Idade: {}.'.format(self.getIdade()))
        print('Titulação: {}.'.format(self.getTitulacao()))

class Aluno(Pessoa):
    #Construtor
    def __init__(self, nome, endereco, idade, curso):
        #Chama o construtor da superclasse
        super().__init__(nome, endereco, idade)
        self.__curso = curso
    
    def getCurso(self):
        return self.__curso
    
    def printDescricao(self):
        print('Nome: {}.'.format(self.getNome()))
        print('Endereço: {}.'.format(self.getEndereco()) )
        print('Idade: {}.'.format(self.getIdade()))
        print('Curso: {}.'.format(self.getCurso()))


prof = Professor('Joao', 'Av.Bps, 1303', 33, 'doutorado')
prof.printDescricao()
print('-----------------------------------------------------------------')
aluno = Aluno('Joao Lucas', 'Av.Bps, 1212', 33, 'Sistemas de informação')
aluno.printDescricao()