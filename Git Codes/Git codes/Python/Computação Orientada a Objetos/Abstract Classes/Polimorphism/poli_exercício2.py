from abc import ABC, abstractmethod

class Professor(ABC):
    def __init__(self, nome, matricula, cargaHoraria, salarioLiquido, aliquota):
        self.__nome = nome
        self.__matricula = matricula
        self.__cargaHoraria = cargaHoraria
        self.__salarioLiquido = salarioLiquido
        self.__aliquota = aliquota

    def getNome(self):
        return self.__nome

    def getMatricula(self):
        return self.__matricula

    def getCargaHoraria(self):
        return self.__cargaHoraria
    
    def CalculaAliquota(self):
       if self.__salario <= 1903.98:
           return 0
        elif self.__salario >= 1903.99 and s

    @abstractmethod
    def getSalario(self):
        pass

    @abstractmethod
    def CalculaSalarioLiquido(self):
        pass

class ProfDE(Professor):
    def __init__(self, nome, matricula, cargaHoraria, salarioLiquido, salario):
        super().__init__(nome, matricula, cargaHoraria, salarioLiquido)
        self.__salario = salario

    def setSalario(self, salario):
        self.__salario = salario

    def getSalario(self):
        return self.__salario
    
    def CalculaSalarioLiquido(self):
        Liquido = self.__salario + (self.__salario * 0.11) - 

class ProfHorista(Professor):
    def __init__(self, nome, matricula, cargaHoraria, salarioHora):
        super().__init__(nome, matricula, cargaHoraria)
        self.__salarioHora = salarioHora

    def setSalarioHora(self, salarioHora):
        self.__salarioHora = salarioHora 

    def getSalarioHora(self):
        return self.__salarioHora

    def getSalario(self):
        return self.__salarioHora * self.getCargaHoraria()

prof1 = ProfDE('Joao', 12345, 40, 5000)
prof2 = ProfHorista('Paulo', 54321, 30, 75)
prof3 = ProfHorista('Ana', 56789, 38, 95)
profs = [prof1, prof2, prof3]
for prof in profs:
    print ('Nome: {} - Salário: {}'.format(prof.getNome(), prof.getSalario()))