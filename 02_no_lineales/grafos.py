
# TEMA: GRAFOS

# Representacion mediante listas de adyacencia
grafo = {
    "Ana": ["Luis", "Pedro"],
    "Luis": ["Ana", "Carlos"],
    "Pedro": ["Ana", "Sofia"],
    "Carlos": ["Luis"],
    "Sofia": ["Pedro"]
}

# Mostrar las conexiones de cinco usuarios
for usuario, conexiones in grafo.items():
    print(usuario, "esta conectado con:", conexiones)
