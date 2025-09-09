# Juego de adivinanza con entrada de usuario
import random

numero_secreto = random.randint(1, 10)
intentos = 0
adivinado = False

print("¡Adivina el número secreto! Está entre 1 y 10.")

while not adivinado:
  try:
    adivinanza_usuario = int(input("Ingresa tu adivinanza: "))
    intentos += 1

    if adivinanza_usuario == numero_secreto:
      print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
      adivinado = True
    elif adivinanza_usuario < numero_secreto:
      print("El número es más grande.")
    else:
      print("El número es más pequeño.")
  except ValueError:
    print("Entrada inválida. Por favor ingresa un número.")