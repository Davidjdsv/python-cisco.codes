array = [22, 33, 11, 222, 45, 90, 99, 777, -1, 0, -96, 53]

def ordenar_pivote(arr):
    if len(arr) <= 1:
        return arr
    
    pivote = arr[len(arr) // 2]
    izq = [x for x in arr if x < pivote]
    centro = [x for x in arr if x == pivote]
    der = [x for x in arr if x > pivote]
    
    return ordenar_pivote(izq) + ordenar_pivote(centro) + ordenar_pivote(der)

print(array)
print(ordenar_pivote(array))
print("Esta vaina funciona")