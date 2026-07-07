def buscar_por_id(registros: list[dict], id_buscado: int) -> dict | None:
    for registro in registros:
        if registro["id"] == id_buscado:
            return registro

    return None
