from src.shared.busqueda import buscar_por_id
from src.shared.formato import (
    mostrar_error,
    mostrar_exito,
    mostrar_info,
    mostrar_separador,
    mostrar_titulo,
)
from src.shared.validacion import (
    confirmar,
    leer_fecha,
    leer_hora,
    leer_numero,
    leer_texto,
)
from src.features.mascota.presentacion import mostrar_mascotas
from src.features.turno.servicio import (
    cancelar_turno_servicio,
    crear_turno,
)


def asignar_turno(propietarios: list[dict], mascotas: list[dict], turnos: list[dict]) -> None:
    mostrar_titulo("Asignar Turno")

    if not mascotas:
        mostrar_error("No se puede asignar un turno porque no hay mascotas registradas.")
        mostrar_separador()
        return

    mostrar_mascotas(mascotas, propietarios)

    id_mascota = int(leer_numero("Ingrese el ID de la mascota: "))
    mascota = buscar_por_id(mascotas, id_mascota)

    if not mascota:
        mostrar_error("No se encontró una mascota con ese ID.")
        mostrar_separador()
        return

    fecha = leer_fecha("Ingrese la fecha del turno (dd/mm/yyyy): ")
    hora = leer_hora("Ingrese la hora del turno (HH:MM): ")
    nota = leer_texto("Ingrese la nota del turno: ")

    turno = crear_turno(turnos, id_mascota, fecha, hora, nota)

    if turno is None:
        mostrar_error("El horario seleccionado ya esta ocupado.")
        mostrar_separador()
        return

    mostrar_exito(f"Turno asignado para {mascota['nombre']} el {fecha} a las {hora}.")
    mostrar_separador()


def mostrar_turnos(turnos: list[dict], mascotas: list[dict]) -> None:
    mostrar_titulo("Lista de Turnos")

    if not turnos:
        mostrar_info("No hay turnos asignados.")
        mostrar_separador()
        return

    for turno in turnos:
        mascota = buscar_por_id(mascotas, turno["id_mascota"])

        if mascota is None:
            mostrar_error(f"No se encontró la mascota con ID {turno['id_mascota']}.")
            continue

        mostrar_info(
            f"ID: {turno['id']}, "
            f"Mascota: {mascota['nombre']}, "
            f"Fecha: {turno['fecha']}, "
            f"Hora: {turno['hora']}, "
            f"Estado: {turno['estado']}, "
            f"Nota: {turno['nota']}"
        )

    mostrar_separador()


def cancelar_turno(turnos: list[dict], mascotas: list[dict]) -> None:
    mostrar_titulo("Cancelar Turno")

    if not turnos:
        mostrar_info("No hay turnos asignados para cancelar.")
        mostrar_separador()
        return

    for turno in turnos:
        mascota = buscar_por_id(mascotas, turno["id_mascota"])

        if mascota is None:
            mostrar_error(f"No se encontró la mascota con ID {turno['id_mascota']}.")
            continue

        mostrar_info(
            f"ID: {turno['id']}, "
            f"Mascota: {mascota['nombre']}, "
            f"Fecha: {turno['fecha']}, "
            f"Hora: {turno['hora']}, "
            f"Estado: {turno['estado']}, "
            f"Nota: {turno['nota']}"
        )

    id_turno = int(leer_numero("Ingrese el ID del turno que desea cancelar: "))
    turno_a_cancelar = buscar_por_id(turnos, id_turno)

    if turno_a_cancelar is None:
        mostrar_error("No se encontró un turno con ese ID.")
        mostrar_separador()
        return

    if confirmar("Esta seguro que desea cancelar este turno?"):
        if cancelar_turno_servicio(turno_a_cancelar):
            mostrar_exito("Turno cancelado.")
        else:
            mostrar_error("No se puede cancelar un turno que no esta pendiente.")
    else:
        mostrar_info("Operación cancelada.")

    mostrar_separador()
