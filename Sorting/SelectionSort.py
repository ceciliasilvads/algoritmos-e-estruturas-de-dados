def selectionSort(lista):
    for j in range(len(lista)-1):
        min_index = j
        for i in range(j, len(lista)):
            if lista[i] < lista[min_index]:
                min_index = i

        if lista[j] > lista[min_index]:
            aux = lista[j]
            lista[j] = lista[min_index]
            lista[min_index] = aux
    print(lista)

if __name__ == '__main__':
    selectionSort([5,2, 3,6,3])