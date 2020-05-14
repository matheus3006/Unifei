class Lampada:
    #Construtor
    def __init__(self, estadoDaLampada):
        self.__estadoDaLampada = estadoDaLampada
    
    def isLampadaEmQueEstado(self):
        return self.__estadoDaLampada
    
    #Método de instância
    def acende(self):
        if self.__estadoDaLampada == True:
            print('A lampada ja estava acesa!')
        else:
            self.__estadoDaLampada = True
            print('A lampada acaba de ser acesa!')
    
    def apaga(self):
        if self.__estadoDaLampada == False:
            print('A lampada ja estava apagada!')
        else:
            self.__estadoDaLampada = False
            print('A lampada acaba de ser apagada!')
    
    def mostraEstado(self):
        if self.__estadoDaLampada == True:
            print('A lampada esta acesa.')
        else:
            print('A lampada esta apagada.')
    
L = Lampada(True)
L.mostraEstado()
print('Tentando acender a lampada:')
L.acende()
print('-----------------------------')
print('Mostrando estado da lampada:')
L.mostraEstado()
print('-----------------------------')
print('Tentando apagar a lampada:')
L.apaga()
print('-----------------------------')
print('Mostrando estado da lampada:')
L.mostraEstado()