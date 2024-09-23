def es_par(num):
    return num % 2 == 0#Si es par, retornará verdadero, sino, retornará falso.

matrix = []
pares = []
impares = []
acum = 0

listas = int(input("Ingrese la cantidad de listas en la matrix: "))
elementos = int(input("Ingrese la cantidad de elementos en cada lista: "))

for lista in range(listas):
    fila = []#La fila se crea acá porque nacerá cada fila nueva después de cada fin de iteración
    for elemento in range(elementos):
        num = int(input(f"Lista: {lista+1}/{listas}, Elemento: {elemento+1}/{elementos}: "))
        fila.append(num)
        pares.append(num) if es_par(num) else impares.append(num)#opeador ternario
        #El operador ternario es condición verdadera izquierda, condición falsa derecha
    matrix.append(fila)

print("La matrix: ")
for m in matrix:
    print(m)

print()
print(f"Los números pares {pares}")
print(f"Los números impares {impares}")
print(f"Suma total de elemenos ingresados: {acum}")