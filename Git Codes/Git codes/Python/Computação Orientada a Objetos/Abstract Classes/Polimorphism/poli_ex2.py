from abc import ABC, abstractmethod

class Professor(ABC):
    #Construtor
    def __init__(self, nome, matricula, CargaHoraria):
        self.__nome = nome
        self.__matricula = matricula
        self.__CargaHoraria = CargaHoraria
    
    def getNome(self):
        return self.__nome
    
    def getMatricula(self):
        return self.__matricula
    
    def getCargaHoraria(self):
        return self.__CargaHoraria
    
    @abstractmethod
    def getSalario(self):
        pass

class ProfDE(Professor):
    #Construtor
    def __init__(self, nome, matricula, CargaHoraria, salario):
        #Construtor da superclasse
        super().__init__(nome, matricula, CargaHoraria)
        self.__salario = salario
    
    def setSalario(self, salario):
        self.__salario = salario
    
    def getSalario(self):
        return self.__salario
    
class ProfHorista(Professor):
    #Construtor
    def __init__(self, nome, matricula, CargaHoraria, salarioHora):
        #Construtor da superclasse
        super().__init__(nome, matricula, CargaHoraria)
        self.__salarioHora = salarioHora
    
    def setSalarioHora(self, salarioHora):
        self.__salarioHora = salarioHora
    
    def getSalarioHora(self):
        return self.__salarioHora
    
    def getSalario(self):
        return self.__salarioHora * self.getCargaHoraria()
    
prof1 = ProfDE('Matheus', 20190999, 64, 5000)
prof2 = ProfHorista('James', 20190034, 30, 75)
prof3 = ProfHorista('Janete', 20196437, 36, 80)
profs =[prof1, prof2, prof3]
for prof in profs:
    print('Nome: {} - Salário: {}.'.format(prof.getNome(), prof.getSalario()))