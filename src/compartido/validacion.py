def leer_entero(mensaje: str) -> int:
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Ingrese un numero entero valido.")


def leer_opcion(mensaje: str, opciones: list[str]) -> str:
    while True:
        opcion = input(mensaje).strip()

        if opcion in opciones:
            return opcion

        print(f"Ingrese una opcion valida: {', '.join(opciones)}")
