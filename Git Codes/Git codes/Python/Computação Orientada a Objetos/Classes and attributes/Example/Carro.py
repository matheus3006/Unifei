class Carro:
    #Construtor
    def __init__(self, marca, cor, motorLigado, portaMalasCheio):
        self.__marca = marca
        self.__cor = cor
        self.__motorLigado = motorLigado
        self.__portaMalasCheio = portaMalasCheio
    
    def getMarca(self):
        return self.__marca
    
    def getCor(self):
        return self.__cor

    def isMotorLigado(self):
        return self.__motorLigado
    
    def isPortaMalasCheio(self):
        return self.__portaMalasCheio
    
    #Métodos de instância
    def ligaMotor(self):
        if self.__motorLigado == True:
            print('Seu motor ja estava ligado!')
        else:
            self.__motorLigado = True
            print('Seu motor acaba de ser ligado!')
    
    def enchePortaMalas(self):
        if self.__portaMalasCheio == True:
            print('Seu porta malas ja estava cheio!')
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
            print('Seu porta malas esta vazio.')
        
c = Carro('Chevrolet', 'Vermelho', False, False)
c.mostraAtributos()
print('------------------------')
print('Tentando ligar o seu motor:')
c.ligaMotor()
print('Tentando encher o seu porta malas:')
c.enchePortaMalas()
c.mostraAtributos()
