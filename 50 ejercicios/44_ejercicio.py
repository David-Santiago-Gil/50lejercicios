# Verificador de Palíndromos en una Lista
def es_palindromo(palabra):
    # Ignorar espacios y mayúsculas
    palabra_limpia = palabra.replace(" ", "").lower()
    # Comparar la palabra con su versión invertida
    return palabra_limpia == palabra_limpia[::-1]

def verificar_lista_palindromos(lista_palabras):
    print("--- Verificando la lista de palabras ---")
    for palabra in lista_palabras:
        if es_palindromo(palabra):
            print(f"'{palabra}' es un palíndromo.")
        else:
            print(f"'{palabra}' no es un palíndromo.")

# Lista de ejemplo
lista_de_palabras = ["reconocer", "radar", "sol", "anita lava la tina", "programacion"]
verificar_lista_palindromos(lista_de_palabras)