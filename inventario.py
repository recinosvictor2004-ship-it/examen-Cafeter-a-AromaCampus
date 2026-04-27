from storage import load_coffees, save_coffees

VALID_TOSTADOS = {"ligero", "medio", "oscuro"}

def get_next_id(coffees):
    if not coffees:
        return 1
    return max(c["id"] for c in coffees) + 1