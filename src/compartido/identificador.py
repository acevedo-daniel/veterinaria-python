def generar_id(registros: list[dict]) -> int:
    if not registros:
        return 1

    return registros[-1]["id"] + 1
