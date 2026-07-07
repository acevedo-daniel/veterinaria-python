def buscar_por_id(id_buscado: int, registros: list[dict]) -> dict | None:
    for registro in registros:
        if registro["id"] == id_buscado:
            return registro

    return None
