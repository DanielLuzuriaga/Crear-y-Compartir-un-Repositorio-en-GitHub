def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]
    return fila

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

# Matriz bidimensional (3×3)
matriz = [
    [4, 7, 2],
    [1, 9, 6],
    [8, 3, 5]
]

print("Matriz original:")
imprimir_matriz(matriz)

# Fila que se desea ordenar (por índice: 0, 1 o 2)
indice_fila = 0

# Ordenar la fila específica
matriz[indice_fila] = bubble_sort(matriz[indice_fila])

print(f"\nMatriz después de ordenar la fila {indice_fila}:")
imprimir_matriz(matriz)