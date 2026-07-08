from src.shared.busqueda import buscar_por_id
from src.shared.formato import (
    mostrar_error,
    mostrar_exito,
    mostrar_info,
    mostrar_opciones,
    mostrar_separador,
    mostrar_subtitulo,
    mostrar_titulo,
)
from src.shared.validacion import (
    leer_numero,
    leer_numero_negativo,
    leer_opcion,
    leer_texto,
)
from src.features.propietario.presentacion import mostrar_propietarios
from src.features.mascota.servicio import buscar_mascota, crear_mascota


def registrar_mascota(propietarios: list[dict], mascotas: list[dict]) -> None:
    mostrar_titulo("Registrar Mascota")

    if not propietarios:
        mostrar_error("No se puede registrar una mascota porque no hay propietarios registrados.")
        mostrar_separador()
        return

    mostrar_propietarios(propietarios)

    id_propietario = int(leer_numero("Ingrese el ID del propietario de la mascota: "))
    propietario = buscar_por_id(propietarios, id_propietario)

    if not propietario:
        mostrar_error(f"No se encontro un propietario con el ID {id_propietario}.")
        mostrar_separador()
        return

    nombre = leer_texto("Ingrese el nombre de la mascota: ")

    mostrar_subtitulo("Especies")
    mostrar_opciones(["Perro", "Gato", "Ave", "Otra"])

    opcion_especie = leer_opcion(
        "Ingrese el numero correspondiente a la especie de la mascota: ",
        ["1", "2", "3", "4"],
    )
    especies = {
        "1": "Perro",
        "2": "Gato",
        "3": "Ave",
        "4": "Otra",
    }
    especie = especies[opcion_especie]

    raza = leer_texto("Ingrese la raza de la mascota: ")
    edad = leer_numero_negativo("Ingrese la edad de la mascota en anios: ")

    mascota = crear_mascota(mascotas, nombre, especie, raza, edad, id_propietario)

    if mascota:
        mostrar_exito(f"Mascota registrada: {mascota}")
    else:
        mostrar_error(
            f"Ya existe una mascota con el nombre '{nombre}' para el propietario con ID {id_propietario}."
        )
        mostrar_info(f"Mascota existente: {buscar_mascota(mascotas, nombre, id_propietario)}")

    mostrar_separador()


def mostrar_mascotas(mascotas: list[dict], propietarios: list[dict]) -> None:
    mostrar_titulo("Lista de Mascotas")

    if not mascotas:
        mostrar_info("No hay mascotas registradas.")
    else:
        for mascota in mascotas:
            propietario = buscar_por_id(propietarios, mascota["id_propetario"])
            nombre_propietario = "Desconocido"
            if propietario:
                nombre_propietario = propietario["nombre"]
            mostrar_info(
                f"ID: {mascota['id']}, "
                f"Nombre: {mascota['nombre']}, "
                f"Especie: {mascota['especie']}, "
                f"Raza: {mascota['raza']}, "
                f"Edad: {mascota['edad']} anios, "
                f"Propietario: {nombre_propietario}"
            )

    mostrar_separador()


def consultar_mascota(mascotas: list[dict], propietarios: list[dict]) -> None:
    mostrar_titulo("Consultar Mascota")

    if not mascotas:
        mostrar_info("No hay mascotas registradas.")
        mostrar_separador()
        return

    id_mascota = int(leer_numero("Ingrese el ID de la mascota a consultar: "))
    mascota = buscar_por_id(mascotas, id_mascota)

    if not mascota:
        mostrar_error(f"No se encontro una mascota con el ID {id_mascota}.")
    else:
        propietario = buscar_por_id(propietarios, mascota["id_propetario"])
        nombre_propietario = "Desconocido"
        if propietario:
            nombre_propietario = propietario["nombre"]
        mostrar_info(
            f"ID: {mascota['id']}, "
            f"Nombre: {mascota['nombre']}, "
            f"Especie: {mascota['especie']}, "
            f"Raza: {mascota['raza']}, "
            f"Edad: {mascota['edad']} anios, "
            f"Propietario: {nombre_propietario}"
        )

    mostrar_separador()
