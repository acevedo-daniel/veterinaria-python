from datetime import datetime

from src.shared.formato import mostrar_error


def leer_opcion(mensaje: str, opciones: list[str]) -> str:
    while True:
        opcion = input(mensaje).strip()

        if opcion in opciones:
            return opcion

        mostrar_error(f"Ingrese una opcion valida: {', '.join(opciones)}")


def leer_texto(mensaje: str) -> str:
    while True:
        texto = input(mensaje).strip()

        if texto:
            return texto

        mostrar_error("El campo no puede quedar vacio.")


def leer_numero(mensaje: str) -> str:
    while True:
        texto = input(mensaje).strip()

        if texto.isdigit():
            return texto

        mostrar_error("Debe ingresar solamente numeros.")


def leer_numero_negativo(mensaje: str) -> int:
    while True:
        texto = input(mensaje).strip()

        if texto.isdigit() and int(texto) >= 0:
            return int(texto)

        mostrar_error("Debe ingresar un numero positivo o cero.")


def leer_fecha(mensaje: str) -> str:
    while True:
        fecha_texto = input(mensaje).strip()

        try:
            fecha = datetime.strptime(fecha_texto, "%d/%m/%Y")

            if fecha.date() < datetime.now().date():
                mostrar_error("La fecha no puede ser anterior a hoy.")
                continue

            return fecha_texto
        except ValueError:
            mostrar_error("El formato de fecha debe ser dd/mm/yyyy.")


def leer_hora(mensaje: str) -> str:
    while True:
        hora_texto = input(mensaje).strip()

        try:
            hora = datetime.strptime(hora_texto, "%H:%M")

            if hora.hour < 8 or hora.hour >= 20:
                mostrar_error("La hora debe estar entre 08:00 y 20:00.")
                continue

            return hora_texto
        except ValueError:
            mostrar_error("El formato de hora debe ser HH:MM (24 horas).")


def confirmar(mensaje: str) -> bool:
    while True:
        respuesta = input(f"{mensaje} (s/n): ").strip().lower()

        if respuesta in ["s", "n"]:
            return respuesta == "s"

        mostrar_error("Debe ingresar 's' para si o 'n' para no.")

def leer_dni(mensaje: str) -> str:
    while True:
        dni = input(mensaje).strip()

        if not dni.isdigit():
            print("Error: el DNI debe contener solo números.")
        elif len(dni) != 8:
            print("Error: el DNI debe tener exactamente 8 dígitos.")
        else:
            return dni