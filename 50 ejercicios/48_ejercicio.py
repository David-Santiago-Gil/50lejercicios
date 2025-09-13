# Generador de Tablas de Multiplicar
try:
    numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))
    
    print(f"\n--- Tabla del {numero} ---")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

except ValueError:
    print("Entrada no válida. Por favor, ingresa un número entero.")