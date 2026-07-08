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
from src.shared.validacion import leer_fecha, leer_opcion, leer_numero, leer_texto
from src.features.mascota.presentacion import mostrar_mascotas
from src.features.seguimiento.servicio import registrar_seguimiento


def registrar_vacuna_o_control(
    propietarios: list[dict],
    mascotas: list[dict],
    seguimientos: list[dict],
) -> None:
    mostrar_titulo("Registrar Vacuna / Control Próximo")

    if not mascotas:
        mostrar_error("No se puede registrar un seguimiento porque no hay mascotas registradas.")
        mostrar_separador()
        return

    mostrar_mascotas(mascotas, propietarios)

    id_mascota = int(leer_numero("Ingrese el ID de la mascota: "))
    mascota = buscar_por_id(mascotas, id_mascota)

    if mascota is None:
        mostrar_error("No se encontró una mascota con ese ID.")
        mostrar_separador()
        return

    mostrar_subtitulo("Tipo de seguimiento")
    mostrar_opciones(["Vacuna", "Control"])

    opcion_tipo = leer_opcion(
        "Ingrese el número correspondiente al tipo de seguimiento: ",
        ["1", "2"],
    )

    tipos = {
        "1": "Vacuna",
        "2": "Control",
    }

    tipo = tipos[opcion_tipo]

    descripcion = leer_texto("Ingrese la descripción del seguimiento: ")
    fecha_registro = leer_fecha("Ingrese la fecha de registro/aplicación (dd/mm/yyyy): ")
    proxima_fecha = leer_fecha("Ingrese la próxima fecha (dd/mm/yyyy): ")
    observaciones = leer_texto("Ingrese observaciones: ")

    seguimiento = registrar_seguimiento(
        seguimientos,
        id_mascota,
        tipo,
        descripcion,
        fecha_registro,
        proxima_fecha,
        observaciones,
    )

    mostrar_exito(f"{tipo} registrada correctamente con ID {seguimiento['id']}.")
    mostrar_info(
        f"Mascota: {mascota['nombre']} | "
        f"Descripción: {seguimiento['descripcion']} | "
        f"Próxima fecha: {seguimiento['proxima_fecha']}"
    )

    mostrar_separador()


def mostrar_seguimientos(
    propietarios: list[dict],
    mascotas: list[dict],
    seguimientos: list[dict],
) -> None:
    mostrar_titulo("Vacunas y Controles Registrados")

    if not seguimientos:
        mostrar_info("No hay vacunas ni controles registrados.")
        mostrar_separador()
        return

    for seguimiento in seguimientos:
        mascota = buscar_por_id(mascotas, seguimiento["id_mascota"])

        nombre_mascota = "Desconocida"
        if mascota is not None:
            nombre_mascota = mascota["nombre"]

        mostrar_info(
            f"ID: {seguimiento['id']}, "
            f"Mascota: {nombre_mascota}, "
            f"Tipo: {seguimiento['tipo']}, "
            f"Descripción: {seguimiento['descripcion']}, "
            f"Fecha registro: {seguimiento['fecha_registro']}, "
            f"Próxima fecha: {seguimiento['proxima_fecha']}, "
            f"Estado: {seguimiento['estado']}, "
            f"Observaciones: {seguimiento['observaciones']}"
        )

    mostrar_separador()