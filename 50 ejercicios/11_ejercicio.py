# Las 10 marcas de autos más populares (basado en datos de ventas globales)
marcas_de_auto = [
    "Toyota",
    "Volkswagen",
    "Hyundai",
    "Honda",
    "Ford",
    "Nissan",
    "Mercedes-Benz",
    "BMW",
    "Chevrolet",
    "Kia"
]

# Inicializamos el contador en 0 para acceder a los índices de la lista
contador = 0

print("Las 10 marcas de autos más vendidas en el mundo son:")

# El bucle se ejecutará mientras el contador sea menor que la longitud de la lista
while contador < len(marcas_de_auto):
    print(f"{contador + 1}. {marcas_de_auto[contador]}")
    # Incrementamos el contador para pasar a la siguiente marca
    contador = contador + 1