# Matriz bidimensional (3×3)
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Valor que estamos buscando
valor_buscado = 9

# Inicializar variables para rastrear la posición del valor
fila_e = -1
columna_e = -1

# Recorrer la matriz para buscar el valor
for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
        if matriz[fila][columna] == valor_buscado:
            fila_e = fila
            columna_e = columna
            break  # Detener la búsqueda una vez que se encuentra el valor
    if fila_e != -1:
        break  # Salir del bucle exterior si se encuentra el valor

# Verificar si se encontró el valor y mostrar la posición
if fila_e != -1:
    print(f"Se encontró {valor_buscado} en la fila {fila_e} y columna {columna_e}.")
else:
    print(f"{valor_buscado} no se encontró en la matriz.")