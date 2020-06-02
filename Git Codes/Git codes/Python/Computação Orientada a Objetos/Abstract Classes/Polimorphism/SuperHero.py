from abc import ABC, abstractmethod

class SuperHero(ABC):
    #Construtor
    def __init__(self, nome, identidadeReal, superPoder, vilao):
        self.__nome = nome
        self.__identidadeReal = identidadeReal
        self.__superPoder = superPoder
        self.__vilao = vilao
    
    def getNome(self):
        return self.__nome
    
    def getIdentidadeReal(self):
        return self.__identidadeReal
    
    def getSuperPoder(self):
        return self.__superPoder
    
    def getVilao(self):
        return self.__vilao
    
    @abstractmethod
    def getVitoria(self):
        pass

class Arrow(SuperHero):
    #Construtor
    def __init__(self, nome, identidadeReal, superPoder, vilao, vitoria):
        #Chama construtor da super classe
        super().__init__(nome, identidadeReal, superPoder, vilao)
        self.__vitoria = vitoria

    def getVitoria(self):
        return self.__vitoria

class Flash(SuperHero):
    #Construtor
    def __init__(self, nome, identidadeReal, superPoder, vilao, vitoria, velocidade):
        #Chama construtor da super classe
        super().__init__(nome, identidadeReal, superPoder, vilao)
        self.__vitoria = vitoria
        self.__velocidade = velocidade

    def getVelocidade(self):
        return self.__velocidade

    def getVitoria(self):
        return self.__vitoria

#Executando as instruções com o primeiro herói
h1 = Arrow('Arqueiro verde', 'Oliver Queen', 'atirar flechas', 'Prometheus', 'atirando flechas venenosas')

print("""Herói e relatório de luta:
Nome: {}.
Identidade real: {}.
Poderes: {}.
Vilão: {}.
Como o vilão foi derrotado: {} venceu {} {}."""
.format(h1.getNome(), h1.getIdentidadeReal(), h1.getSuperPoder(), h1.getVilao(), h1.getNome(), h1.getVilao(), h1.getVitoria()))

print('---------------------------------------------------------------------------------------------------------')

#Executando as instruções com o segundo herói
h2 = Flash('Flash', 'Barry Allen', 'Super velocidade', 'Zoom', 'dando o soco de massa infinita', 100000000000)

print("""Herói e relatório de luta:
Nome: {}.
Identidade real: {}.
Poderes: {}.
Vilão: {}.
Como o vilão foi derrotado: {} venceu {} {} a {} km/h."""
.format(h2.getNome(), h2.getIdentidadeReal(), h2.getSuperPoder(), h2.getVilao(), h2.getNome(),
h2.getVilao(), h2.getVitoria(), h2.getVelocidade()))