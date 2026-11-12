
# TEMA: TABLAS HASH / MAPAS

# Diccionario de productos y precios
productos = {
    "Arroz": 3000,
    "Leche": 4500,
    "Pan": 2000,
    "Huevos": 12000,
    "Azucar": 3500
}

# Mostrar los cinco productos
for producto, precio in productos.items():
    print(producto, ":", precio)

# Buscar un producto mediante su clave
print("Precio del arroz:", productos["Arroz"])
