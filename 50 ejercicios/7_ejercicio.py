# Calculadora de IVA

# Define el precio base del producto
# Puedes cambiar este valor por el que desees
precio_base = 100

# Define el porcentaje de IVA (19% en Colombia)
# Puedes cambiar este valor si el porcentaje es diferente en tu región
tasa_iva = 0.19

# Calcula el monto del IVA
monto_iva = precio_base * tasa_iva

# Calcula el precio final (precio base + IVA)
precio_final = precio_base + monto_iva

# Imprime los resultados
print(f"Precio base: ${precio_base:.2f}")
print(f"Monto del IVA: ${monto_iva:.2f}")
print(f"Precio final (con IVA): ${precio_final:.2f}")
