def mdc(m, n):
    while m%n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm%oldn
    return n
#Exemplo:
#Se m = 2 e n = 4, temos:
#2 , 4
#2/4 -> resto da divisão é 2, porque 2 não divide 4
#oldm = 2
#oldn = 4
#m = 4
#n = 2
#Agora, com m = 4 e n = 2, temos:
#4 , 2
#4/2 -> resto da divisão é 0, parou o laço while
#return 2 -> valor do "n"

def mesmaFracao(f1, f2):
    return (f1.getNumerador() == f2.getNumerador()) and (f1.getDenominador() == f2.getDenominador())    
# Exemplo:
# Para f1 = 1/2 e f2 = 1/2:
# return 1 == 1 e 2 == 2

class Fracao:
    
    def __init__(self, numerador, denominador):
        self.__numerador = numerador        
        self.__denominador = denominador     

    def __str__(self):
        return str(self.__numerador) + "/" + str(self.__denominador)

    def getNumerador(self):
        return self.__numerador

    def getDenominador(self):
        return self.__denominador       

    def simplifica(self):
        divComum = mdc(self.__numerador, self.__denominador)
        self.__numerador = self.__numerador // divComum
        self.__denominador = self.__denominador // divComum 
    # Exemplo:
    # Para 2/4:
    # divComum = 2
    # self.__numerador = 2 // 2 -> self.__numerador = 1
    # self.__denominador = 4 // 2 -> self.__denominador = 2 

    def __add__(self,outraFrac):
        novonumerador = self.__numerador * outraFrac.getDenominador() + self.__denominador * outraFrac.getNumerador()
        novodenominador = self.__denominador * outraFrac.getDenominador()
        divComum = mdc(novonumerador, novodenominador)
        return Fracao(novonumerador//divComum, novodenominador//divComum)
               
    # Exemplo:
    # Para 2/4 + 1/2:
    # novonumerador = (2 * 2) + (4 * 1) = 8
    # novodenominador = 4 * 2 = 8
    # divComum = mdc(8, 8) -> divComum = 8
    # return Fracao(8 // 8, 8 // 8) -> return 1 e 1
    # Na hora de printar a fração, o resultado exibido será 1/1

frac1 = Fracao (1, 3)
frac2 = Fracao(2, 3)
frac3 = frac1 + frac2
print(frac3)