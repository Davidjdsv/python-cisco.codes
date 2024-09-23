numbers = [1, 3, 4, 23, 55]
print(f"Lista: {numbers}")

numbers[0] = 111
print(f"Lista actualizada: {numbers}")

numbers[1] = numbers[4]
print(f"Lista actualizada: {numbers}")

print(f"Longitud de la lista: {len(numbers)}")
del numbers[1]
print(numbers[-4])

#
my_list = [2, 3, 7, 8, 20, 30]
total = 0

print("Sumando los elementos de una lista ")
for i in range(len(my_list)):
    total += my_list[i]
print(total)

void_list = []
for i in range(0, 10):
    void_list.insert(i, 0)
print(void_list)

print("Otra lista: ")
lst = [1, 2, 3, 4, 5]
lst_2 = []
add = 0
for number in lst:
    add += number
    lst_2.append(add)

print(lst_2)
