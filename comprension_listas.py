import random
#Primer ejemplo
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares_cuadrado = [num ** 2 for num in numeros if num % 2 == 0]

#SINTAXIS: newlist = [expression for item in iterable if condition]

#num ** 2: EXPRESIÓN: ELEVA EL NÚMERO PAR AL CUADRADO
#for num un numeros: ITERA SOBRE CADA ELEMENTO DEL ARREGLO
#if num % 2 == 0: SI ES PAR, HACE LA PRIMERA INSTRUCCIÓN Y LO GUARDA EN PARES_CUADRADOS

#print(f"Los pares al cuadrado: {pares_cuadrado}")

animales = ["oso", "narval", "ornitorrinco", "gato", "vaca", "perro", "pez", "mono"]
animales_letras = [i for i in animales if len(i) > 4]
#print(animales_letras)

#ARREGLOS BIDIMENSIONALES

tablero = []
EMPTY = ""

#PRIMERA FORMA COMPRENSIÓN DE LISTAS
# for i in range(8):
#     casilla1 = [EMPTY for i in range(8)]

#SEGUNDA FORMA MAS CORTA
casilla = [[EMPTY for i in range(8)] for j in range(8)]
tablero.append(casilla)

casilla[0][0] = "TORRE"
casilla[0][7] = "TORRE"
casilla[7][0] = "TORRE"
casilla[7][7] = "TORRE"

casilla[0][1] = "CABALLO"
casilla[0][6] = "CABALLO"
casilla[7][1] = "CABALLO"
casilla[7][6] = "CABALLO"
#print(f"Tablero ajedrez: \n{tablero}")

#CON OPERADOR TERNARIO EN LA MATRIZ
casillas = [["😎" if i % 2 == 0 else "😍" for i in range(4)] for _ in range(4)]
print(casillas)

#EJEMPLO 2 DE ARRAYS CON TERMOMETRO
temps = [[round(random.uniform(0, 50), 1) for h in range(24)] for d in range(31)]
#print(temps)

#Temperatura mas alta:
t_alta = -100
for day in temps:#recorre cada día
    for temp in day:#recorre cada hora del día
        if temp > t_alta:
            t_alta = temp
#print(f"Temperatura mas alta del mes: {t_alta:.1f}")
nums = [1, 2, 3]
vals = nums[-1:-2]
# print(nums)
# print(vals)
my_list = [3, 1, -2]
#print(my_list[my_list[-1]])










