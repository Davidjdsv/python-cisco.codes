import os

array = [99,10, 2, 88, 3, 1, 55, 33, 4]#guiense en base a este arreglo
aux = 0

#EJEMPLO 1
def bubble_sort1(arreglo):
    for i in range(0, len(arreglo)-1):
        for j in range(i+1, len(arreglo)):
            if arreglo[i] > arreglo[j]:
                aux = arreglo[i]
                arreglo[i] = arreglo[j]
                arreglo[j] = aux
    return arreglo

print(f"Bubble sort 1: {bubble_sort1(array)}")

input("Enter para mostrar la otra forma de ejecutar el bubble sort!")

#EJEMPLO 2
def bubble_sort2(arreglo):#Ordenamiento de menor a mayor
    for i in range(0, len(arreglo) -1):
        if arreglo[i] > arreglo[i + 1]:
            arreglo[i], arreglo[i+1] = arreglo[i+1], arreglo[i]
    return arreglo

print(f"Bubble sort 2: {bubble_sort2(array)}")

input("Enter para mostrar la otra forma de ejecutar el bubble sort!")

#EJEMPLO 3


def bubble_sort3(arreglo):
    cambio = True
    while cambio:
        cambio = False#No hay ningún cambio...
        for i in range(0, len(arreglo) -1):
            if arreglo[i] > arreglo[i+1]:#Comprueba si es verdadero, si si
                cambio = True#Se ejecuta la siguiente instrucción
                arreglo[i], arreglo[i+1] = arreglo[i+1], arreglo[i]
    return arreglo

print(f"Bubble sort 3: {bubble_sort3(array)}")

input("Ahora vamos con una lista interactiva!")

os.system("cls")

lista = []
ordenado = True
cant_num = int(input("Ingrese la cantidad de números que deseas agregar a la lista: "))

for i in range(cant_num):
    num = int(input(f"Números ingresados:{i}/{cant_num-1}: "))
    lista.append(num)

print(f"Lista desordenada: {lista}")

while ordenado:
    ordenado = False
    for i in range(0, len(lista) -1):
        if lista[i] > lista[i+1]:
            ordenado = True
            lista[i], lista[i+1] = lista[i+1], lista[i]

print(f"Lista ordendada: {lista}")