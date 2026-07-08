# Sistema de Gestion Veterinaria

<div align="center">

# Trabajo Final Integrador

## Sistema de Gestion Veterinaria en Python

Aplicacion de consola para administrar propietarios, mascotas, turnos,
servicios veterinarios y atenciones.

---

**Institucion:** ..................................................

**Materia:** ......................................................

**Docente:** ......................................................

**Curso / Comision:** ..............................................

**Fecha de entrega:** ..............................................

---

## Integrantes

| Apellido y nombre | Rol / observaciones |
| --- | --- |
| .................................................. | .................................................. |
| .................................................. | .................................................. |
| .................................................. | .................................................. |
| .................................................. | .................................................. |

</div>

---

## Descripcion

Este proyecto implementa un sistema basico de gestion para una veterinaria.
La aplicacion se ejecuta desde consola y permite registrar informacion central
del negocio: propietarios, mascotas, turnos, servicios disponibles y atenciones
realizadas.

El objetivo principal del proyecto es practicar programacion modular en Python,
separando responsabilidades entre presentacion, logica de servicio, validaciones
y datos compartidos.

---

## Estado actual

El sistema cuenta actualmente con las siguientes funcionalidades implementadas:

- Registro de propietarios.
- Listado de propietarios.
- Registro de mascotas asociadas a propietarios.
- Listado de mascotas.
- Consulta de mascota por ID.
- Asignacion de turnos.
- Listado de turnos.
- Cancelacion de turnos pendientes.
- Listado de servicios veterinarios disponibles.
- Atención de turnos pendientes.
- Registro de atenciones realizadas.
- Listado de atenciones.

Funcionalidades presentes en el menu pero pendientes de implementacion:

- Mostrar estadisticas.

---

## Como ejecutar el proyecto

Desde la carpeta raiz del proyecto:

```bash
python main.py
```

Requisitos:

- Python 3 instalado.
- Ejecutar el comando desde la raiz del proyecto, donde se encuentra `main.py`.

---

## Estructura del proyecto

```text
veterinaria-python/
|-- main.py
|-- README.md
|-- src/
    |-- app/
    |   |-- datos.py
    |   |-- menu.py
    |
    |-- features/
    |   |-- propietario/
    |   |   |-- presentacion.py
    |   |   |-- servicio.py
    |   |
    |   |-- mascota/
    |   |   |-- presentacion.py
    |   |   |-- servicio.py
    |   |
    |   |-- turno/
    |   |   |-- presentacion.py
    |   |   |-- servicio.py
    |   |
    |   |-- atencion/
    |       |-- presentacion.py
    |       |-- servicio.py
    |
    |-- servicios_veterinarios/
    |   |-- datos.py
    |   |-- presentacion.py
    |
    |-- shared/
        |-- busqueda.py
        |-- formato.py
        |-- identificador.py
        |-- validacion.py
```

---

## Organizacion interna

El proyecto esta dividido por responsabilidades:

| Carpeta / archivo | Responsabilidad |
| --- | --- |
| `main.py` | Punto de entrada de la aplicacion. |
| `src/app/menu.py` | Menu principal y navegacion entre opciones. |
| `src/app/datos.py` | Listas en memoria usadas por el sistema. |
| `src/features/*/presentacion.py` | Entrada y salida por consola de cada funcionalidad. |
| `src/features/*/servicio.py` | Reglas de negocio y operaciones sobre los datos. |
| `src/shared/formato.py` | Funciones comunes para mostrar titulos, mensajes y separadores. |
| `src/shared/validacion.py` | Funciones para validar datos ingresados por el usuario. |
| `src/shared/busqueda.py` | Busqueda generica por ID. |
| `src/shared/identificador.py` | Generacion de IDs incrementales. |
| `src/servicios_veterinarios/` | Servicios disponibles y su visualizacion. |

---

## Flujo principal de uso

Un flujo habitual dentro del sistema es:

1. Registrar un propietario.
2. Registrar una mascota asociada a ese propietario.
3. Asignar un turno a la mascota.
4. Atender el turno seleccionando un servicio veterinario.
5. Consultar el listado de atenciones.

---

## Datos que administra el sistema

### Propietarios

Cada propietario contiene:

- ID.
- DNI.
- Nombre.
- Telefono.

### Mascotas

Cada mascota contiene:

- ID.
- Nombre.
- Especie.
- Raza.
- Edad.
- ID del propietario.

### Turnos

Cada turno contiene:

- ID.
- ID de mascota.
- Fecha.
- Hora.
- Nota.
- Estado.

Estados posibles:

- `Pendiente`
- `Cancelado`
- `Atendido`

### Atenciones

Cada atención contiene:

- ID.
- ID del turno.
- ID del servicio.
- Diagnóstico.
- Observaciones.
- Importe.

---

## Decisiones de diseno

- La aplicacion usa listas en memoria para guardar los datos durante la ejecucion.
- Cada modulo separa la presentacion de la logica de negocio.
- Los mensajes de consola se centralizan en `src/shared/formato.py`.
- Las validaciones de entrada se centralizan en `src/shared/validacion.py`.
- Los IDs se generan de forma incremental.
- Se utilizan diccionarios para representar registros simples.

---

## Limitaciones actuales

- Los datos no se guardan en archivos ni base de datos.
- Al cerrar el programa, la informacion cargada se pierde.
- La opcion de estadisticas todavia no esta implementada.
- No hay sistema de usuarios ni permisos.
- No hay interfaz grafica; la aplicacion funciona por consola.

---

## Verificacion rapida

Para comprobar que los archivos Python compilan correctamente:

```bash
python -m compileall src
```

---

## Estado del proyecto

Proyecto en desarrollo.

Version actual orientada a consola, con funcionalidades principales de gestion
veterinaria ya implementadas y una estructura preparada para seguir agregando
modulos.
