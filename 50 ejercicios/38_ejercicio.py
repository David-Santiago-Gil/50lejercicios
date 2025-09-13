# Generador de secuencia de números pares
cantidad = int(input("¿Cuántos números pares quieres generar?: "))

for i in range(cantidad):
  # El patrón para generar números pares es 2 * i
  numero_par = 2 * i
  print(numero_par)