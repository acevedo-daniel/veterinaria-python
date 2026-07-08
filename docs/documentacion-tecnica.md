# Documentación técnica

## Sistema de Gestión Veterinaria

Documento técnico del proyecto **Sistema de Gestión Veterinaria en Python**.  
Su objetivo es explicar cómo está organizada la aplicación, cómo se ejecuta, qué datos administra y cuál es el flujo principal de funcionamiento.

---

## 1. Resumen

El sistema permite administrar la información básica de una veterinaria:

- Propietarios.
- Mascotas.
- Turnos.
- Atenciones veterinarias.
- Servicios disponibles.
- Historial clínico.
- Vacunas y controles próximos.
- Alertas.
- Estadísticas generales.

La aplicación puede utilizarse de dos formas:

- **Consola**, mediante `main.py`.
- **Interfaz gráfica**, mediante `gui.py`.

Ambas versiones trabajan sobre el mismo archivo de datos: `data/datos.json`.

---

## 2. Tecnologías utilizadas

| Tecnología | Uso |
| --- | --- |
| Python 3 | Lenguaje principal del proyecto |
| Tkinter | Interfaz gráfica de escritorio |
| JSON | Persistencia local de datos |
| Módulos propios | Separación de presentación, lógica, validación y persistencia |

El proyecto no requiere dependencias externas.

---

## 3. Estructura del proyecto

```text
veterinaria-python/
├── main.py
├── gui.py
├── README.md
├── data/
│   └── datos.json
├── docs/
│   └── documentacion-tecnica.md
└── src/
    ├── app/
    ├── features/
    ├── servicios_veterinarios/
    └── shared/
```

### Archivos principales

| Archivo | Responsabilidad |
| --- | --- |
| `main.py` | Punto de entrada de la aplicación por consola |
| `gui.py` | Interfaz gráfica desarrollada con Tkinter |
| `data/datos.json` | Archivo de persistencia local |
| `src/app/menu.py` | Menú principal y navegación por consola |
| `src/app/datos.py` | Carga inicial de datos compartidos |

---

## 4. Arquitectura general

El proyecto está organizado por responsabilidades. Cada funcionalidad se divide en módulos de presentación y módulos de servicio.

```text
Entrada de usuario
      │
      ├── Consola: main.py → src/app/menu.py
      │
      └── GUI: gui.py
              │
              ▼
       Funcionalidades
              │
              ├── Propietarios
              ├── Mascotas
              ├── Turnos
              ├── Atenciones
              ├── Historial
              ├── Seguimientos
              └── Estadísticas
              │
              ▼
       Datos en memoria
              │
              ▼
       data/datos.json
```

### Capas del sistema

| Capa | Ubicación | Descripción |
| --- | --- | --- |
| Entrada | `main.py`, `gui.py` | Inicia la aplicación |
| Presentación | `src/features/*/presentacion.py` | Muestra información y solicita datos al usuario |
| Servicio | `src/features/*/servicio.py` | Contiene reglas de negocio |
| Compartida | `src/shared/` | Validaciones, búsquedas, formato, IDs y persistencia |
| Datos | `data/datos.json` | Guarda la información cargada |

---

## 5. Módulos funcionales

### Propietarios

Permite registrar y listar propietarios.

Datos principales:

- `id`
- `dni`
- `nombre`
- `telefono`

Reglas destacadas:

- El DNI debe tener 8 dígitos.
- No se permite registrar dos propietarios con el mismo DNI.

Archivos:

- `src/features/propietario/presentacion.py`
- `src/features/propietario/servicio.py`

---

### Mascotas

Permite registrar, listar y consultar mascotas asociadas a propietarios.

Datos principales:

- `id`
- `nombre`
- `especie`
- `raza`
- `edad`
- `id_propetario`

Reglas destacadas:

- Una mascota debe estar asociada a un propietario existente.
- No se permite repetir el mismo nombre de mascota para el mismo propietario.

Archivos:

- `src/features/mascota/presentacion.py`
- `src/features/mascota/servicio.py`

---

### Turnos

Permite asignar, listar y cancelar turnos.

Datos principales:

- `id`
- `id_mascota`
- `fecha`
- `hora`
- `nota`
- `estado`

Estados posibles:

- `Pendiente`
- `Cancelado`
- `Atendido`

Reglas destacadas:

- No se puede asignar un turno si no existen mascotas registradas.
- No se permite ocupar el mismo horario con otro turno pendiente.
- Solo se pueden cancelar turnos pendientes.

Archivos:

- `src/features/turno/presentacion.py`
- `src/features/turno/servicio.py`

---

### Atenciones

Permite atender turnos pendientes y registrar el servicio realizado.

Datos principales:

- `id`
- `id_turno`
- `id_servicio`
- `diagnostico`
- `observaciones`
- `importe`

Reglas destacadas:

- Solo se pueden atender turnos pendientes.
- Al registrar una atención, el turno pasa a estado `Atendido`.
- El importe se toma del servicio veterinario seleccionado.

Archivos:

- `src/features/atencion/presentacion.py`
- `src/features/atencion/servicio.py`

---

### Servicios veterinarios

Los servicios disponibles están definidos en código.

Archivo:

- `src/servicios_veterinarios/datos.py`

Servicios actuales:

| ID | Servicio | Precio |
| --- | --- | --- |
| 1 | Consulta general | 12000.0 |
| 2 | Vacunacion | 15000.0 |
| 3 | Desparasitacion | 10000.0 |
| 4 | Control posoperatorio | 9000.0 |
| 5 | Curacion | 13000.0 |

---

### Historial clínico

Permite consultar las atenciones realizadas a una mascota.

El historial se arma relacionando:

- Mascota.
- Turnos.
- Atenciones.
- Servicios.

Archivo:

- `src/features/historial/presentacion.py`

---

### Seguimientos, vacunas y controles

Permite registrar vacunas o controles próximos.

Datos principales:

- `id`
- `id_mascota`
- `tipo`
- `descripcion`
- `fecha_registro`
- `proxima_fecha`
- `observaciones`
- `estado`

Tipos posibles:

- `Vacuna`
- `Control`

Archivos:

- `src/features/seguimiento/presentacion.py`
- `src/features/seguimiento/servicio.py`

---

### Alertas

El sistema calcula alertas según la próxima fecha de cada seguimiento.

Estados de alerta:

- `Vencido`
- `Para hoy`
- `Próximo`

Por defecto, se consideran próximos los seguimientos con vencimiento dentro de los siguientes 7 días.

---

### Estadísticas

Permite consultar indicadores generales del sistema:

- Cantidad de propietarios.
- Cantidad de mascotas.
- Cantidad de turnos.
- Cantidad de atenciones.
- Turnos por estado.
- Mascotas por especie.
- Total recaudado.
- Promedio por atención.
- Servicio más frecuente.

Archivos:

- `src/features/estadistica/presentacion.py`
- `src/features/estadistica/servicio.py`

---

## 6. Persistencia de datos

La persistencia se realiza en el archivo:

```text
data/datos.json
```

El módulo responsable es:

```text
src/shared/persistencia.py
```

### Estructura esperada del archivo

```json
{
  "propietarios": [],
  "mascotas": [],
  "turnos": [],
  "atenciones": [],
  "seguimientos": []
}
```

### Consideración importante

El archivo `data/datos.json` debe contener JSON válido.  
Si el archivo existe pero está vacío o dañado, la aplicación inicia con listas vacías y muestra un mensaje de error de carga.

---

## 7. Flujo principal de uso

Un flujo típico de trabajo es:

1. Registrar un propietario.
2. Registrar una mascota asociada al propietario.
3. Asignar un turno a la mascota.
4. Atender el turno.
5. Seleccionar el servicio realizado.
6. Registrar diagnóstico y observaciones.
7. Consultar atenciones.
8. Consultar historial clínico.
9. Registrar una vacuna o control próximo.
10. Revisar alertas.
11. Consultar estadísticas.

---

## 8. Ejecución

### Ejecutar por consola

Desde la raíz del proyecto:

```bash
python main.py
```

### Ejecutar interfaz gráfica

Desde la raíz del proyecto:

```bash
python gui.py
```

La interfaz gráfica utiliza Tkinter, incluido por defecto en Python.

---

## 9. Validaciones principales

| Dato | Validación |
| --- | --- |
| DNI | Debe contener 8 dígitos |
| Texto | No puede estar vacío |
| Números | Deben contener solo dígitos |
| Edad | Debe ser positiva o cero |
| Fecha | Formato `dd/mm/yyyy` |
| Hora | Formato `HH:MM` |
| Turno | No debe superponerse con otro turno pendiente |

---

## 10. Verificación técnica

Para comprobar que los archivos Python compilan correctamente:

```bash
python -m compileall .
```

Para una prueba manual rápida:

1. Ejecutar `python gui.py`.
2. Registrar un propietario.
3. Registrar una mascota.
4. Asignar un turno.
5. Atender el turno.
6. Verificar que aparezca en atenciones e historial.

---

## 11. Decisiones de diseño

- Se utiliza una estructura modular para separar responsabilidades.
- La lógica de negocio está separada de la presentación en consola.
- La persistencia se centraliza en un único módulo.
- Los datos se almacenan en JSON para mantener simple el proyecto.
- Los IDs se generan de forma incremental según los registros existentes.
- La GUI reutiliza los mismos datos que la versión por consola.
- No se utiliza base de datos externa para reducir complejidad de instalación.

---

## 12. Limitaciones actuales

- No existe sistema de usuarios o permisos.
- No hay base de datos relacional.
- No se envían notificaciones reales.
- La GUI es local y de escritorio.
- Algunas operaciones de edición y eliminación completa no están implementadas.
- Los servicios veterinarios están definidos en código y no se administran desde la interfaz.

---

## 13. Glosario

| Término | Significado |
| --- | --- |
| Propietario | Persona responsable de una mascota |
| Mascota | Animal registrado en el sistema |
| Turno | Reserva de atención para una mascota |
| Atención | Registro de un servicio realizado |
| Seguimiento | Vacuna o control programado |
| Alerta | Aviso generado por una fecha próxima o vencida |

---

## 14. Mantenimiento recomendado

Para mantener el proyecto ordenado:

- Conservar la separación entre presentación y servicios.
- Agregar nuevas reglas de negocio en módulos `servicio.py`.
- Evitar duplicar validaciones si ya existen en `src/shared/validacion.py`.
- Mantener `data/datos.json` con JSON válido.
- Ejecutar `python -m compileall .` después de cambios importantes.
- Documentar nuevas funcionalidades en este archivo.
