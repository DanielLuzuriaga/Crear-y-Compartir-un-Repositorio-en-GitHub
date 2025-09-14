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

# Mostrar promedio semanal por ciudad
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

# Función para calcular el promedio total por ciudad
def calcular_promedio_ciudades(temperaturas, ciudades):
    """
    Calcula el promedio total de temperatura por ciudad.

    Parámetros:
    - temperaturas (list): matriz 3D [ciudad][semana][día] con temperaturas.
    - ciudades (list): lista con los nombres de las ciudades.

    Retorna:
    - dict: diccionario con el nombre de la ciudad como clave y su promedio como valor.
    """
    promedios_por_ciudad = {}

    for i, ciudad in enumerate(ciudades):
        suma = 0
        cantidad_datos = 0
        for semana in temperaturas[i]:
            for temp in semana:
                suma += temp
                cantidad_datos += 1
        promedio = suma / cantidad_datos if cantidad_datos else 0
        promedios_por_ciudad[ciudad] = promedio

    return promedios_por_ciudad

# Calcular y mostrar el promedio total por ciudad
promedios = calcular_promedio_ciudades(temperaturas, ciudades)

print("Promedio total de temperaturas por ciudad:\n")
for ciudad, promedio in promedios.items():
    print(f"{ciudad}: {promedio:.2f}°C")


