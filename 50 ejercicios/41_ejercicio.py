# Gestor de Tareas
def gestor_tareas():
    tareas = []
    print("¡Bienvenido al Gestor de Tareas!")

    while True:
        print("\nMenú:")
        print("1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Eliminar tarea")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            nueva_tarea = input("Escribe la nueva tarea: ")
            tareas.append(nueva_tarea)
            print(f"Tarea '{nueva_tarea}' agregada.")
        elif opcion == '2':
            if not tareas:
                print("No hay tareas pendientes.")
            else:
                print("\n--- Tus Tareas Pendientes ---")
                for i, tarea in enumerate(tareas):
                    print(f"{i + 1}. {tarea}")
        elif opcion == '3':
            if not tareas:
                print("No hay tareas para eliminar.")
            else:
                try:
                    indice = int(input("Ingresa el número de la tarea a eliminar: ")) - 1
                    if 0 <= indice < len(tareas):
                        tarea_eliminada = tareas.pop(indice)
                        print(f"Tarea '{tarea_eliminada}' eliminada.")
                    else:
                        print("Número de tarea no válido.")
                except ValueError:
                    print("Por favor, ingresa un número.")
        elif opcion == '4':
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

gestor_tareas()