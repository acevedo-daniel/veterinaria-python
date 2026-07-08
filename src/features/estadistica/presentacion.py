from shared.formato import mostrar_titulo
from features.estadistica.servicio import (
    contar_turnos_por_estado,
    contar_mascotas_por_especie,
    calcular_total_recaudado,
    calcular_promedio_atenciones,
    obtener_servicio_mas_frecuente,
)


def mostrar_estadisticas(
    propietarios: list,
    mascotas: list,
    turnos: list,
    atenciones: list,
) -> None:
    mostrar_titulo("Estadísticas")

    turnos_por_estado = contar_turnos_por_estado(turnos)
    mascotas_por_especie = contar_mascotas_por_especie(mascotas)
    total = calcular_total_recaudado(atenciones)
    promedio = calcular_promedio_atenciones(atenciones)
    servicio_frecuente = obtener_servicio_mas_frecuente(atenciones)

    print(f"Propietarios: {len(propietarios)}")
    print(f"Mascotas: {len(mascotas)}")
    print(f"Turnos: {len(turnos)}")
    print(f"Atenciones: {len(atenciones)}")

    print("\nTurnos por estado:")
    print(f"Pendientes: {turnos_por_estado['Pendiente']}")
    print(f"Atendidos: {turnos_por_estado['Atendido']}")
    print(f"Cancelados: {turnos_por_estado['Cancelado']}")

    print("\nMascotas por especie:")
    print(f"Perros: {mascotas_por_especie['Perro']}")
    print(f"Gatos: {mascotas_por_especie['Gato']}")
    print(f"Aves: {mascotas_por_especie['Ave']}")
    print(f"Otras: {mascotas_por_especie['Otra']}")

    print(f"\nTotal recaudado: ${total:.2f}")
    print(f"Promedio por atención: ${promedio:.2f}")

    if servicio_frecuente is None:
        print("Servicio más frecuente: sin datos")
    else:
        print(f"Servicio más frecuente: {servicio_frecuente}")
