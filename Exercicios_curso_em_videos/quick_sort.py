import random

def quicksort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)-1
    if inicio < fim:
        p = partition(lista, inicio, fim)
        quicksort(lista, inicio, p-1)
        quicksort(lista, p+1, fim)
        
def partition(lista, inicio, fim):
    pivot = lista[fim]
    i = inicio
    for j in range(inicio, fim):
        if lista[j] <= pivot:
            lista[j], lista[i] = lista[i], lista[j]
            i = i + 1

    lista[i], lista[fim] = lista[fim], lista[i]
    return i       

#Números aleatórios escolhido pelo sistema
any_numbers = random.sample(range(1, 1000), 40)

already_sorted = [1, 2, 3, 4, 5, 6, 9, 20, 22, 23, 28,
                  32, 34, 39, 40, 42, 76, 87, 99, 112]

inversed = [117, 90, 88, 83, 81, 77, 74, 69, 64, 63, 51, 
            50, 49, 42, 41, 34, 32, 29, 28, 22, 15, 8, 6, 5, 3, 1]

repeated =[7, 7, 7, 7, 7, 1, 1, 9, 9, 0, 4, 4, 4, 5, 4, 5, 7, 1]

lista = inversed

print(lista)

#aplicando a função
quicksort(lista)

print('\nOrdenado:')
print(lista)