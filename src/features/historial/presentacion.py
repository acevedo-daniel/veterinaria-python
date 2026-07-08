from src.shared.busqueda import buscar_por_id
from src.shared.formato import (
    mostrar_error,
    mostrar_info,
    mostrar_separador,
    mostrar_titulo,
)
from src.shared.validacion import leer_numero
from src.features.mascota.presentacion import mostrar_mascotas


def consultar_historial_mascota(
    propietarios: list[dict],
    mascotas: list[dict],
    turnos: list[dict],
    atenciones: list[dict],
    servicios: list[dict],
) -> None:
    mostrar_titulo("Historial Clínico")

    if not mascotas:
        mostrar_error("No hay mascotas registradas.")
        mostrar_separador()
        return

    mostrar_mascotas(mascotas, propietarios)

    id_mascota = int(leer_numero("Ingrese el ID de la mascota: "))
    mascota = buscar_por_id(mascotas, id_mascota)

    if mascota is None:
        mostrar_error("No se encontró una mascota con ese ID.")
        mostrar_separador()
        return

    mostrar_info(
        f"Mascota: {mascota['nombre']} | "
        f"Especie: {mascota['especie']} | "
        f"Raza: {mascota['raza']} | "
        f"Edad: {mascota['edad']} años"
    )

    tiene_atenciones = False

    for atencion in atenciones:
        turno = buscar_por_id(turnos, atencion["id_turno"])

        if turno is None:
            continue

        if turno["id_mascota"] != id_mascota:
            continue

        servicio = buscar_por_id(servicios, atencion["id_servicio"])

        nombre_servicio = "Servicio desconocido"
        if servicio is not None:
            nombre_servicio = servicio["nombre"]

        tiene_atenciones = True

        mostrar_info(
            f"\nFecha: {turno['fecha']}\n"
            f"Hora: {turno['hora']}\n"
            f"Servicio: {nombre_servicio}\n"
            f"Diagnóstico: {atencion['diagnostico']}\n"
            f"Observaciones: {atencion['observaciones']}\n"
            f"Importe: ${atencion['importe']}"
        )

    if not tiene_atenciones:
        mostrar_info("Esta mascota todavía no tiene atenciones registradas.")

    mostrar_separador()