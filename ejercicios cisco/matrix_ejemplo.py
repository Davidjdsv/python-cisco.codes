matriz = [
    [1, 2, 3], 
    [4, 5, 6],
    [7, 8, 9]
]
print("Imprimiendo la matriz como si fuera un arreglo")

print(matriz)
print()

for arreglo in matriz:
    print(arreglo)

print()
print("Recorriendo cada arreglo dentro de la matriz")
print()
for arreglo in matriz:
    for elemento in arreglo:
        print(elemento)
    print()

print("Recorriendo cada elemento de cada arreglo individualmente")