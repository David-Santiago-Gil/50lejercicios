# Calculadora de Promedio Ponderado
def calcular_promedio_ponderado():
    try:
        num_materias = int(input("¿Cuántas materias vas a ingresar?: "))
        if num_materias <= 0:
            print("Número de materias no válido.")
            return

        suma_ponderada = 0
        suma_pesos = 0

        for i in range(num_materias):
            calificacion = float(input(f"Ingresa la calificación de la materia #{i + 1}: "))
            peso = float(input(f"Ingresa el peso (créditos) de la materia #{i + 1}: "))
            
            suma_ponderada += calificacion * peso
            suma_pesos += peso

        if suma_pesos == 0:
            print("No se puede calcular el promedio sin pesos.")
            return
        
        promedio = suma_ponderada / suma_pesos
        print(f"\nEl promedio ponderado es: {promedio:.2f}")

    except ValueError:
        print("Entrada no válida. Por favor, ingresa solo números.")

calcular_promedio_ponderado()