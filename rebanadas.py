import os
def limpiar():
    input(f"Enter para continuar con el siguiente ejemplo.")
    return os.system("cls")

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)#salida: [8, 6, 4]
#Sintaxis de la rebanada lista[start:end]. Toma el valor de inicio y el final -1

limpiar()

print(my_list)
new_list = my_list[0:]
print(f"Nueva lista iterando for each [0:] lo mismo que len(new_list): {new_list}")

limpiar()

# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[:] Crea una copia de my_list
# print(new_list)

print("PARA ELIMINAR ELEMENTOS DE LA LISTA EN REBANADAS, SE PUEDE USAR DEL + NOMBRE_LISTA[START:END]. NO PRODUCE LISTA NUEVA")
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)

limpiar()

print("Operador in, not in: ")

my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)

limpiar()
print("Uso de in: ")

numeros = [99, 2, 5, 32, 456, 3, 6, 77, 777]
largest = numeros[0]

for i in numeros:#i recorre numeros
    if i > largest:
        largest = i
print(f"Número mayor en el arreglo con in: {largest}")

limpiar()

print("Encontrando un elemento dentro de la lista: ")
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print(f"Está en la posición: {i} de la lista")
else:
    print("No está en la lista")

