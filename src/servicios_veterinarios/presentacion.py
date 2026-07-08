from src.shared.formato import mostrar_info, mostrar_separador, mostrar_titulo


def mostrar_servicios(servicios: list[dict]) -> None:
    mostrar_titulo("Lista de Servicios Veterinarios")

    if not servicios:
        mostrar_info("No hay servicios veterinarios registrados.")
    else:
        for servicio in servicios:
            mostrar_info(
                f"ID: {servicio['id']}, "
                f"Nombre: {servicio['nombre']}, "
                f"Precio: ${servicio['precio']}"
            )

    mostrar_separador()
