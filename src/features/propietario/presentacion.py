from src.features.propietario.servicio import (
    buscar_propietario_por_dni,
    crear_propietario,
)
from src.shared.formato import (
    mostrar_error,
    mostrar_exito,
    mostrar_info,
    mostrar_separador,
    mostrar_titulo,
)
from src.shared.validacion import leer_numero, leer_texto, leer_dni 


def registrar_propietario(propietarios: list[dict]) -> None:
    mostrar_titulo("Registrar Propietario")

    dni = leer_dni("Ingrese el DNI del propietario (8 dígitos): ")
    nombre = leer_texto("Ingrese el nombre del propietario: ")
    telefono = leer_numero("Ingrese el telefono del propietario: ")

    propietario = crear_propietario(propietarios, dni, nombre, telefono)

    if propietario:
        mostrar_exito(f"Propietario registrado: {propietario}")
    else:
        mostrar_error(f"Ya existe un propietario con el DNI {dni}.")
        mostrar_info(f"Propietario existente: {buscar_propietario_por_dni(dni, propietarios)}")

    mostrar_separador()


def mostrar_propietarios(propietarios: list[dict]) -> None:
    mostrar_titulo("Lista de Propietarios")

    if not propietarios:
        mostrar_info("No hay propietarios registrados.")
    else:
        for propietario in propietarios:
            mostrar_info(
                f"ID: {propietario['id']}, "
                f"DNI: {propietario['dni']}, "
                f"Nombre: {propietario['nombre']}, "
                f"Telefono: {propietario['telefono']}"
            )

    mostrar_separador()
