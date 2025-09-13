# Analizador de Contraseña
def analizar_contrasena(contrasena):
    puntuacion = 0
    tiene_longitud = len(contrasena) >= 8
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_digito = False

    for caracter in contrasena:
        if caracter.isupper():
            tiene_mayuscula = True
        elif caracter.islower():
            tiene_minuscula = True
        elif caracter.isdigit():
            tiene_digito = True
    
    if tiene_longitud:
        puntuacion += 1
    if tiene_mayuscula:
        puntuacion += 1
    if tiene_minuscula:
        puntuacion += 1
    if tiene_digito:
        puntuacion += 1

    if puntuacion >= 3:
        print("¡Contraseña fuerte!")
    else:
        print("Contraseña débil. Intenta mejorarla.")
    
    print(f"\nPuntuación: {puntuacion}/4")
    print(f"Longitud >= 8 caracteres: {tiene_longitud}")
    print(f"Contiene mayúscula: {tiene_mayuscula}")
    print(f"Contiene minúscula: {tiene_minuscula}")
    print(f"Contiene dígito: {tiene_digito}")

# Pedir al usuario que ingrese una contraseña
contrasena_usuario = input("Ingresa una contraseña para analizar su fortaleza: ")
analizar_contrasena(contrasena_usuario)