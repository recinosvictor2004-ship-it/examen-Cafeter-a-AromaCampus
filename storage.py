import json
from pathlib import Path

DATA_PATH = Path("data/coffees.json")

def load_coffees():
    if not DATA_PATH.exists():
        return []
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_coffees(coffees):
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(coffees, f, ensure_ascii=False, indent=2)

    