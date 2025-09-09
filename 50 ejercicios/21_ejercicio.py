# Verificación de palíndromo con slicing
def es_palindromo(texto):
  texto_limpio = texto.replace(" ", "").lower()
  return texto_limpio == texto_limpio[::-1]

frase_ejemplo = "anita lava la tina"
if es_palindromo(frase_ejemplo):
  print(f"'{frase_ejemplo}' es un palíndromo.")
else:
  print(f"'{frase_ejemplo}' no es un palíndromo.")