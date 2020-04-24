#Implemente uma função que receba uma lista de inteiros e
#ordena essa lista utilizando o Bubble Sort

def bubble_sort(array): #Função que recebe o vetor como argumento
    elementos = len(array)-1 #Aloca espaço do tamanho do vetor - 1
    ordenado = False #Inicializa a variável ordenado como falso
    while not ordenado: #Enquanto não estiver ordenado, repita
        ordenado = True #Ordenado se torna verdadeiro
        for i in range(elementos): #Faça nos elementos
            if array[i] > array[i+1]: #Se um elemento for maior que o próximo
                array[i], array[i+1] = array[i+1],array[i] #Troca_os de posição
                ordenado = False #Ordenado se trona falso novamente
#Quando finalizar a ordenação, ordenado se torna verdadeiro, e retorna o vetor ordenado               
    return array 
#Criando e preenchendo o vetor com valores aleatórios entre 0 e 10000
vet = []
for i in range(10000):
    from random import randint
    i=randint(1,10000)
    vet.append(i)
print('Este é o vetor desordenado:')
print(vet)

print('Ordenando em bubble sort...')
#Calculando e printando o tempo de execução
import time
inicio_bubble = time.time()
#Chamando a função bubble_sort e passando o vetor como parâmetro
bubble_sort(vet)
#Printando o vetor ordenado na tela
print(vet)

fim_bubble = time.time()
print(f'Duracao do Bubble Sort: {(fim_bubble - inicio_bubble) * 1000} milisegundos')