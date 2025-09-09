# Generador de secuencia de Fibonacci usando recursividad
def fibonacci_recursivo(n):
  """
  Calcula el n-ésimo número de la secuencia de Fibonacci.
  Esta función se llama a sí misma para resolver el problema.
  """
  # Casos base para detener la recursión
  if n <= 1:
    return n
  # Llamada recursiva para sumar los dos números anteriores
  else:
    return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

limite_fib = 10
print(f"Los primeros {limite_fib} números de la secuencia de Fibonacci son:")
# Usamos un bucle para llamar a la función en cada posición
for i in range(limite_fib):
  print(fibonacci_recursivo(i), end=" ")

print("\n¡Secuencia generada!")