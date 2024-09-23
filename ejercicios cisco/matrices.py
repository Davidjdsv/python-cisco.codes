#EJERCICIO EJEMPLO #1
rows = int(input("Ingrese cantidad filas: "))
columns = int(input("Ingrese cantidad columnas: "))

matrix = []

for r_pos in range(rows):
    row = []
    for element in range(columns):
        row.append(int(input(f"Ingresando fila {r_pos+1}/{rows}. elemento {element+1}/{columns}: ")))
    matrix.append(row)

for m in matrix:
    print(m)