# Creando una lista de la compra de una forma más ágil
entrada_usuario = input("Ingresa los artículos de la lista, separados por comas: ")
lista_de_articulos = [item.strip() for item in entrada_usuario.split(',')]

print("Tu lista de la compra incluye:")
for item in lista_de_articulos:
  print(f"- {item}")