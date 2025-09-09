import random

# Título del juego
print("¡Bienvenido al Bingo de Python!")

# Generar un cartón de bingo
# Usamos un conjunto (set) para evitar números duplicados
carton_de_bingo = set()
while len(carton_de_bingo) < 5:
    carton_de_bingo.add(random.randint(1, 20)) # Números entre 1 y 20

print(f"Tu cartón de bingo es: {sorted(list(carton_de_bingo))}")

# Simular que se sacan 5 números del "bolillero"
numeros_sacados = set()
while len(numeros_sacados) < 5:
    numeros_sacados.add(random.randint(1, 20))

print(f"Los números que salieron son: {sorted(list(numeros_sacados))}")

# Comparar los números para ver cuántos aciertos tiene el jugador
aciertos = carton_de_bingo.intersection(numeros_sacados)

# Mostrar el resultado
if len(aciertos) == 5:
    print("\n¡BINGO! ¡Felicidades, ganaste!")
elif len(aciertos) > 0:
    print(f"\n¡Casi! Tuviste {len(aciertos)} aciertos.")
    print(f"Tus números acertados son: {sorted(list(aciertos))}")
else:
    print("\nLo siento, no tuviste ningún acierto. ¡Intenta de nuevo!")