# imprime o número recíproco apenas de números pares

try:
    num = int(input("Digite um número: "))
    #Assert serve para garantir que uma exigência ou condição seja atendida
    #Caso não for, gera uma exceção
    assert num % 2 == 0
except:
    print("Não é um número par!")
else:
    reciproco = 1/num
    print(reciproco)