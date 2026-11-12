
# TEMA: LISTAS ENLAZADAS

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

# Crear cinco nodos
nodo1 = Nodo("Cancion 1")
nodo2 = Nodo("Cancion 2")
nodo3 = Nodo("Cancion 3")
nodo4 = Nodo("Cancion 4")
nodo5 = Nodo("Cancion 5")

# Conectar los nodos
nodo1.siguiente = nodo2
nodo2.siguiente = nodo3
nodo3.siguiente = nodo4
nodo4.siguiente = nodo5

# Recorrer la lista
actual = nodo1

while actual is not None:
    print(actual.dato)
    actual = actual.siguiente
