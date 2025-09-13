# Inversor de Palabras en una Frase
def invertir_palabras_en_frase(frase):
    # Dividir la frase en palabras
    palabras = frase.split()
    
    palabras_invertidas = []
    
    # Invertir cada palabra en un bucle
    for palabra in palabras:
        palabra_invertida = palabra[::-1]
        palabras_invertidas.append(palabra_invertida)
        
    # Unir las palabras invertidas en una nueva frase
    frase_invertida = " ".join(palabras_invertidas)
    
    return frase_invertida

frase_usuario = input("Ingresa una frase para invertir las palabras: ")
frase_resultante = invertir_palabras_en_frase(frase_usuario)
print(f"Frase original: '{frase_usuario}'")
print(f"Frase con palabras invertidas: '{frase_resultante}'")