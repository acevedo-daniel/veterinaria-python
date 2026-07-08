from src.shared.identificador import generar_id


def registrar_seguimiento(
    seguimientos: list[dict],
    id_mascota: int,
    tipo: str,
    descripcion: str,
    fecha_registro: str,
    proxima_fecha: str,
    observaciones: str,
) -> dict:
    seguimiento = {
        "id": generar_id(seguimientos),
        "id_mascota": id_mascota,
        "tipo": tipo,
        "descripcion": descripcion,
        "fecha_registro": fecha_registro,
        "proxima_fecha": proxima_fecha,
        "observaciones": observaciones,
        "estado": "Pendiente",
    }

    seguimientos.append(seguimiento)
    return seguimiento