from src.shared.identificador import generar_id


def horario_ocupado(turnos: list[dict], fecha: str, hora: str) -> bool:
    for turno in turnos:
        misma_fecha = turno["fecha"] == fecha
        misma_hora = turno["hora"] == hora
        esta_pendiente = turno["estado"] == "Pendiente"

        if misma_fecha and misma_hora and esta_pendiente:
            return True

    return False


def crear_turno(
    turnos: list[dict],
    id_mascota: int,
    fecha: str,
    hora: str,
    nota: str,
) -> dict | None:
    if horario_ocupado(turnos, fecha, hora):
        return None

    turno = {
        "id": generar_id(turnos),
        "id_mascota": id_mascota,
        "fecha": fecha,
        "hora": hora,
        "nota": nota,
        "estado": "Pendiente",
    }

    turnos.append(turno)
    return turno


def cancelar_turno_servicio(turno: dict) -> bool:
    if turno["estado"] != "Pendiente":
        return False

    turno["estado"] = "Cancelado"
    return True
