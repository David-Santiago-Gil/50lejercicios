import random

# Simulador de Lanzamiento de Dados
def simular_lanzamientos(num_lanzamientos):
    resultados = {}
    
    # Inicializar el diccionario de resultados
    for i in range(2, 13):
        resultados[i] = 0

    for _ in range(num_lanzamientos):
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        suma = dado1 + dado2
        resultados[suma] += 1
    
    return resultados

# Pedir al usuario cuántos lanzamientos quiere
try:
    num_lanzamientos = int(input("¿Cuántas veces quieres lanzar los dados?: "))
    if num_lanzamientos > 0:
        frecuencias = simular_lanzamientos(num_lanzamientos)
        print("\n--- Frecuencia de los resultados ---")
        for suma, frecuencia in sorted(frecuencias.items()):
            print(f"Suma {suma}: {frecuencia} veces")
    else:
        print("Por favor, ingresa un número positivo.")
except ValueError:
    print("Entrada no válida. Por favor, ingresa un número entero.")