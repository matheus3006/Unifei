class Aparelho:
    #Construtor
    def __init__(self, marca, estado):
        self.__marca = marca
        self.__estado = estado
    
    def getMarca(self):
        return self.__marca
    
    def isEmQueEstado(self):
        return self.__estado
    
    #Métodos de instância
    def ligaAparelho(self):
        if self.__estado == True:
            print('Já estava ligado(a)!')
        else:
            self.__estado = True
            print('Ligado(a) com sucesso!')
    
    def desligaAparelho(self):
        if self.__estado == False:
            print('Já estava desligado(a)!')
        else:
            self.__estado = False
            print('Desligado(a) com sucesso!')
        
class Televisao(Aparelho):
    #Construtor
    def __init__(self, marca, estado, volume):
        #Chama construtor da superclasse
        super().__init__(marca, estado)    
        self.__volume = volume
    
    def isEmQueVolume(self):
        return self.__volume
    
    #Métodos de instância
    def aumentaVolume(self):
        if self.__volume == True:
            print('O volume ja esta alto!')
        else:
            self.__volume = True
            print('O volume foi aumentado!')
    
    def abaixaVolume(self):
        if self.__volume == False:
            print('O volume ja esta baixo!')
        else:
            self.__volume = False
            print('O volume foi abaixado!')

    def mostraAtributos(self):
        print('A tv é da marca {}.'.format(self.getMarca()))
        if(self.isEmQueEstado()):
            print('A tv esta ligada.')
        else:
            print('A tv esta desligada.')
        if(self.isEmQueVolume()):
            print('O volume esta alto.')
        else:
            print('O volume esta baixo.')

class Celular(Aparelho):
    #Construtor
    def __init__(self, marca, estado, whatsappAberto):
        #Chama construtor da superclasse
        super().__init__(marca, estado)
        self.__whatsappAberto = whatsappAberto
    
    def isWhatsappAberto(self):
        return self.__whatsappAberto
    
    #Métodos de instância
    def abreWhatsapp(self):
        if self.__whatsappAberto == True:
            print('O whatsapp ja estava aberto! Tem varias pessoas no vácuo!')
        else:
            self.__whatsappAberto = True
            print('O whatsapp acaba de ser aberto. Há mensagens não lidas!')
    
    def fechaWhatsapp(self):
        if self.__whatsappAberto == False:
            print('O whatsapp ja estava fechado!')
        else:
            self.__whatsappAberto = False
            print('O whatsapp acaba de ser fechado!')
    
    def mostraAtributos(self):
        print('O celular é da marca {}.'.format(self.getMarca()))
        if(self.isEmQueEstado()):
            print('O celular esta ligado.')
        else:
            print('O celular esta desligado.')
        if(self.isWhatsappAberto()):
            print('O whatsapp esta aberto. Há mensagens não lidas!')
        else:
            print('O whatsapp esta fechado.')

T = Televisao('Philips', False, False)
T.mostraAtributos()
print("""---------------------
Tentando ligar a tv e aumentar seu volume:""")
T.ligaAparelho()
T.aumentaVolume()
print("""---------------------
Resultado após as mudanças:""")
T.mostraAtributos()
print("""---------------------
Tentando abaixar o volume da tv e depois desligá-la:""")
T.abaixaVolume()
T.desligaAparelho()
print("""---------------------
Resultado após as mudanças:""")
T.mostraAtributos()
print('-----------------------')
C = Celular('Moto G 6', True, True)
C.mostraAtributos()
print("""---------------------
Tentando ligar o celular e abrir seu whatsapp:""")
C.ligaAparelho()
C.abreWhatsapp()
print("""---------------------
Resultado após as mudanças:""")
C.mostraAtributos()
print("""---------------------
Tentando fechar o whatsappo do celular e depois desligá-lo:""")
C.fechaWhatsapp()
C.desligaAparelho()
print("""---------------------
Resultado após as mudanças:""")
C.mostraAtributos()