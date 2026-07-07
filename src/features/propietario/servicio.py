from src.shared.identificador import generar_id


def buscar_propietario_por_dni(dni: str, propietarios: list[dict]) -> dict | None:
    for propietario in propietarios:
        if propietario["dni"] == dni:
            return propietario

    return None


def crear_propietario(
    propietarios: list[dict],
    dni: str,
    nombre: str,
    telefono: str,
) -> dict | None:
    propietario_existente = buscar_propietario_por_dni(dni, propietarios)

    if propietario_existente:
        return None

    propietario = {
        "id": generar_id(propietarios),
        "dni": dni,
        "nombre": nombre,
        "telefono": telefono,
    }

    propietarios.append(propietario)
    return propietario
