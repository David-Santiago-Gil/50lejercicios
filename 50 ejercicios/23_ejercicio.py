# Invertir una lista creando una nueva
colores = ["rojo", "verde", "azul", "amarillo", "blanco"]
print(f"La lista original es: {colores}")

# Creamos una lista vacía para guardar los elementos en el orden inverso
colores_invertidos = []
# Iteramos sobre la lista original, pero en reversa
for i in range(len(colores) - 1, -1, -1):
  # Agregamos cada elemento de la lista original a la nueva lista
  colores_invertidos.append(colores[i])

print(f"La lista invertida es: {colores_invertidos}")