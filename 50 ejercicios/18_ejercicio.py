# Contar vocales en una cadena de texto
oracion = "¡Hola, mundo! Esto es un test."
vocales_encontradas = sum(1 for char in oracion.lower() if char in "aeiou")
print(f"El texto '{oracion}' tiene {vocales_encontradas} vocales.")