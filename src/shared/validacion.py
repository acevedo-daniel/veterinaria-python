def leer_opcion(mensaje: str, opciones: list[str]) -> str:
    while True:
        opcion = input(mensaje).strip()

        if opcion in opciones:
            return opcion

        print(f"Ingrese una opcion valida: {', '.join(opciones)}")


def leer_texto(mensaje: str) -> str:
    while True:
        texto = input(mensaje).strip()

        if texto:
            return texto

        print("Error: el campo no puede quedar vacio.")


def leer_numero(mensaje: str) -> str:
    while True:
        texto = input(mensaje).strip()

        if texto.isdigit():
            return texto

        print("Error: debe ingresar solamente numeros.")

def leer_numero_negativo(mensaje: str) -> int:
    while True:
        texto = input(mensaje).strip()

        if texto.isdigit() and int(texto) >= 0:
            return int(texto)

        print("Error: debe ingresar un numero positivo o cero.")
