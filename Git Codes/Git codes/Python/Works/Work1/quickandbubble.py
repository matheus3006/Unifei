#Função de ordenação em Quick sort
def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        # Se o valor corrente é maior que o pivô, ele está no lugar certo, basta 
        # mover o ponteiro high à esquerda. Senão, ele está na posição errada e o laço deve
        # ser interrompido
        while low <= high and array[high] >= pivot:
            high = high - 1

        # Mesmo raciocício se aplica com low
        while low <= high and array[low] <= pivot:
            low = low + 1

        # Nesse ponto, ou achamos dois valores que precisam ser trocados, ou então
        # low > high e não há troca a fazer
        if low <= high:
            # Executando a troca
            array[low], array[high] = array[high], array[low]            
        else:
            # Saindo do loop
            break
        # Colocando o pivô na posição correta
        # (Todos à esquerda do pivô são menores e todas à direita são maiores)
    array[start], array[high] = array[high], array[start]

    return high

def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)

#Função de ordenação em Bubble sort
def bubble_sort(array): #Função que recebe o vetor como argumento
    elementos = len(array)-1 #Aloca espaço do tamanho do vetor - 1
    ordenado = False #Inicializa a variável ordenado como falso
    while not ordenado: #Enquanto não estiver ordenado, repita
        ordenado = True #Ordenado se torna verdadeiro
        for i in range(elementos): #Faça nos elementos
            if array[i] > array[i+1]: #Se um elemento for maior que o próximo
                array[i], array[i+1] = array[i+1],array[i] #Troca-os de posição
                ordenado = False #Ordenado se trona falso novamente
#Quando finalizar a ordenação, ordenado se torna verdadeiro, e retorna o vetor ordenado               
    return array 


#Criando um vetor e o preenchendo com números randômicos de 1 a 10000; Fazer uma cópia dele
from random import seed
from random import randint

seed(1)
vet = []
copy =[]
for i in range(10000):
    from random import randint
    i = randint(1,10000)
    vet.append(i)
    copy.append(i)
    
print('Vetor desordenado:')
print(vet)

#Usando as funções de ordenação passando o mesmo vetor; Fazendo a contagem de tempo
import timeit
import time

#Quick sort
print('\nOrdenando em quick sort')
inicio_quick = timeit.default_timer()
quick_sort(vet, 0, len(vet) - 1)
print(vet)
fim_quick = timeit.default_timer()

#Bubble sort
print('\nOrdenando em bubble sort')
inicio_bubble = timeit.default_timer()
bubble_sort(copy)
fim_bubble = timeit.default_timer()
print(copy)

#Exibindo o tempo de execução
print(f'Duracao do Quick Sort: {(fim_quick - inicio_quick) * 1000} milisegundos')
print(f'Duracao do Bubble Sort: {(fim_bubble - inicio_bubble) * 1000} milisegundos')
