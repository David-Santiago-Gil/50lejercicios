# Validador de números de teléfono

# Número a validar
numero_de_telefono = "5512345678"

# Longitud esperada (por ejemplo, 10 dígitos para un número de México)
longitud_esperada = 10 

print("Número a validar:", numero_de_telefono)
print("Longitud del número:", len(numero_de_telefono))

# 1. Verificar la longitud
if len(numero_de_telefono) == longitud_esperada:
    print("✓ El número tiene la longitud correcta.")
    
    # 2. Verificar si todos los caracteres son dígitos
    if numero_de_telefono.isdigit():
        print("✓ El número contiene solo dígitos.")
        print("\n¡El número de teléfono es válido!")
    else:
        print("✗ El número de teléfono contiene caracteres no válidos (letras o símbolos).")
else:
    print("✗ El número de teléfono no tiene la longitud correcta.")
    