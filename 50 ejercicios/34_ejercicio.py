def calcular_promedio_ventas(diccionario_ventas):
    """
    Calcula el promedio de las ventas de un diccionario.
    Retorna el promedio, la suma total y el número de elementos.
    """
    suma_total = 0
    cantidad_elementos = 0
    print("--- Proceso de cálculo de promedio ---")
    
    for producto, venta in diccionario_ventas.items():
        suma_total += venta
        cantidad_elementos += 1
        print(f"  > Sumando '{producto}' con venta de {venta}. Suma parcial: {suma_total}")
        
    if cantidad_elementos == 0:
        return 0, 0, 0
    
    promedio = suma_total / cantidad_elementos
    return promedio, suma_total, cantidad_elementos

def mostrar_reporte_ventas(promedio, suma, cantidad):
    """
    Muestra un reporte detallado del cálculo de ventas.
    """
    print("\n" + "=" * 40)
    print("REPORTE DE VENTAS PROMEDIO")
    print("=" * 40)
    
    print(f"Total de productos analizados: {cantidad}")
    print(f"Suma total de ventas: {suma}")
    print(f"Promedio de ventas: {promedio:.2f}")
    
    print("-" * 40)

def analizar_ventas_completas(datos_ventas):
    """Realiza un análisis completo de los datos de ventas."""
    print("ANÁLISIS DE DATOS DE VENTAS")
    print("=" * 30)
    
    print(f"\nDatos de entrada: {datos_ventas}")
    
    # 1. Calcular el promedio de las ventas
    promedio, suma_total, cantidad = calcular_promedio_ventas(datos_ventas)
    
    # 2. Mostrar el reporte final
    mostrar_reporte_ventas(promedio, suma_total, cantidad)

# --- Uso del programa ---
# Ejemplo de datos: ventas mensuales de diferentes productos
ventas_mensuales = {
    "Laptop": 1250,
    "Mouse": 150,
    "Teclado": 80,
    "Monitor": 450,
    "Webcam": 75
}

analizar_ventas_completas(ventas_mensuales)
