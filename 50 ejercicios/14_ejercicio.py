# Usando una lista de comprensión para encontrar pares
limite_pares = 20
pares = [i for i in range(1, limite_pares + 1) if i % 2 == 0]

print(f"Los números pares entre 1 y {limite_pares} son:")
print(pares)
print(f"Se encontraron {len(pares)} números pares.")