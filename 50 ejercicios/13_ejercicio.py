# Suma de los primeros N números usando una fórmula
def suma_gauss(n):
  return n * (n + 1) // 2

limite_suma = 100
resultado_suma = suma_gauss(limite_suma)
print(f"La suma de los números del 1 al {limite_suma} es: {resultado_suma}")