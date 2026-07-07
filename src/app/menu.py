from src.app.datos import propietarios
from src.features.propietario.presentacion import (
    mostrar_propietarios,
    registrar_propietario,
)
from src.shared.formato import mostrar_titulo
from src.shared.validacion import leer_opcion


OPCIONES_MENU = [
    "Registrar propietario",
    "Registrar mascota",
    "Mostrar propietarios",
    "Mostrar mascotas",
    "Consultar mascota",
    "Asignar turno",
    "Mostrar turnos",
    "Atender turno",
    "Cancelar turno",
    "Mostrar atenciones",
    "Mostrar estadisticas",
]


def mostrar_menu(titulo: str, opciones: list[str]) -> None:
    mostrar_titulo(titulo)

    for indice, opcion in enumerate(opciones, start=1):
        print(f"{indice}. {opcion}")

    print("0. Salir")


def ejecutar_menu() -> None:
    opciones_validas = [str(numero) for numero in range(len(OPCIONES_MENU) + 1)]

    while True:
        mostrar_menu("Veterinaria", OPCIONES_MENU)
        opcion = leer_opcion("Seleccione una opcion: ", opciones_validas)

        if opcion == "1":
            registrar_propietario(propietarios)
        elif opcion == "3":
            mostrar_propietarios(propietarios)
        elif opcion == "0":
            print("Programa finalizado correctamente.")
            break
        else:
            print("La funcionalidad todavia no fue implementada.")
