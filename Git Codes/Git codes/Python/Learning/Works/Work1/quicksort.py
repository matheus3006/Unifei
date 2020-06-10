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


array = [29,99,27,41,66,28,44,78,87,19,31,76,58,88,83,97,12,21,44]
print(array)
quick_sort(array, 0, len(array) - 1)
print(array)