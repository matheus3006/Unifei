class Veiculo:
    def __init__(self, marca, cor, motorLigado):
        self.__marca = marca
        self.__cor = cor
        self.__motorLigado = motorLigado

    def getMarca(self):
        return self.__marca
    
    def getCor(self):
        return self.__cor

    def isMotorLigado(self):
        return self.__motorLigado

    def ligaMotor(self):
        if self.__motorLigado == True:
            print('O motor ja esta ligado!')
        else:
            self.__motorLigado = True
            print('O motor acaba de ser ligado!')
    
class Motocicleta(Veiculo):
    #Construtor
    def __init__(self, marca, cor, motorLigado, estilo):
        #chama um contrutor da super classe
        super().__init__(marca, cor, motorLigado)
        self.__estilo = estilo

    def getEstilo(self):
        return self.__estilo

    def mostraAtributos(self):
        print('Esta moto é uma {} {}, estilo {}.'.format(self.getMarca(), self.getCor(), self.getEstilo()))
        if(self.isMotorLigado()):
            print('Seu motor esta ligado.')
        else:
            print('Seu motor esta desligado.')
    
class Carro(Veiculo):
    #Construtor
    def __init__(self, marca, cor, motorLigado, portaMalasCheio):
        #Chama o construtor da super classe
        super().__init__(marca, cor, motorLigado)
        self.__portaMalasCheio = portaMalasCheio

    def isPortaMalasCheio(self):
        return self.__portaMalasCheio

    #Métodos de instância
    def enchePortaMalas(self):
        if self.__portaMalasCheio == True:
            print('Seu porta malas ja esta cheio!')
        else:
            self.__portaMalasCheio = True
            print('Seu porta malas acaba de ser carregado!')
    
    def mostraAtributos(self):
        print('Este carro é um {} {}.'.format(self.getMarca(), self.getCor()))
        if(self.isMotorLigado()):
            print('Seu motor esta ligado.')
        else:
            print('Seu motor esta desligado.')
        if(self.isPortaMalasCheio()):
            print('Seu porta malas esta cheio.')
        else:
            print('Seu porta malas esta vazio')
    
#Executando as intruções:
m = Motocicleta('Honda', 'preta', False, 'Cg fun')
m.mostraAtributos()
m.ligaMotor()
m.mostraAtributos()
print('-------------')
c = Carro('Gol', 'prata', False, False)
c.mostraAtributos()
c.ligaMotor()
c.enchePortaMalas()
c.mostraAtributos()   
    
        
