#Sempre que vamos criar uma exception nossa
#Customizada, no caso, temos que criar uma classe
#E dizer que ela é subclasse da classe exception
class ValorMenor(Exception):
    #Gerada quando o valor é menor
    pass

class ValorMaior(Exception):
    #Gerada quando o valor é maior
    pass

# número a ser descoberto
nro = 10

# usuário tenta adivinhar o número
while True:
    try:
        i_num = int(input("Tente acertar o número misterioso.\nDigite um número: "))
        if i_num < nro:
            #Raise chama a exception criada
            raise ValorMenor
        elif i_num > nro:
            raise ValorMaior
        break
    except ValorMenor:
        print("Valor menor, tente novamente!")
        print()
    except ValorMaior:
        print("Valor maior, tente novamente!")
        print()

print("Parabéns! Você descobriu o número.")