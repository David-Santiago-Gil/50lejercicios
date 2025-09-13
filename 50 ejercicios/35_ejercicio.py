def ordenar_productos_por_precio(diccionario_productos):
    """
    Ordena un diccionario de productos basado en el precio.
    Retorna una lista de tuplas (producto, precio) ordenada de menor a mayor.
    """
    print("--- Proceso de ordenamiento por precio ---")
    
    # Se utiliza la función sorted() con una expresión lambda para ordenar por el valor
    productos_ordenados = sorted(diccionario_productos.items(), key=lambda item: item[1])
    
    for producto, precio in productos_ordenados:
        print(f"  > '{producto}' con precio ${precio:.2f}")

    return productos_ordenados

def mostrar_reporte_productos(productos_ordenados):
    """
    Muestra un reporte detallado de los productos ordenados.
    """
    print("\n" + "=" * 40)
    print("REPORTE DE PRODUCTOS ORDENADOS")
    print("=" * 40)
    
    print("Productos ordenados por precio (de menor a mayor):")
    for producto, precio in productos_ordenados:
        print(f" - {producto}: ${precio:.2f}")
    
    print("-" * 40)

def analizar_inventario_completo(inventario):
    """Realiza un análisis completo del inventario de productos."""
    print("ANÁLISIS DE INVENTARIO")
    print("=" * 30)
    
    print(f"\nDatos de inventario de entrada: {inventario}")
    
    # 1. Ordenar los productos por precio
    productos_ordenados = ordenar_productos_por_precio(inventario)
    
    # 2. Mostrar el reporte final
    mostrar_reporte_productos(productos_ordenados)

# --- Uso del programa ---
# Ejemplo de datos: un inventario de tienda
inventario_tienda = {
    "Audífonos": 55.00,
    "Mouse gaming": 35.50,
    "Teclado mecánico": 99.99,
    "Monitor 24''": 150.00,
    "Webcam HD": 25.75
}

analizar_inventario_completo(inventario_tienda)