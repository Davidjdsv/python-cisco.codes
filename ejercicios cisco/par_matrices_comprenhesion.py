def es_par(num):
    return num % 2 == 0

pares = []
impares = []
acum = 0
filas = int(input("Cantidad de listas(filas) en la matrix: "))
columnas = int(input("Cantidad elementos por fila en la matrix: "))

matrix = [
    [
        int(input(f"Fila {f_pos+1}/{filas}. Elemento {element+1}/{columnas}: "))
        for element in range(columnas)
    ]
    for f_pos in range(filas)
]#Para el list comprenhension es mejor hacerlo de derecha a izquierda

for fila in matrix:
    for num in fila:
        acum += num
        #pares.append(num) if num % 2 == 0 else impares.append(num)
        pares.append(num) if es_par(num) else impares.append(num)

print()

for m in matrix:
    print(m)

print()

print(f"Pares en la matrix: {pares}")
print(f"Impares en la matrix: {impares}")
print(f"Suma total de los elementos de la matrix: {acum}")