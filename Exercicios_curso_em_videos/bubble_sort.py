import random

def bubble_sort(lista):
    n = len(lista)
    for j in range(n-1):
        for i in range(n-1):
            if lista[i] > lista[i+1]:
                #troca de elementos nas posições i e i+1
                lista[i], lista[i+1] = lista[i+1], lista[i]
                
                '''
                usando var auxiliar
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
                '''


#Números aleatórios escolhido pelo sistema
any_numbers = random.sample(range(1, 61), 6)

already_sorted = [1, 2, 3, 4, 5, 6, 9, 20, 22, 23, 28,
                  32, 34, 39, 40, 42, 76, 87, 99, 112]

inversed = [117, 90, 88, 83, 81, 77, 74, 69, 64, 63, 51, 
            50, 49, 42, 41, 34, 32, 29, 28, 22, 15, 8, 6, 5, 3, 1]

repeated =[7, 7, 7, 7, 7, 1, 1, 9, 9, 0, 4, 4, 4, 5, 4, 5, 7, 1]

lista = [16,25,2,8,50,40]

'''
#Comando para a lista já sair ordenada:
lista = sorted(lista)
'''
print('\nAntes de ordenar:')
print(lista)

#aplicando a função
bubble_sort(lista)

print('\nOrdenado:')
print(lista)