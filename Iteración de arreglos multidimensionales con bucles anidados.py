import random

# Definir dimensiones
ciudades = ['Ciudad A', 'Ciudad B', 'Ciudad C']
dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
semanas = 4

# Crear la matriz 3D: temperaturas[ciudad][semana][día]
temperaturas = []

# Generar datos aleatorios
for ciudad in ciudades:
    ciudad_data = []
    for semana in range(semanas):
        semana_data = []
        for dia in dias:
            temp = random.randint(15, 35)
            semana_data.append(temp)
        ciudad_data.append(semana_data)
    temperaturas.append(ciudad_data)

# Calcular el promedio de temperaturas por ciudad y semana
print("Promedio de temperaturas semanales por ciudad:\n")

for i, ciudad in enumerate(ciudades):
    print(f"--- {ciudad} ---")
    for semana in range(semanas):
        suma = 0
        for dia in range(len(dias)):
            suma += temperaturas[i][semana][dia]
        promedio = suma / len(dias)
        print(f"Semana {semana + 1}: {promedio:.2f}°C")
    print()
