# Juego de adivinanza de palabra
palabra_secreta = "python"
intentos_restantes = 3

print("¡Bienvenido al juego de adivina la palabra!")
print("Tienes 3 intentos para adivinar la palabra secreta.")

while intentos_restantes > 0:
  adivinanza = input(f"\nIntento {4 - intentos_restantes}: ").lower()
  if adivinanza == palabra_secreta:
    print("¡Felicidades! Adivinaste la palabra.")
    break
  else:
    intentos_restantes -= 1
    if intentos_restantes > 0:
      print(f"Incorrecto. Te quedan {intentos_restantes} intentos.")
    else:
      print(f"Lo siento, perdiste. La palabra era '{palabra_secreta}'.")