matrix = []
pares = []
impares = []
acum = 0
filas = int(input("Cantidad filas en la matrix: "))
elementos = int(input("Cantidad elementos por fila en la matrix: "))

for f_pos in range(filas):
    fila = []#Se declara acá porque es una nueva lista en cada iteración de f_pos
    for element in range(elementos):
        num = int(input(f"Fila: {f_pos+1}/{filas}. Elemento {element+1}/{elementos}: "))
        fila.append(num)
        acum += num
        pares.append(num) if num % 2 == 0 else impares.append(num)
    matrix.append(fila)

print()

for m in matrix:
    print(m)

print()

print(f"Pares en la matrix: {pares}")
print(f"Impares en la matrix: {impares}")
print(f"Suma total de los elementos de la matrix: {acum}")