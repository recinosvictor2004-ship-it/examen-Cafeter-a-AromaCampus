from inventario import (
    agregar_cafe,
    listar_cafes,
    editar_cafe,
    eliminar_cafe
)

def mostrar_menu():
    print("\n--- Cafetería AromaCampus ---")
    print("1. Listar tipos de café")
    print("2. Agregar tipo de café")
    print("3. Editar tipo de café")
    print("4. Eliminar tipo de café")
    print("5. Salir")

def pedir_bool(mensaje):
    valor = input(mensaje + " (s/n): ").strip().lower()
    return valor == "s"

def opcion_listar():
    cafes = listar_cafes()
    if not cafes:
        print("No hay cafés registrados.")
        return
    for c in cafes:
        estado = "En stock" if c["disponible"] else "Sin stock"
        print(f"[{c['id']}] {c['nombre']} - Q{c['precio']} ({c['tostado']}) - {estado}")

def opcion_agregar():
    nombre = input("Nombre: ")
    descripcion = input("Descripción: ")
    precio = input("Precio: ")
    tostado = input("Tostado (ligero/medio/oscuro): ").lower()
    disponible = pedir_bool("¿Disponible?")
    try:
        nuevo = agregar_cafe(nombre, descripcion, precio, tostado, disponible)
        print("Café agregado:", nuevo)
    except ValueError as e:
        print("Error:", e)

def opcion_editar():
    try:
        cafe_id = int(input("ID del café a editar: "))
    except ValueError:
        print("ID inválido.")
        return
    nombre = input("Nuevo nombre (enter para mantener): ") or None
    descripcion = input("Nueva descripción (enter para mantener): ") or None
    precio = input("Nuevo precio (enter para mantener): ") or None
    tostado = input("Nuevo tostado (ligero/medio/oscuro, enter para mantener): ").lower() or None
    disponible_str = input("¿Disponible? (s/n, enter para mantener): ").strip().lower()
    disponible = None
    if disponible_str in ("s", "n"):
        disponible = disponible_str == "s"
    try:
        editar_cafe(
            cafe_id,
            nombre=nombre,
            descripcion=descripcion,
            precio=float(precio) if precio else None,
            tostado=tostado,
            disponible=disponible
        )
        print("Café actualizado.")
    except ValueError as e:
        print("Error:", e)

def opcion_eliminar():
    try:
        cafe_id = int(input("ID del café a eliminar: "))
    except ValueError:
        print("ID inválido.")
        return
    try:
        eliminar_cafe(cafe_id)
        print("Café eliminado.")
    except ValueError as e:
        print("Error:", e)