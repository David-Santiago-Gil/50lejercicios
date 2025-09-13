# Buscador de Números Primos en un Rango
def encontrar_primos(limite):
    primos = []
    for numero in range(2, limite + 1):
        es_primo = True
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(numero)
    return primos

try:
    num_limite = int(input("Ingresa un número para encontrar los primos hasta ese punto: "))
    if num_limite >= 2:
        lista_primos = encontrar_primos(num_limite)
        print(f"\nLos números primos hasta {num_limite} son:")
        print(lista_primos)
    else:
        print("Por favor, ingresa un número mayor o igual a 2.")
except ValueError:
    print("Entrada no válida. Por favor, ingresa un número entero.")