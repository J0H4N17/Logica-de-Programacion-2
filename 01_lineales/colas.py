
# TEMA: COLAS (QUEUE)
# Funcionamiento: FIFO

from collections import deque

cola = deque()

# Ejemplo 1: Primer cliente
cola.append("Cliente 1")

# Ejemplo 2: Segundo cliente
cola.append("Cliente 2")

# Ejemplo 3: Tercer cliente
cola.append("Cliente 3")

# Ejemplo 4: Cuarto cliente
cola.append("Cliente 4")

# Ejemplo 5: Quinto cliente
cola.append("Cliente 5")

print("Cola completa:", list(cola))

# Atender al primer cliente
print("Cliente atendido:", cola.popleft())

print("Cola actual:", list(cola))
