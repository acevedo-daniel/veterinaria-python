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

from datetime import datetime, date


def convertir_fecha(fecha_texto: str) -> date | None:
    try:
        return datetime.strptime(fecha_texto, "%d/%m/%Y").date()
    except ValueError:
        return None


def obtener_alertas_seguimientos(seguimientos: list[dict], dias_anticipacion: int = 7) -> list[dict]:
    alertas = []
    hoy = date.today()

    for seguimiento in seguimientos:
        proxima_fecha = convertir_fecha(seguimiento["proxima_fecha"])

        if proxima_fecha is None:
            continue

        diferencia_dias = (proxima_fecha - hoy).days

        if diferencia_dias < 0:
            estado_alerta = "Vencido"
        elif diferencia_dias == 0:
            estado_alerta = "Para hoy"
        elif diferencia_dias <= dias_anticipacion:
            estado_alerta = "Próximo"
        else:
            continue

        alerta = {
            "id": seguimiento["id"],
            "id_mascota": seguimiento["id_mascota"],
            "tipo": seguimiento["tipo"],
            "descripcion": seguimiento["descripcion"],
            "proxima_fecha": seguimiento["proxima_fecha"],
            "estado_alerta": estado_alerta,
            "dias_restantes": diferencia_dias,
        }

        alertas.append(alerta)

    return alertas