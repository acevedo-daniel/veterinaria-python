# Sistema de Gestión Veterinaria

<div align="center">

# Trabajo Final Integrador

## Sistema de Gestión Veterinaria en Python

Aplicación de consola e interfaz gráfica para administrar propietarios, mascotas, turnos,
servicios veterinarios, atenciones, historial clínico, vacunas, controles, alertas y estadísticas.

---

**Institución:** ..................................................

**Materia:** ......................................................

**Docente:** ......................................................

**Curso / Comisión:** ..............................................

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

## Descripción

Este proyecto implementa un sistema básico de gestión para una veterinaria.
La aplicación permite registrar información central del negocio: propietarios,
mascotas, turnos, servicios disponibles, atenciones, historial clínico, vacunas,
controles próximos y estadísticas generales.

El objetivo principal del proyecto es practicar programación modular en Python,
separando responsabilidades entre presentación, lógica de servicio, validaciones,
persistencia de datos y datos compartidos.

---

## Estado actual

El sistema cuenta actualmente con las siguientes funcionalidades implementadas:

- Registro de propietarios.
- Listado de propietarios.
- Registro de mascotas asociadas a propietarios.
- Listado de mascotas.
- Consulta de mascota por ID.
- Asignación de turnos.
- Listado de turnos.
- Cancelación de turnos pendientes.
- Listado de servicios veterinarios disponibles.
- Atención de turnos pendientes.
- Registro de atenciones realizadas.
- Listado de atenciones.
- Estadísticas generales del sistema.
- Guardado y carga de datos mediante archivo JSON.
- Historial clínico por mascota.
- Registro de vacunas y controles próximos.
- Listado de vacunas y controles registrados.
- Alertas de vacunas y controles vencidos, para hoy o próximos.

---

## Cómo ejecutar el proyecto

El proyecto puede ejecutarse de dos formas: desde consola o mediante interfaz gráfica.

### Ejecución por consola

Desde la carpeta raíz del proyecto:

```bash
python main.py
```

### Ejecución con interfaz gráfica

Desde la carpeta raíz del proyecto:

```bash
python gui.py
```

### Requisitos

- Python 3 instalado.
- Ejecutar los comandos desde la raíz del proyecto, donde se encuentran `main.py` y `gui.py`.
- La interfaz gráfica utiliza Tkinter, librería incluida por defecto en Python.

---

## Persistencia de datos

El sistema guarda la información cargada en un archivo JSON.

Archivo utilizado:

```text
data/datos.json
```

Allí se almacenan los datos de:

- Propietarios.
- Mascotas.
- Turnos.
- Atenciones.
- Vacunas y controles próximos.

Gracias a esta funcionalidad, la información no se pierde al cerrar el programa.
Cuando el sistema vuelve a ejecutarse, carga automáticamente los datos guardados.

---

## Estructura del proyecto

```text
veterinaria-python/
├── main.py
├── gui.py
├── README.md
├── data/
│   └── datos.json
├── docs/
│   ├── README.md
│   └── documentacion-tecnica.md
└── src/
    ├── app/
    │   ├── __init__.py
    │   ├── datos.py
    │   └── menu.py
    ├── features/
    │   ├── propietario/
    │   │   ├── presentacion.py
    │   │   └── servicio.py
    │   ├── mascota/
    │   │   ├── presentacion.py
    │   │   └── servicio.py
    │   ├── turno/
    │   │   ├── presentacion.py
    │   │   └── servicio.py
    │   ├── atencion/
    │   │   ├── presentacion.py
    │   │   └── servicio.py
    │   ├── estadistica/
    │   │   ├── presentacion.py
    │   │   └── servicio.py
    │   ├── historial/
    │   │   └── presentacion.py
    │   └── seguimiento/
    │       ├── presentacion.py
    │       └── servicio.py
    ├── servicios_veterinarios/
    │   ├── datos.py
    │   └── presentacion.py
    └── shared/
        ├── busqueda.py
        ├── formato.py
        ├── identificador.py
        ├── persistencia.py
        └── validacion.py
```

---

## Organización interna

El proyecto está dividido por responsabilidades:

| Carpeta / archivo | Responsabilidad |
| --- | --- |
| `main.py` | Punto de entrada de la aplicación por consola. |
| `gui.py` | Interfaz gráfica del sistema desarrollada con Tkinter. |
| `src/app/menu.py` | Menú principal y navegación entre opciones. |
| `src/app/datos.py` | Carga inicial de las listas utilizadas por el sistema. |
| `src/features/*/presentacion.py` | Entrada y salida por consola de cada funcionalidad. |
| `src/features/*/servicio.py` | Reglas de negocio y operaciones sobre los datos. |
| `src/features/estadistica/` | Cálculo y presentación de estadísticas generales. |
| `src/features/historial/` | Consulta del historial clínico de cada mascota. |
| `src/features/seguimiento/` | Registro de vacunas, controles y alertas. |
| `src/shared/formato.py` | Funciones comunes para mostrar títulos, mensajes y separadores. |
| `src/shared/validacion.py` | Funciones para validar datos ingresados por el usuario. |
| `src/shared/busqueda.py` | Búsqueda genérica por ID. |
| `src/shared/identificador.py` | Generación de IDs incrementales. |
| `src/shared/persistencia.py` | Carga y guardado de datos en archivo JSON. |
| `src/servicios_veterinarios/` | Servicios disponibles y su visualización. |

---

## Flujo principal de uso

Un flujo habitual dentro del sistema es:

1. Registrar un propietario.
2. Registrar una mascota asociada a ese propietario.
3. Asignar un turno a la mascota.
4. Atender el turno seleccionando un servicio veterinario.
5. Registrar diagnóstico, observaciones e importe.
6. Consultar el listado de atenciones.
7. Consultar el historial clínico de la mascota.
8. Registrar una vacuna o control próximo.
9. Ver alertas de vacunas o controles próximos.
10. Consultar estadísticas generales.

---

## Interfaz gráfica

El sistema cuenta con una interfaz gráfica desarrollada con Tkinter.

Esta interfaz permite utilizar las funcionalidades principales del sistema de una manera más visual, ordenada y amigable para el usuario.

Desde la interfaz gráfica se puede:

- Registrar propietarios.
- Registrar mascotas.
- Asignar turnos.
- Cancelar turnos pendientes.
- Atender turnos.
- Registrar vacunas y controles.
- Visualizar alertas de seguimientos próximos o vencidos.
- Consultar estadísticas generales.
- Ver listados mediante tablas.

La interfaz incluye un panel de inicio con tarjetas de resumen, secciones diferenciadas por funcionalidad y tablas para organizar mejor la información cargada.

---

## Datos que administra el sistema

### Propietarios

Cada propietario contiene:

- ID.
- DNI.
- Nombre.
- Teléfono.

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

### Vacunas y controles

Cada seguimiento contiene:

- ID.
- ID de mascota.
- Tipo de seguimiento.
- Descripción.
- Fecha de registro o aplicación.
- Próxima fecha.
- Observaciones.
- Estado.

Tipos posibles:

- Vacuna.
- Control.

---

## Alertas de vacunas y controles

El sistema cuenta con una funcionalidad de alertas para vacunas y controles próximos.

Las alertas permiten identificar:

- Vacunas o controles vencidos.
- Vacunas o controles programados para el día actual.
- Vacunas o controles próximos.

Esta funcionalidad ayuda a realizar un seguimiento más ordenado de la atención veterinaria de cada mascota.

---

## Decisiones de diseño

- La aplicación está organizada de forma modular.
- Cada módulo separa la presentación de la lógica de negocio.
- Los mensajes de consola se centralizan en `src/shared/formato.py`.
- Las validaciones de entrada se centralizan en `src/shared/validacion.py`.
- Los IDs se generan de forma incremental.
- Se utilizan diccionarios para representar registros simples.
- Se utilizan listas para administrar propietarios, mascotas, turnos, atenciones y seguimientos.
- Los datos se guardan y cargan mediante un archivo JSON.
- La persistencia de datos se centraliza en `src/shared/persistencia.py`.
- Las atenciones modifican automáticamente el estado del turno a `Atendido`.
- Las vacunas y controles permiten generar alertas según la próxima fecha registrada.
- Se mantiene una versión por consola mediante `main.py`.
- Se incorpora una interfaz gráfica mediante `gui.py`.
- La interfaz gráfica utiliza Tkinter para evitar dependencias externas.
- La interfaz gráfica reutiliza los mismos datos persistidos en `data/datos.json`.
- El diseño visual utiliza secciones, pestañas, tablas y tarjetas de resumen para facilitar el uso del sistema.

---

## Limitaciones actuales

- No hay sistema de usuarios ni permisos.
- No se utiliza una base de datos externa.
- El sistema no envía notificaciones reales por correo o teléfono; las alertas se muestran dentro de la aplicación.
- La interfaz gráfica es local y de escritorio, no una aplicación web.
- No posee edición o eliminación completa de todos los registros desde la interfaz gráfica.

---

## Verificación rápida

Para comprobar que los archivos Python compilan correctamente:

```bash
python -m compileall src
```

---

## Estado del proyecto

Proyecto en desarrollo.

Versión actual con funcionamiento por consola e interfaz gráfica, persistencia de datos en JSON, estadísticas, historial clínico, seguimiento de vacunas y controles, y sistema de alertas.

La aplicación permite administrar la información principal de una veterinaria desde consola o desde una interfaz gráfica local desarrollada con Tkinter.
