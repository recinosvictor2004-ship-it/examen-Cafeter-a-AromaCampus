from storage import load_coffees, save_coffees

VALID_TOSTADOS = {"ligero", "medio", "oscuro"}

def get_next_id(coffees):
    if not coffees:
        return 1
    return max(c["id"] for c in coffees) + 1
def eliminar_cafe(cafe_id):
    coffees = load_coffees()
    new_list = [c for c in coffees if c["id"] != cafe_id]
    if len(new_list) == len(coffees):
        raise ValueError("Café no encontrado.")
    save_coffees(new_list)