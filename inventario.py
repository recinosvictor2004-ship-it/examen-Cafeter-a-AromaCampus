from storage import load_coffees, save_coffees

VALID_TOSTADOS = {"ligero", "medio", "oscuro"}

def get_next_id(coffees):
    if not coffees:
        return 1
    return max(c["id"] for c in coffees) + 1
def agregar_cafe(nombre, descripcion, precio, tostado, disponible):
    coffees = load_coffees()
    if tostado not in VALID_TOSTADOS:
        raise ValueError("Nivel de tostado inválido.")
    nuevo = {
        "id": get_next_id(coffees),
        "nombre": nombre,
        "descripcion": descripcion,
        "precio": float(precio),
        "tostado": tostado,
        "disponible": bool(disponible)
    }
    coffees.append(nuevo)
    save_coffees(coffees)
    return nuevo

def listar_cafes():
    return load_coffees()

def editar_cafe(cafe_id, **kwargs):
    coffees = load_coffees()
    for c in coffees:
        if c["id"] == cafe_id:
            for key, value in kwargs.items():
                if key == "tostado" and value not in VALID_TOSTADOS:
                    raise ValueError("Nivel de tostado inválido.")
                if value is not None:
                    c[key] = value
            save_coffees(coffees)
            return c
    raise ValueError("Café no encontrado.")
def eliminar_cafe(cafe_id):
    coffees = load_coffees()
    new_list = [c for c in coffees if c["id"] != cafe_id]
    if len(new_list) == len(coffees):
        raise ValueError("Café no encontrado.")
    save_coffees(new_list)