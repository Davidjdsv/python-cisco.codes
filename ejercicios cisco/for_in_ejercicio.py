import random
print("Loteria! Apuesta 5 números. Elige números 5 entre el 1 hasta el 20 para poder ganar premios espectaculares!")
loteria = []
participante = []
aciertos = 0

#Se agregar los números al azar de la loteria y el usuario ingresa sus números a apostar
for i in range(0, 5):
    while True:
        try:
            num = int(input(f"Número {i+1}/5: "))
            if num > 20 or num < 1:
                print("Ingrese números dentro del (rango 1-20)")
                continue
            else:
                participante.append(num)
                loteria.append(random.randint(1, 20))
            break
        except ValueError:
            print("Ingrese solo números...")

#Se buscan las coincidencias entre la loteria y el usuario
for i in loteria:#I recorre el arreglo de la loteria
    if i in participante:#A su vez, i compara con los números del participante y añade 1 acierto al cont
        aciertos+=1

print(f"Números loteria: {loteria}")
print(f"Números participante: {participante}")
print(f"Acciertos: {aciertos}")

num1 = int(input("Ingrese num1: "))
num2 = int(input("Ingrese num2: "))
res = num1 + num2

print(res)
