# Clasificador del nivel de batería

nivel_bateria = 85  # Porcentaje de batería del celular

if nivel_bateria >= 80:
    clasificacion = "Carga óptima"
    mensaje = "¡Tu batería está en perfecto estado! Sigue así."
elif nivel_bateria >= 20:
    clasificacion = "Carga media"
    mensaje = "Puedes usar tu celular sin preocupaciones por ahora."
else:
    clasificacion = "Batería baja"
    mensaje = "Conecta tu celular a cargar pronto para evitar que se apague."

print("El nivel de batería es:", nivel_bateria, "%")
print("Clasificación:", clasificacion)
print("Comentario:", mensaje)