class Televisao:
    #Construtor
    def __init__(self, marca, estado):
        self.__marca = marca
        self.__estado = estado
    
    def getMarca(self):
        return self.__marca
    
    def isTvEmQualEstado(self):
        return self.__estado
    
    #Métodos de instância
    def ligaTv(self):
        if self.__estado == True:
            print('A tv ja estava ligada!')
        else:
            self.__estado = True
            print('A tv acaba de ser ligada!')
    
    def desligaTv(self):
        if self.__estado == False:
            print('A tv ja estava desligada!')
        else:
            self.__estado = False
            print('A tv acaba de ser desligada!')

    def mostraAtributos(self):
        print('A tv é da marca {}.'.format(self.getMarca()))
        if(self.isTvEmQualEstado()):
            print('A tv esta ligada.')
        else:
            print('A tv esta desligada.')
    
#Executando intruções:
T = Televisao('Philips', False)
T.mostraAtributos()
print("""----------------------
Tentando ligar a tv:""")
T.ligaTv()
T.mostraAtributos()
print("""----------------------
Tentando desligar a tv:""")
T.desligaTv()
T.mostraAtributos()