
# TEMA: ARBOLES

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None

# Crear cinco nodos
raiz = Nodo("Empresa")
raiz.izquierdo = Nodo("Administracion")
raiz.derecho = Nodo("Ventas")

raiz.izquierdo.izquierdo = Nodo("Contabilidad")
raiz.izquierdo.derecho = Nodo("Recursos Humanos")

# Mostrar los cinco nodos
print("Raiz:", raiz.dato)
print("Hijo izquierdo:", raiz.izquierdo.dato)
print("Hijo derecho:", raiz.derecho.dato)
print("Otro nodo:", raiz.izquierdo.izquierdo.dato)
print("Otro nodo:", raiz.izquierdo.derecho.dato)
