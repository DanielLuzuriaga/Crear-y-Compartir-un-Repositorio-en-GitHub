# ----------------------------------------
# Escritura en un archivo de texto
# ----------------------------------------

# Abre el archivo en modo escritura ('w') y lo crea si no existe
archivo = open("my_notes.txt", "w")

# Escribe tres líneas de notas personales
archivo.write("Nota 1: Mi nombre es Daniel Luzuriaga.\n")
archivo.write("Nota 2: Soy estudiante de la Universidad Estatal Amazónica.\n")
archivo.write("Nota 3: Estoy siguiendo la carrera de Tecnologías de la Información.\n")

# Cierra el archivo después de escribir
archivo.close()


# ----------------------------------------
# Lectura del archivo línea por línea
# ----------------------------------------

# Abre el archivo en modo lectura ('r')
archivo = open("my_notes.txt", "r")

# Lee y muestra cada línea usando readline()
print("Contenido del archivo:")
linea = archivo.readline()  # Lee la primera línea

while linea:
    print(linea.strip())  # Imprime la línea sin salto de línea extra
    linea = archivo.readline()  # Lee la siguiente línea

# Cierra el archivo después de leer
archivo.close()
