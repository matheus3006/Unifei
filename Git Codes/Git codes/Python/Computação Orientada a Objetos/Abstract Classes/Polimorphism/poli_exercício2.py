from abc import ABC, abstractmethod

class Professor(ABC):
    #Construtor
    def __init__(self, nome, matricula, CargaHoraria, salarioBruto):
        self.__nome = nome
        self.__matricula = matricula
        self.__CargaHoraria = CargaHoraria
        self.__salarioBruto = salarioBruto

    def getNome(self):
        return self.__nome
    
    def getMatricula(self):
        return self.__matricula
    
    def getCargaHoraria(self):
        return self.__CargaHoraria

    def getSalarioBruto(self):
        return self.__salarioBruto

    def calculaValorImposto(self, salarioBruto):
        if self.getSalarioBruto() < 1903.99:
            imposto = 0
        elif self.getSalarioBruto() < 2826.65:
            imposto = 0.075
        elif self.getSalarioBruto() < 3751.06:
            imposto = 0.15
        elif self.getSalarioBruto() < 4664.68:
            imposto = 0.225
        else:
            imposto = 0.275
        if imposto == 0:
            return 0
        else:
            return self.__salarioBruto * imposto

    @abstractmethod
    def getSalarioLiquido(self):
        pass

    @abstractmethod
    def CalculaSalarioLiquido(self):
        pass

class ProfDE(Professor):
    #Construtor
    def __init__(self, nome, matricula, CargaHoraria, salarioBruto):
        #Construtor da superclasse
        super().__init__(nome, matricula, CargaHoraria, salarioBruto)

    def setSalarioBruto(self, salarioBruto):
        self.__salarioBruto = salarioBruto
    
    def getSalarioBruto(self):
        return self.__salarioBruto
    
    def CalculaSalarioLiquido(self):
        #Calcular o valor da contribuição previdenciária
        previd = self.getSalarioBruto() * 0.11

        #SalarioLiquido = Salario Bruto - (previdencia + imposto)
        SalarioLiquido = self.getSalarioBruto() - (previd + self.calculaValorImposto(self.__salarioBruto))
        return SalarioLiquido

class ProfHorista(Professor):
    #Construtor
    def __init__(self, nome, matricula, CargaHoraria, salarioBruto):
        #Construtor da superclasse
        super().__init__(nome, matricula, CargaHoraria, salarioBruto)

    def setSalarioBruto(self, salarioBruto):
        self.__salarioBruto = salarioBruto
    
    def getSalarioBruto(self):
        return self.__salarioBruto
    
    def CalculaSalarioLiquido(self):
        SalarioLiquido = (self.getSalarioBruto() * self.__CargaHoraria) - self.calculaValorImposto(self.getSalarioBruto())
        return SalarioLiquido

Prof1 = ProfDE('José Ferretto', '12345', 64, 5600)
Prof2 = ProfHorista('Fernando Jacinto', '67890', 38, 90)
Prof3 = ProfDE('Antônio Nunes', '101112', 56, 95)

Profs = [Prof1, Prof2, Prof3]

for Prof in Profs:
    print('Nome: {} - Salário: {}.'.format(Prof.getNome(), Prof.CalculaSalarioLiquido()))