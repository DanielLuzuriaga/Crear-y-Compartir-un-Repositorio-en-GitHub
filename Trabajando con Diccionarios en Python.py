# Crear un Diccionario
informacion_personal = {
    "nombre": "Daniel Luzuriaga",
    "edad": 43,
    "ciudad": "Cuenca",
    "profesion": "Tecnólogo"
}

# Acceder y Modificar el valor de la clave "ciudad"
informacion_personal["ciudad"] = "Quito"

# Agregar una nueva clave-valor para "profesion" (ya existe, pero se puede actualizar)
informacion_personal["profesion"] = "Ingeniero en Sistemas"

# Verificar si la clave "telefono" existe; si no, agregarla
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0987703700"

# Eliminar la clave "edad"
informacion_personal.pop("edad", None)

# Imprimir el diccionario final
print(informacion_personal)
