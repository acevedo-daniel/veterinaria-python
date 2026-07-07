def mostrar_titulo(titulo: str) -> None:
    print(f"\n{'=' * 10} {titulo} {'=' * 10}\n")


def mostrar_subtitulo(subtitulo: str) -> None:
    print(f"\n{'-' * 10} {subtitulo} {'-' * 10}\n")


def mostrar_opciones(opciones: list[str], inicio: int = 1) -> None:
    for indice, opcion in enumerate(opciones, start=inicio):
        print(f"{indice}. {opcion}")


def mostrar_separador() -> None:
    print(f"\n{'-' * 30}\n")
