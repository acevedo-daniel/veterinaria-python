from src.shared.identificador import generar_id


def registrar_atencion(
    atenciones: list[dict],
    turno: dict,
    servicio: dict,
    diagnostico: str,
    observaciones: str,
) -> dict | None:
    if turno["estado"] != "Pendiente":
        return None

    atencion = {
        "id": generar_id(atenciones),
        "id_turno": turno["id"],
        "id_servicio": servicio["id"],
        "diagnostico": diagnostico,
        "observaciones": observaciones,
        "importe": servicio["precio"],
    }

    atenciones.append(atencion)
    turno["estado"] = "Atendido"

    return atencion
