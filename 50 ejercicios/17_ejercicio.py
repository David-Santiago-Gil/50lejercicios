# Búsqueda de un elemento en una lista con el operador 'in'
frutas = ["manzana", "banana", "uva", "fresa"]
fruta_buscada = input("¿Qué fruta buscas? ").lower()

if fruta_buscada in frutas:
  print(f"¡Sí, tenemos {fruta_buscada}!")
else:
  print(f"Lo siento, no tenemos {fruta_buscada}.")