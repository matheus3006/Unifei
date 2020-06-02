from abc import ABC, abstractmethod

class Professor(ABC):
    #Construtor
    def __init__(self, nome, matricula, CargaHoraria, salarioBruto, imposto):
        self.__nome = nome
        self.__matricula = matricula
        self.__CargaHoraria = CargaHoraria
        self.__salarioBruto = salarioBruto
        self.__imposto = imposto

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

class ProfDE(Professor):
    #Construtor
    def __init__(self, nome, matricula, CargaHoraria, salarioBruto, SalarioLiquido):
        #Construtor da superclasse
        super().__init__(nome, matricula, CargaHoraria, salarioBruto, imposto)
        self.__salarioLiquido = SalarioLiquido

    def setSalarioBruto(self, salarioBruto):
        self.__salarioBruto = salarioBruto
    
    def getSalarioBruto(self):
        return self.__salarioBruto
    
    def getSalarioLiquido(self):
        #Calcular o valor da contribuição previdenciária
        previd = self.getSalarioBruto() * 0.11

        #SalarioLiquido = Salario Bruto - (previdencia + imposto)
        SalarioLiquido = self.getSalarioBruto() - (previd + calculaValorImposto(self.__salarioBruto))

class ProfHorista(Professor):
    #Construtor
    def __init__(self, nome, matricula, CargaHoraria, salarioBruto, imposto, SalarioLiquido):
        #Construtor da superclasse
        super().__init__(nome, matricula, CargaHoraria, salarioBruto, imposto)
    
    def setSalarioBruto(self, salarioBruto):
        self.__salarioBruto = salarioBruto
    
    def getSalarioBruto(self):
        return self.__salarioBruto
    
    def getSalarioLiquido(self):
        return self.__salarioBruto * self.getCargaHoraria()
    
prof1 = ProfDE('Matheus', 20190999, 64, 5000)
prof2 = ProfHorista('James', 20190034, 30, 75)
prof3 = ProfHorista('Janete', 20196437, 36, 80)
profs =[prof1, prof2, prof3]
for prof in profs:
    print('Nome: {} - Salário: {}.'.format(prof.getNome(), prof.getSalario()))