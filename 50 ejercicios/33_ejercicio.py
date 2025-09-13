def contar_frecuencia_numeros(lista_numeros):
    """
    Cuenta la frecuencia de cada número en la lista.
    Retorna un diccionario con el número y su frecuencia.
    """
    frecuencias = {}
    print("--- Proceso de conteo de números ---")
    
    for numero in lista_numeros:
        if numero in frecuencias:
            frecuencias[numero] += 1
            print(f"  > El número '{numero}' encontrado de nuevo. Frecuencia: {frecuencias[numero]}")
        else:
            frecuencias[numero] = 1
            print(f"  > Nuevo número encontrado: '{numero}'")
            
    return frecuencias

def mostrar_reporte_frecuencias(frecuencias):
    """
    Muestra un reporte detallado de la frecuencia de los números.
    """
    if not frecuencias:
        print("La lista está vacía o no contiene números.")
        return
        
    print("\n" + "=" * 40)
    print("REPORTE DE FRECUENCIA DE NÚMEROS")
    print("=" * 40)
    
    # Ordenar los números por su frecuencia, de mayor a menor
    frecuencias_ordenadas = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)
    
    for numero, frecuencia in frecuencias_ordenadas:
        print(f" - Número '{numero}': {frecuencia} veces")
    
    print("-" * 40)

def analizar_datos_completos(datos):
    """Realiza un análisis completo de los datos numéricos."""
    print("ANÁLISIS DE DATOS NUMÉRICOS")
    print("=" * 30)
    
    print(f"\nDatos de entrada: {datos}")
    
    # 1. Contar la frecuencia de los números
    frecuencias = contar_frecuencia_numeros(datos)
    
    # 2. Mostrar el reporte de frecuencias
    mostrar_reporte_frecuencias(frecuencias)

# --- Uso del programa ---
# Ejemplo de datos: resultados de una encuesta
resultados_encuesta = [5, 4, 3, 5, 2, 1, 5, 4, 3, 5, 5, 2]

analizar_datos_completos(resultados_encuesta)