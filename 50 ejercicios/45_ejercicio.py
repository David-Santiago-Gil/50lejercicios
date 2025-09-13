# Conversor de Unidades de Temperatura
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temperaturas_celsius = [0, 10, 25, 30, -5, 100]
temperaturas_fahrenheit = []

print("Temperaturas originales en Celsius:", temperaturas_celsius)

for temp_c in temperaturas_celsius:
    temp_f = celsius_a_fahrenheit(temp_c)
    temperaturas_fahrenheit.append(temp_f)
    print(f"  {temp_c}°C es igual a {temp_f}°F")

print("\nLista de temperaturas convertidas a Fahrenheit:", temperaturas_fahrenheit)