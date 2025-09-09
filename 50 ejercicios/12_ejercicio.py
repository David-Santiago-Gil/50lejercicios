# Suma de los números desde el 1 hasta un número dado

# Pide al usuario que ingrese un número
numero_limite = int(input("Ingresa un número para sumar hasta él: "))

# Inicializa la suma y un contador
suma = 0
contador = 1

# Bucle para sumar los números
while contador <= numero_limite:
  suma = suma + contador
  contador = contador + 1

# Muestra el resultado
print(f"La suma de todos los números hasta el {numero_limite} es: {suma}")