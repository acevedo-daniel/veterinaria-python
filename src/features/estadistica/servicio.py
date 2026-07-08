def contar_turnos_por_estado(turnos: list) -> dict:
    cantidades = {
        "Pendiente": 0,
        "Atendido": 0,
        "Cancelado": 0,
    }
    for turno in turnos:
        estado = turno["estado"]
        if estado in cantidades:
            cantidades[estado] += 1
    return cantidades


def contar_mascotas_por_especie(mascotas: list) -> dict:
    cantidades = {
        "Perro": 0,
        "Gato": 0,
        "Ave": 0,
        "Otra": 0,
    }
    for mascota in mascotas:
        especie = mascota["especie"]
        if especie in cantidades:
            cantidades[especie] += 1
        else:
            cantidades["Otra"] += 1
    return cantidades


def calcular_total_recaudado(atenciones: list) -> float:
    total = 0.0
    for atencion in atenciones:
        total += atencion["importe"]
    return total


def calcular_promedio_atenciones(atenciones: list) -> float:
    if len(atenciones) == 0:
        return 0.0
    total = calcular_total_recaudado(atenciones)
    return total / len(atenciones)


def obtener_servicio_mas_frecuente(atenciones: list, servicios: list) -> str | None:
    if len(atenciones) == 0:
        return None

    cantidades = {}

    for atencion in atenciones:
        id_servicio = atencion["id_servicio"]

        if id_servicio in cantidades:
            cantidades[id_servicio] += 1
        else:
            cantidades[id_servicio] = 1

    id_servicio_mas_frecuente = None
    mayor_cantidad = 0

    for id_servicio, cantidad in cantidades.items():
        if cantidad > mayor_cantidad:
            mayor_cantidad = cantidad
            id_servicio_mas_frecuente = id_servicio

    for servicio in servicios:
        if servicio["id"] == id_servicio_mas_frecuente:
            return servicio["nombre"]

    return "Servicio desconocido"