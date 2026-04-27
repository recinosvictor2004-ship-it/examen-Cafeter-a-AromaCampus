from main import (
    mostrar_menu,
    opcion_listar,
    opcion_agregar,
    opcion_editar,
    opcion_eliminar,
)

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            opcion_listar()
        elif opcion == "2":
            opcion_agregar()
        elif opcion == "3":
            opcion_editar()
        elif opcion == "4":
            opcion_eliminar()
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()