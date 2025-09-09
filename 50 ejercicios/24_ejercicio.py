import random
import string

class GeneradorContrasena:
    """Clase para generar y evaluar la fortaleza de una contraseña."""

    def __init__(self, longitud=8, incluir_mayusculas=True, incluir_numeros=True, incluir_simbolos=False):
        """Inicializa el generador con las características deseadas."""
        self.longitud = longitud
        self.caracteres = string.ascii_lowercase
        if incluir_mayusculas:
            self.caracteres += string.ascii_uppercase
        if incluir_numeros:
            self.caracteres += string.digits
        if incluir_simbolos:
            self.caracteres += "!@#$%&*()_-+="

    def generar(self):
        """Genera una contraseña aleatoria basada en las propiedades de la clase."""
        contrasena_generada = ''.join(random.choice(self.caracteres) for _ in range(self.longitud))
        return contrasena_generada

    def evaluar_fortaleza(self, contrasena):
        """Evalúa la fortaleza de una contraseña dada."""
        puntos = 0
        comentarios = []

        # Evaluación de la longitud
        if len(contrasena) >= 12:
            puntos += 2
            comentarios.append("✓ Longitud muy adecuada")
        elif len(contrasena) >= 8:
            puntos += 1
            comentarios.append("✓ Longitud adecuada")
        else:
            comentarios.append("✗ Contraseña muy corta")

        # Evaluación de la composición
        if any(char.isupper() for char in contrasena):
            puntos += 1
            comentarios.append("✓ Contiene mayúsculas")
        else:
            comentarios.append("✗ No contiene mayúsculas")

        if any(char.isdigit() for char in contrasena):
            puntos += 1
            comentarios.append("✓ Contiene números")
        else:
            comentarios.append("✗ No contiene números")

        if any(not char.isalnum() for char in contrasena):
            puntos += 1
            comentarios.append("✓ Contiene símbolos")
        else:
            comentarios.append("✗ No contiene símbolos")
        
        # Asignar nivel de fortaleza
        if puntos >= 5:
            fortaleza = "Muy Fuerte"
        elif puntos >= 3:
            fortaleza = "Moderada"
        else:
            fortaleza = "Débil"
        
        return fortaleza, comentarios

# --- Uso del programa ---
print("GENERADOR Y EVALUADOR DE CONTRASEÑAS POO")
print("=" * 45)

# 1. Generar una contraseña con la configuración por defecto (8 caracteres, mayúsculas, números)
generador1 = GeneradorContrasena()
contrasena1 = generador1.generar()
fortaleza1, comentarios1 = generador1.evaluar_fortaleza(contrasena1)

print("\nTipo 1: Por defecto (8 caracteres, mayúsculas, números)")
print(f"Contraseña: {contrasena1}")
print(f"Fortaleza: {fortaleza1}")
for c in comentarios1:
    print(f"  {c}")

# 2. Generar una contraseña más larga con todos los tipos de caracteres
generador2 = GeneradorContrasena(longitud=12, incluir_simbolos=True)
contrasena2 = generador2.generar()
fortaleza2, comentarios2 = generador2.evaluar_fortaleza(contrasena2)

print("\nTipo 2: Larga y compleja (12 caracteres, mayúsculas, números, símbolos)")
print(f"Contraseña: {contrasena2}")
print(f"Fortaleza: {fortaleza2}")
for c in comentarios2:
    print(f"  {c}")

# 3. Evaluar una contraseña débil manualmente
contrasena3 = "123"
fortaleza3, comentarios3 = generador1.evaluar_fortaleza(contrasena3)

print("\nTipo 3: Contraseña manual y débil")
print(f"Contraseña: {contrasena3}")
print(f"Fortaleza: {fortaleza3}")
for c in comentarios3:
    print(f"  {c}")