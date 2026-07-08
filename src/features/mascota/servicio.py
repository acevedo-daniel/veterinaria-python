from src.shared.identificador import generar_id

def buscar_mascota(mascotas: list[dict], nombre: str, id_propetario: int) -> dict | None:
    for mascota in mascotas:
        if mascota["nombre"].lower() == nombre.lower() and mascota["id_propetario"] == id_propetario:
            return mascota
    return None

def crear_mascota(
    mascotas: list[dict],
    nombre: str,
    especie: str,
    raza: str,
    edad: int,
    id_propetario: int,
) -> dict | None:

    if buscar_mascota(mascotas, nombre, id_propetario):
        return None

    mascota = {
        "id": generar_id(mascotas),
        "nombre": nombre,
        "especie": especie,
        "raza": raza,
        "edad": edad,
        "id_propetario": id_propetario
    }
    mascotas.append(mascota)
    return mascota
