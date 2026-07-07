from src.shared.busqueda import buscar_por_id
from src.shared.formato import (
mostrar_opciones,
mostrar_subtitulo,
mostrar_titulo,
mostrar_separador
)
from src.shared.validacion import (
  leer_numero,
  leer_numero_negativo,
  leer_opcion,
  leer_texto
)
from src.features.propietario.presentacion import (
  mostrar_propietarios
)
from src.features.mascotas.servicio import (
  buscar_mascota,
  crear_mascota
)

def registrar_mascota(propetarios : list, mascotas : list) -> None:
    mostrar_titulo("Registrar Mascota")

    if not propetarios:
        print("No hay propietarios registrados. Por favor, registre un propietario primero.")
        mostrar_separador()
        return

    mostrar_propietarios(propetarios)

    id_propetario = int(leer_numero("Ingrese el ID del propietario de la mascota: "))
    propietario = buscar_por_id(propetarios, id_propetario)

    if not propietario:
        print(f"Error: No se encontró un propietario con el ID {id_propetario}.")
        mostrar_separador()
        return

    nombre = leer_texto("Ingrese el nombre de la mascota: ")

    mostrar_subtitulo("Especies")
    mostrar_opciones(["Perro", "Gato", "Ave", "Otra"])

    opcion_especie = leer_opcion(
    "Ingrese el número correspondiente a la especie de la mascota: ",
    ["1", "2", "3", "4"]
    )
    especies = {
    "1": "Perro",
    "2": "Gato",
    "3": "Ave",
    "4": "Otra"
    }
    especie = especies[opcion_especie]

    raza = leer_texto("Ingrese la raza de la mascota: ")
    edad = leer_numero_negativo("Ingrese la edad de la mascota (en años): ")

    mascota = crear_mascota(mascotas, nombre, especie, raza, edad, id_propetario)

    if mascota:
        print(f"Mascota registrada con éxito: {mascota}")
    else:
        print(f"Error: Ya existe una mascota con el nombre '{nombre}' para el propietario con ID {id_propetario}.")
        print(f"Mascota existente: {buscar_mascota(mascotas, nombre, id_propetario)}")

    mostrar_separador()

def mostrar_mascotas(mascotas: list, propietarios: list) -> None:
        mostrar_titulo("Lista de Mascotas")

        if not mascotas:
            print("No hay mascotas registradas.")
        else:
            for mascota in mascotas:
                propietario = buscar_por_id(propietarios, mascota["id_propetario"])
                nombre_propietario = propietario["nombre"] if propietario else "Desconocido"
                print(
                    f"ID: {mascota['id']}, "
                    f"Nombre: {mascota['nombre']}, "
                    f"Especie: {mascota['especie']}, "
                    f"Raza: {mascota['raza']}, "
                    f"Edad: {mascota['edad']} años, "
                    f"Propietario: {nombre_propietario}"
                )

        mostrar_separador()

def consultar_mascota(mascotas: list, propietarios: list) -> None:
    mostrar_titulo("Consultar Mascota")

    if not mascotas:
        print("No hay mascotas registradas.")
        mostrar_separador()
        return

    id_mascota = int(leer_numero("Ingrese el ID de la mascota a consultar: "))
    mascota = buscar_por_id(mascotas, id_mascota)

    if not mascota:
        print(f"Error: No se encontró una mascota con el ID {id_mascota}.")
    else:
        propietario = buscar_por_id(propietarios, mascota["id_propetario"])
        nombre_propietario = propietario["nombre"] if propietario else "Desconocido"
        print(
            f"ID: {mascota['id']}, "
            f"Nombre: {mascota['nombre']}, "
            f"Especie: {mascota['especie']}, "
            f"Raza: {mascota['raza']}, "
            f"Edad: {mascota['edad']} años, "
            f"Propietario: {nombre_propietario}"
        )

    mostrar_separador()
