personal_data = {
    "Nombre": "jhoan",
    "edad": 25,
    "Documento": 1116281626,
    "Ocupación": "Desarrollador"
}

personal_data1 = {
    "Nombre": "Priscilla",
    "edad": 24,
    "Documento": 1116324546,
    "Ocupación": "Desarrolladora"
}

for key in personal_data.keys():
    print(f"{key} -> {personal_data[key]}")

print()

for key,value in personal_data1.items():
    print(f"{key} -> {value}")


