import random

# Juego de Adivinanza de Número
def juego_adivinanza():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    
    print("¡Bienvenido al juego de adivina el número!")
    print("Estoy pensando en un número entre 1 y 100.")
    
    while True:
        try:
            adivinanza = int(input("\nIngresa tu adivinanza: "))
            intentos += 1
            
            if adivinanza < numero_secreto:
                print("El número que busco es más alto. ¡Intenta de nuevo!")
            elif adivinanza > numero_secreto:
                print("El número que busco es más bajo. ¡Intenta de nuevo!")
            else:
                print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
                break
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número.")

juego_adivinanza()