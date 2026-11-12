
# TEMA: CONJUNTOS (SET)

# Crear un conjunto con cinco elementos
estudiantes = {
    "Ana",
    "Luis",
    "Pedro",
    "Sofia",
    "Carlos"
}

print("Estudiantes:", estudiantes)

# Agregar un nuevo estudiante
estudiantes.add("Maria")

# Intentar agregar un elemento repetido
estudiantes.add("Ana")

# Mostrar el conjunto
print("Conjunto actualizado:", estudiantes)

# Consultar cantidad de elementos
print("Cantidad de estudiantes:", len(estudiantes))
