def generar_id(registro: list[dict]) -> int:
    if not registro:
        return 1

    return registro[-1]["id"] + 1
