import json
from pathlib import Path


RUTA_DATOS = Path(__file__).resolve().parents[2] / "data" / "datos.json"


def cargar_datos() -> tuple[list, list, list, list]:
    if not RUTA_DATOS.exists():
        return [], [], [], []

    try:
        with open(RUTA_DATOS, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

        propietarios = datos.get("propietarios", [])
        mascotas = datos.get("mascotas", [])
        turnos = datos.get("turnos", [])
        atenciones = datos.get("atenciones", [])

        return propietarios, mascotas, turnos, atenciones

    except json.JSONDecodeError:
        print("Error: el archivo de datos está dañado. Se iniciará con datos vacíos.")
        return [], [], [], []


def guardar_datos(
    propietarios: list,
    mascotas: list,
    turnos: list,
    atenciones: list,
) -> None:
    RUTA_DATOS.parent.mkdir(parents=True, exist_ok=True)

    datos = {
        "propietarios": propietarios,
        "mascotas": mascotas,
        "turnos": turnos,
        "atenciones": atenciones,
    }

    with open(RUTA_DATOS, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)