class Coleccion:
  """
  Clase para administrar una colección de ítems.
  Incluye métodos para agregar ítems y eliminar duplicados.
  """
  def __init__(self, nombre_coleccion):
    self.nombre = nombre_coleccion
    self.items = []

  def agregar_item(self, item):
    """Agrega un ítem a la colección."""
    self.items.append(item)
    print(f"✓ Ítem '{item}' agregado a la colección '{self.nombre}'.")

  def mostrar_items(self):
    """Muestra todos los ítems de la colección."""
    print(f"\n--- Ítems en '{self.nombre}' ---")
    for item in self.items:
      print(f"- {item}")

  def eliminar_duplicados(self):
    """
    Elimina los ítems duplicados de la colección.
    Utiliza un 'set' para un proceso más eficiente.
    """
    if not self.items:
      print("\n✗ La colección está vacía, no hay duplicados para eliminar.")
      return

    items_sin_duplicados = list(set(self.items))
    self.items = items_sin_duplicados
    print("\n✓ Duplicados eliminados exitosamente.")

# --- Uso del programa ---

# Creamos una instancia de nuestra clase para una colección de frutas
frutas = Coleccion("Mi canasta de frutas")

# Agregamos ítems a la colección, incluyendo algunos duplicados
frutas.agregar_item("manzana")
frutas.agregar_item("banana")
frutas.agregar_item("manzana")
frutas.agregar_item("naranja")
frutas.agregar_item("uva")
frutas.agregar_item("banana")
frutas.agregar_item("manzana")

# Mostramos la colección con duplicados
frutas.mostrar_items()

# Eliminamos los duplicados
frutas.eliminar_duplicados()

# Mostramos la colección limpia
frutas.mostrar_items()