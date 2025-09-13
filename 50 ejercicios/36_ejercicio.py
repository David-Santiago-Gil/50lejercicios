# Suma de los dígitos de un número
def suma_digitos(numero):
  suma = 0
  # Convertir el número a cadena de texto para iterar sobre sus dígitos
  for digito in str(numero):
    suma += int(digito)
  return suma

# Pedir al usuario que ingrese un número
num_usuario = int(input("Ingresa un número para sumar sus dígitos: "))
resultado = suma_digitos(num_usuario)
print(f"La suma de los dígitos de {num_usuario} es: {resultado}")