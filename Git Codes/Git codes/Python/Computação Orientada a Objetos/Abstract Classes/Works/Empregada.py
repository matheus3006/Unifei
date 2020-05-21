from abc import ABC, abstractmethod

class EmpDomestica(ABC):
    #Construtor
    def __init__(self, nome, telefone):
        self.__nome = nome
        self.__telefone = telefone
    
    def getNome(self):
        return self.__nome

    def getTelefone(self):
        return self.__telefone
    
    @abstractmethod
    def getSalario(self):
        pass

class Horista(EmpDomestica):
    #Construtor
    def __init__(self, nome, telefone, horasTrabalhadas, valorPorHora):
        #Chama construtor da superclasse
        super().__init__(nome, telefone)
        self.__horasTrabalhadas = horasTrabalhadas
        self.__valorPorHora = valorPorHora
    
    def getHorasTrabalhadas(self):
        return self.__horasTrabalhadas
    
    def getValorPorHora(self):
        return self.__valorPorHora
    
    #Função que calcula o salário mensal
    def getSalario(self):
        salario = self.getHorasTrabalhadas() * self.getValorPorHora()
        return salario
    
    def imprimeSalarioMensal(self):
        print("""Nome: {}.
Telefone: {}.
Salário Mensal: {}.""".format(self.getNome(), self.getTelefone(), self.getSalario()))

class Diarista(EmpDomestica):
    #Construtor
    def __init__(self, nome, telefone, diasTrabalhados, valorPorDia):
        #Chama construtor da superclasse
        super().__init__(nome, telefone)
        self.__diasTrabalhados = diasTrabalhados
        self.__valorPorDia = valorPorDia
    
    def getDiasTrabalhados(self):
        return self.__diasTrabalhados
    
    def getValorPorDia(self):
        return self.__valorPorDia
    
   #Função que calcula o salário mensal
    def getSalario(self):
        salario = self.getDiasTrabalhados() * self.getValorPorDia()
        return salario

    def imprimeSalarioMensal(self):
        print("""Nome: {}.
Telefone: {}.
Salário Mensal: {}.""".format(self.getNome(), self.getTelefone(), self.getSalario()))

class Mensalista(EmpDomestica):
    #Construtor
    def __init__(self, nome, telefone, valorMensal):
        #Chama construtor da superclasse
        super().__init__(nome, telefone)
        self.__ValorMensal = valorMensal
    
    def getValorMensal(self):
        return self.__ValorMensal
    
    def getSalario(self):
        return self.getValorMensal()
    
    def imprimeSalarioMensal(self):
        print("""Nome: {}.
Telefone: {}.
Salário Mensal: {}.""".format(self.getNome(), self.getTelefone(), self.getSalario()))    

#Executando as instruções
print('Estas são as empregadas disponíveis:\n')

#Printando características da empregada horista  
horista = Horista('Vania da Silva', '35999876534', 160, 10)
horista.imprimeSalarioMensal()
print()

#Printando características da empregada diarista  
diarista = Diarista('Elizabete Sanchez', '35999976627', 20, 55)
diarista.imprimeSalarioMensal()
print()

#Printando características da empregada mensalista  
mensalista = Mensalista('Judite Francisca Lemes', '35998124780', 1000)
mensalista.imprimeSalarioMensal()
print()

if horista.getSalario() < diarista.getSalario():
    if horista.getSalario() < mensalista.getSalario():
        print('A empregada cujo salário é o mais barato é:')
        horista.imprimeSalarioMensal()
    else:
        print('A empregada cujo salário é o mais barato é:')
        mensalista.imprimeSalarioMensal()

if diarista.getSalario() < horista.getSalario():
    if diarista.getSalario() < mensalista.getSalario():
        print('A empregada cujo salário é o mais barato é:')
        diarista.imprimeSalarioMensal()
    else:
        print('A empregada cujo salário é o mais barato é:')
        mensalista.imprimeSalarioMensal() 