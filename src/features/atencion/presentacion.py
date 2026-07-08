from src.shared.busqueda import buscar_por_id
from src.shared.formato import (
    mostrar_error,
    mostrar_exito,
    mostrar_info,
    mostrar_separador,
    mostrar_titulo,
)
from src.shared.validacion import leer_numero, leer_texto
from src.servicios_veterinarios.presentacion import mostrar_servicios
from src.features.turno.presentacion import mostrar_turnos
from src.features.atencion.servicio import registrar_atencion


def atender_turno(
    turnos: list[dict],
    mascotas: list[dict],
    servicios: list[dict],
    atenciones: list[dict],
) -> None:
    mostrar_titulo("Atender Turno")

    if not turnos:
        mostrar_info("No hay turnos asignados.")
        mostrar_separador()
        return

    mostrar_turnos(turnos, mascotas)

    id_turno = int(leer_numero("Ingrese el ID del turno a atender: "))
    turno = buscar_por_id(turnos, id_turno)

    if not turno:
        mostrar_error("No se encontro un turno con ese ID.")
        mostrar_separador()
        return

    if turno["estado"] != "Pendiente":
        mostrar_error("No se puede atender un turno que no esta pendiente.")
        mostrar_separador()
        return

    mostrar_servicios(servicios)

    id_servicio = int(leer_numero("Ingrese el ID del servicio realizado: "))
    servicio = buscar_por_id(servicios, id_servicio)

    if not servicio:
        mostrar_error("No se encontro un servicio con ese ID.")
        mostrar_separador()
        return

    diagnostico = leer_texto("Ingrese el diagnostico: ")
    observaciones = leer_texto("Ingrese las observaciones: ")

    atencion = registrar_atencion(
        atenciones,
        turno,
        servicio,
        diagnostico,
        observaciones,
    )

    if atencion:
        mostrar_exito(f"Atencion registrada con ID {atencion['id']}.")
        mostrar_info(f"Importe a pagar: ${atencion['importe']}")
    else:
        mostrar_error("No se pudo registrar la atencion.")

    mostrar_separador()


def mostrar_atenciones(
    atenciones: list[dict],
    turnos: list[dict],
    mascotas: list[dict],
    servicios: list[dict],
) -> None:
    mostrar_titulo("Lista de Atenciones")

    if not atenciones:
        mostrar_info("No hay atenciones registradas.")
        mostrar_separador()
        return

    for atencion in atenciones:
        turno = buscar_por_id(turnos, atencion["id_turno"])
        servicio = buscar_por_id(servicios, atencion["id_servicio"])

        nombre_mascota = "Desconocida"
        if turno:
            mascota = buscar_por_id(mascotas, turno["id_mascota"])
            if mascota:
                nombre_mascota = mascota["nombre"]

        nombre_servicio = "Desconocido"
        if servicio:
            nombre_servicio = servicio["nombre"]

        mostrar_info(
            f"ID: {atencion['id']}, "
            f"Mascota: {nombre_mascota}, "
            f"Servicio: {nombre_servicio}, "
            f"Diagnostico: {atencion['diagnostico']}, "
            f"Observaciones: {atencion['observaciones']}, "
            f"Importe: ${atencion['importe']}"
        )

    mostrar_separador()
