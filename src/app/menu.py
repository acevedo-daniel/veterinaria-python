from src.app.datos import (propietarios, mascotas, turnos, atenciones)
from src.features.propietario.presentacion import (
    mostrar_propietarios,
    registrar_propietario,
)
from src.features.mascota.presentacion import (
    registrar_mascota,
    mostrar_mascotas,
    consultar_mascota
)
from src.features.turno.presentacion import (
    asignar_turno,
    mostrar_turnos,
    cancelar_turno
)
from src.features.atencion.presentacion import (
    atender_turno,
    mostrar_atenciones,
)
from src.servicios_veterinarios.datos import servicios
from src.shared.formato import (
    mostrar_info,
    mostrar_opciones,
    mostrar_separador,
    mostrar_titulo,
)
from src.shared.validacion import leer_opcion
from src.features.estadistica.presentacion import mostrar_estadisticas
from src.shared.persistencia import guardar_datos


OPCIONES_MENU = [
    "Registrar propietario",
    "Registrar mascota",
    "Mostrar propietarios",
    "Mostrar mascotas",
    "Consultar mascota",
    "Asignar turno",
    "Mostrar turnos",
    "Atender turno",
    "Cancelar turno",
    "Mostrar atenciones",
    "Mostrar estadísticas",
]


def mostrar_menu(titulo: str, opciones: list[str]) -> None:
    mostrar_titulo(titulo)
    mostrar_opciones(opciones)
    mostrar_info("0. Salir")


def ejecutar_menu() -> None:
    opciones_validas = [str(numero) for numero in range(len(OPCIONES_MENU) + 1)]

    while True:
        mostrar_menu("Veterinaria", OPCIONES_MENU)
        opcion = leer_opcion("Seleccione una opcion: ", opciones_validas)

        if opcion == "1":
            registrar_propietario(propietarios)
            guardar_datos(propietarios, mascotas, turnos, atenciones)
        elif opcion == "2":
            registrar_mascota(propietarios, mascotas)
            guardar_datos(propietarios, mascotas, turnos, atenciones)
        elif opcion == "3":
            mostrar_propietarios(propietarios)
        elif opcion == "4":
            mostrar_mascotas(mascotas, propietarios)
        elif opcion == "5":
            consultar_mascota(mascotas, propietarios)
        elif opcion == "6":
            asignar_turno(propietarios, mascotas, turnos)
            guardar_datos(propietarios, mascotas, turnos, atenciones)
        elif opcion == "7":
            mostrar_turnos(turnos, mascotas)
        elif opcion == "8":
            atender_turno(turnos, mascotas, servicios, atenciones)
            guardar_datos(propietarios, mascotas, turnos, atenciones)
        elif opcion == "9":
            cancelar_turno(turnos, mascotas)
            guardar_datos(propietarios, mascotas, turnos, atenciones)
        elif opcion == "10":
            mostrar_atenciones(atenciones, turnos, mascotas, servicios)
        elif opcion == "11":
            mostrar_estadisticas(propietarios, mascotas, turnos, atenciones, servicios)
        elif opcion == "0":
            guardar_datos(propietarios, mascotas, turnos, atenciones)
            mostrar_info("Programa finalizado correctamente.")
            break
        else:
            mostrar_info("La funcionalidad todavia no fue implementada.")
            mostrar_separador()
