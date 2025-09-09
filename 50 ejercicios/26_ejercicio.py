def encontrar_elementos_comunes(lista1, lista2):
  """
  Busca elementos comunes entre dos listas de forma manual
  y muestra el proceso paso a paso.
  """
  elementos_comunes = [] # Almacena los elementos encontrados
  comparaciones = 0
  coincidencias = 0

  print(f"Lista 1: {lista1}")
  print(f"Lista 2: {lista2}")
  print("\n--- INICIANDO BÚSQUEDA DE ELEMENTOS COMUNES ---")

  # Bucle externo: recorre la primera lista
  for i, elemento1 in enumerate(lista1):
    print(f"\nVerificando el elemento '{elemento1}' de la Lista 1...")
    
    # Bucle interno: compara el elemento de la primera lista con todos los de la segunda
    for j, elemento2 in enumerate(lista2):
      comparaciones += 1
      print(f"  Comparando '{elemento1}' con '{elemento2}'")

      # Si el elemento de la lista 1 es igual al de la lista 2
      if elemento1 == elemento2:
        # Verificamos si ya fue agregado para evitar duplicados en el resultado final
        if elemento1 not in elementos_comunes:
          elementos_comunes.append(elemento1)
          coincidencias += 1
          print(f"  ✓ ¡Coincidencia encontrada! '{elemento1}'")
        else:
          # Esto ocurre si el elemento está en la lista de comunes,
          # pero aparece de nuevo en la segunda lista
          print(f"  ✓ Coincidencia duplicada: '{elemento1}'")
      else:
        print("  ✗ No hay coincidencia.")

  print("\n--- BÚSQUEDA FINALIZADA ---")
  print(f"\nResultado final: {elementos_comunes}")

  print("\nEstadísticas:")
  print(f" - Total de comparaciones realizadas: {comparaciones}")
  print(f" - Total de elementos comunes encontrados: {coincidencias}")

  return elementos_comunes

# --- Probando la función ---
lista_a = [10, 20, 30, 40, 50]
lista_b = [30, 60, 20, 70, 80, 20]

resultado = encontrar_elementos_comunes(lista_a, lista_b)