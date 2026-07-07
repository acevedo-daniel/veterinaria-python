def mostrar_titulo(titulo: str) -> None:
    print(f"\n{'=' * 10} {titulo} {'=' * 10}\n")


def mostrar_subtitulo(subtitulo: str) -> None:
    print(f"\n{'-' * 10} {subtitulo} {'-' * 10}\n")


def mostrar_opciones(opciones: list[str], inicio: int = 1) -> None:
    for indice, opcion in enumerate(opciones, start=inicio):
        print(f"{indice}. {opcion}")


def mostrar_info(mensaje: str) -> None:
    print(mensaje)


def mostrar_exito(mensaje: str) -> None:
    print(f"Exito: {mensaje}")


def mostrar_error(mensaje: str) -> None:
    print(f"Error: {mensaje}")


def mostrar_separador() -> None:
    print(f"\n{'-' * 30}\n")
