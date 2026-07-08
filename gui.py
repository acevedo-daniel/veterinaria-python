import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, date

from src.app.datos import propietarios, mascotas, turnos, atenciones, seguimientos
from src.servicios_veterinarios.datos import servicios
from src.shared.identificador import generar_id
from src.shared.persistencia import guardar_datos


COLOR_FONDO = "#F4FBF8"
COLOR_PANEL = "#FFFFFF"
COLOR_PRIMARIO = "#2E8B57"
COLOR_PRIMARIO_OSCURO = "#246B45"
COLOR_SECUNDARIO = "#5DADE2"
COLOR_TEXTO = "#1F2933"
COLOR_TEXTO_SUAVE = "#6B7280"
COLOR_BORDE = "#DDE7E2"
COLOR_ALERTA = "#F59E0B"
COLOR_ERROR = "#DC2626"
COLOR_EXITO_SUAVE = "#E8F8EF"
COLOR_AZUL_SUAVE = "#EAF4FB"

FUENTE_TITULO = ("Segoe UI", 22, "bold")
FUENTE_SUBTITULO = ("Segoe UI", 14, "bold")
FUENTE_NORMAL = ("Segoe UI", 10)
FUENTE_CHICA = ("Segoe UI", 9)
FUENTE_CARD = ("Segoe UI", 20, "bold")


def buscar_por_id(lista, id_buscado):
    for elemento in lista:
        if elemento["id"] == id_buscado:
            return elemento
    return None


def guardar():
    guardar_datos(propietarios, mascotas, turnos, atenciones, seguimientos)


def obtener_id_combo(combo):
    valor = combo.get()

    if not valor:
        return None

    try:
        return int(valor.split(" - ")[0])
    except ValueError:
        return None


def convertir_fecha(fecha_texto):
    try:
        return datetime.strptime(fecha_texto, "%d/%m/%Y").date()
    except ValueError:
        return None


def validar_hora(hora_texto):
    try:
        datetime.strptime(hora_texto, "%H:%M")
        return True
    except ValueError:
        return False


class VeterinariaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión Veterinaria")
        self.root.geometry("1180x720")
        self.root.minsize(1050, 640)

        self.configurar_estilos()

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True, padx=8, pady=8)

        self.crear_tab_inicio()
        self.crear_tab_propietarios()
        self.crear_tab_mascotas()
        self.crear_tab_turnos()
        self.crear_tab_atenciones()
        self.crear_tab_seguimientos()
        self.crear_tab_estadisticas()

        self.refrescar_todo()

    def configurar_estilos(self):
        self.root.configure(bg=COLOR_FONDO)

        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "TNotebook",
            background=COLOR_FONDO,
            borderwidth=0,
        )

        style.configure(
            "TNotebook.Tab",
            font=("Segoe UI", 10, "bold"),
            padding=(18, 9),
            background="#E8F5EF",
            foreground=COLOR_TEXTO,
        )

        style.map(
            "TNotebook.Tab",
            background=[("selected", COLOR_PRIMARIO)],
            foreground=[("selected", "white")],
        )

        style.configure(
            "TFrame",
            background=COLOR_FONDO,
        )

        style.configure(
            "Card.TFrame",
            background=COLOR_PANEL,
            relief="solid",
            borderwidth=1,
        )

        style.configure(
            "Header.TFrame",
            background=COLOR_PRIMARIO,
        )

        style.configure(
            "TLabel",
            background=COLOR_FONDO,
            foreground=COLOR_TEXTO,
            font=FUENTE_NORMAL,
        )

        style.configure(
            "HeaderTitle.TLabel",
            background=COLOR_PRIMARIO,
            foreground="white",
            font=("Segoe UI", 21, "bold"),
        )

        style.configure(
            "HeaderSubtitle.TLabel",
            background=COLOR_PRIMARIO,
            foreground="#EAF7F0",
            font=("Segoe UI", 11),
        )

        style.configure(
            "SectionTitle.TLabel",
            background=COLOR_FONDO,
            foreground=COLOR_PRIMARIO_OSCURO,
            font=FUENTE_SUBTITULO,
        )

        style.configure(
            "Muted.TLabel",
            background=COLOR_FONDO,
            foreground=COLOR_TEXTO_SUAVE,
            font=FUENTE_NORMAL,
        )

        style.configure(
            "CardTitle.TLabel",
            background=COLOR_PANEL,
            foreground=COLOR_TEXTO_SUAVE,
            font=("Segoe UI", 10, "bold"),
        )

        style.configure(
            "CardValue.TLabel",
            background=COLOR_PANEL,
            foreground=COLOR_PRIMARIO,
            font=FUENTE_CARD,
        )

        style.configure(
            "CardMini.TLabel",
            background=COLOR_PANEL,
            foreground=COLOR_TEXTO_SUAVE,
            font=FUENTE_CHICA,
        )

        style.configure(
            "TLabelframe",
            background=COLOR_FONDO,
            bordercolor=COLOR_BORDE,
            relief="solid",
            borderwidth=1,
        )

        style.configure(
            "TLabelframe.Label",
            background=COLOR_FONDO,
            foreground=COLOR_PRIMARIO_OSCURO,
            font=("Segoe UI", 11, "bold"),
        )

        style.configure(
            "TEntry",
            padding=6,
            relief="flat",
        )

        style.configure(
            "TCombobox",
            padding=6,
        )

        style.configure(
            "TButton",
            font=("Segoe UI", 10, "bold"),
            padding=(13, 8),
            background=COLOR_PRIMARIO,
            foreground="white",
            borderwidth=0,
        )

        style.map(
            "TButton",
            background=[("active", COLOR_PRIMARIO_OSCURO)],
        )

        style.configure(
            "Secondary.TButton",
            font=("Segoe UI", 10, "bold"),
            padding=(13, 8),
            background=COLOR_SECUNDARIO,
            foreground="white",
            borderwidth=0,
        )

        style.map(
            "Secondary.TButton",
            background=[("active", "#337FB3")],
        )

        style.configure(
            "Danger.TButton",
            font=("Segoe UI", 10, "bold"),
            padding=(13, 8),
            background=COLOR_ERROR,
            foreground="white",
            borderwidth=0,
        )

        style.map(
            "Danger.TButton",
            background=[("active", "#991B1B")],
        )

        style.configure(
            "Treeview",
            background=COLOR_PANEL,
            foreground=COLOR_TEXTO,
            rowheight=30,
            fieldbackground=COLOR_PANEL,
            bordercolor=COLOR_BORDE,
            borderwidth=1,
            font=FUENTE_NORMAL,
        )

        style.configure(
            "Treeview.Heading",
            background="#DFF3EA",
            foreground=COLOR_PRIMARIO_OSCURO,
            font=("Segoe UI", 10, "bold"),
            padding=8,
        )

        style.map(
            "Treeview",
            background=[("selected", COLOR_PRIMARIO)],
            foreground=[("selected", "white")],
        )

    def crear_encabezado(self, contenedor, titulo, subtitulo):
        header = ttk.Frame(contenedor, style="Header.TFrame")
        header.pack(fill="x", padx=0, pady=(0, 16))

        ttk.Label(
            header,
            text=titulo,
            style="HeaderTitle.TLabel",
        ).pack(anchor="w", padx=22, pady=(16, 2))

        ttk.Label(
            header,
            text=subtitulo,
            style="HeaderSubtitle.TLabel",
        ).pack(anchor="w", padx=22, pady=(0, 16))

    def crear_titulo_seccion(self, contenedor, titulo, subtitulo=None):
        ttk.Label(
            contenedor,
            text=titulo,
            style="SectionTitle.TLabel",
        ).pack(anchor="w", padx=20, pady=(10, 3))

        if subtitulo:
            ttk.Label(
                contenedor,
                text=subtitulo,
                style="Muted.TLabel",
            ).pack(anchor="w", padx=20, pady=(0, 8))

    def crear_tarjeta(self, contenedor, titulo, valor, descripcion, fila, columna):
        tarjeta = ttk.Frame(contenedor, style="Card.TFrame")
        tarjeta.grid(row=fila, column=columna, padx=9, pady=9, sticky="nsew")

        lbl_titulo = ttk.Label(
            tarjeta,
            text=titulo,
            style="CardTitle.TLabel",
        )
        lbl_titulo.pack(anchor="w", padx=15, pady=(13, 0))

        lbl_valor = ttk.Label(
            tarjeta,
            text=valor,
            style="CardValue.TLabel",
        )
        lbl_valor.pack(anchor="w", padx=15, pady=(2, 0))

        lbl_descripcion = ttk.Label(
            tarjeta,
            text=descripcion,
            style="CardMini.TLabel",
        )
        lbl_descripcion.pack(anchor="w", padx=15, pady=(0, 13))

        return {
            "frame": tarjeta,
            "titulo": lbl_titulo,
            "valor": lbl_valor,
            "descripcion": lbl_descripcion,
        }

    def actualizar_tarjeta(self, tarjeta, valor):
        tarjeta["valor"].config(text=str(valor))

    def crear_tabla(self, contenedor, columnas, alto=10):
        frame_tabla = ttk.Frame(contenedor)
        frame_tabla.pack(fill="both", expand=True, padx=20, pady=(5, 16))

        nombres_columnas = []

        for columna, titulo, ancho in columnas:
            nombres_columnas.append(columna)

        tree = ttk.Treeview(
            frame_tabla,
            columns=nombres_columnas,
            show="headings",
            height=alto,
        )

        scrollbar_y = ttk.Scrollbar(frame_tabla, orient="vertical", command=tree.yview)
        scrollbar_x = ttk.Scrollbar(frame_tabla, orient="horizontal", command=tree.xview)

        tree.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

        tree.grid(row=0, column=0, sticky="nsew")
        scrollbar_y.grid(row=0, column=1, sticky="ns")
        scrollbar_x.grid(row=1, column=0, sticky="ew")

        frame_tabla.rowconfigure(0, weight=1)
        frame_tabla.columnconfigure(0, weight=1)

        for columna, titulo, ancho in columnas:
            tree.heading(columna, text=titulo)
            tree.column(columna, width=ancho, minwidth=80)

        return tree
    
    def limpiar_tree(self, tree):
        for item in tree.get_children():
            tree.delete(item)

    def crear_tab_inicio(self):
        self.tab_inicio = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_inicio, text="Inicio")

        self.crear_encabezado(
            self.tab_inicio,
            "🐾 Sistema de Gestión Veterinaria",
            "Panel general de control, alertas y resumen del estado actual de la veterinaria.",
        )

        self.crear_titulo_seccion(
            self.tab_inicio,
            "Resumen general",
            "Vista rápida de los datos principales cargados en el sistema.",
        )

        self.frame_cards_inicio = ttk.Frame(self.tab_inicio)
        self.frame_cards_inicio.pack(fill="x", padx=11, pady=4)

        for columna in range(5):
            self.frame_cards_inicio.columnconfigure(columna, weight=1)

        self.card_propietarios = self.crear_tarjeta(
            self.frame_cards_inicio,
            "Propietarios",
            "0",
            "Dueños registrados",
            0,
            0,
        )

        self.card_mascotas = self.crear_tarjeta(
            self.frame_cards_inicio,
            "Mascotas",
            "0",
            "Animales registrados",
            0,
            1,
        )

        self.card_turnos = self.crear_tarjeta(
            self.frame_cards_inicio,
            "Turnos",
            "0",
            "Turnos generados",
            0,
            2,
        )

        self.card_atenciones = self.crear_tarjeta(
            self.frame_cards_inicio,
            "Atenciones",
            "0",
            "Consultas realizadas",
            0,
            3,
        )

        self.card_seguimientos = self.crear_tarjeta(
            self.frame_cards_inicio,
            "Vacunas / controles",
            "0",
            "Seguimientos activos",
            0,
            4,
        )

        botonera = ttk.Frame(self.tab_inicio)
        botonera.pack(fill="x", padx=20, pady=(0, 4))

        ttk.Button(
            botonera,
            text="Actualizar panel",
            command=self.refrescar_todo,
            style="Secondary.TButton",
        ).pack(anchor="e")

        self.crear_titulo_seccion(
            self.tab_inicio,
            "Alertas importantes",
            "Vacunas y controles vencidos, para hoy o próximos dentro de los próximos 7 días.",
        )

        self.tree_alertas = self.crear_tabla(
            self.tab_inicio,
            [
                ("mascota", "Mascota", 160),
                ("tipo", "Tipo", 110),
                ("descripcion", "Descripción", 320),
                ("fecha", "Próxima fecha", 130),
                ("estado", "Estado", 230),
            ],
            alto=8,
        )

    def crear_tab_propietarios(self):
        self.tab_propietarios = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_propietarios, text="Propietarios")

        self.crear_encabezado(
            self.tab_propietarios,
            "👤 Propietarios",
            "Registro y administración de los dueños de las mascotas.",
        )

        frame_form = ttk.LabelFrame(self.tab_propietarios, text="Nuevo propietario")
        frame_form.pack(fill="x", padx=20, pady=(0, 12))

        ttk.Label(frame_form, text="DNI:").grid(row=0, column=0, padx=8, pady=10, sticky="w")
        self.entry_dni = ttk.Entry(frame_form, width=22)
        self.entry_dni.grid(row=0, column=1, padx=8, pady=10)

        ttk.Label(frame_form, text="Nombre:").grid(row=0, column=2, padx=8, pady=10, sticky="w")
        self.entry_nombre_propietario = ttk.Entry(frame_form, width=28)
        self.entry_nombre_propietario.grid(row=0, column=3, padx=8, pady=10)

        ttk.Label(frame_form, text="Teléfono:").grid(row=0, column=4, padx=8, pady=10, sticky="w")
        self.entry_telefono = ttk.Entry(frame_form, width=22)
        self.entry_telefono.grid(row=0, column=5, padx=8, pady=10)

        ttk.Button(
            frame_form,
            text="Registrar propietario",
            command=self.registrar_propietario,
        ).grid(row=0, column=6, padx=12, pady=10)

        self.crear_titulo_seccion(
            self.tab_propietarios,
            "Listado de propietarios",
            "Personas registradas como responsables de mascotas.",
        )

        self.tree_propietarios = self.crear_tabla(
            self.tab_propietarios,
            [
                ("id", "ID", 70),
                ("dni", "DNI", 130),
                ("nombre", "Nombre", 280),
                ("telefono", "Teléfono", 180),
            ],
            alto=12,
        )

    def crear_tab_mascotas(self):
        self.tab_mascotas = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_mascotas, text="Mascotas")

        self.crear_encabezado(
            self.tab_mascotas,
            "🐶 Mascotas",
            "Alta y consulta de mascotas asociadas a cada propietario.",
        )

        frame_form = ttk.LabelFrame(self.tab_mascotas, text="Nueva mascota")
        frame_form.pack(fill="x", padx=20, pady=(0, 12))

        ttk.Label(frame_form, text="Propietario:").grid(row=0, column=0, padx=8, pady=8, sticky="w")
        self.combo_propietario_mascota = ttk.Combobox(frame_form, state="readonly", width=28)
        self.combo_propietario_mascota.grid(row=0, column=1, padx=8, pady=8)

        ttk.Label(frame_form, text="Nombre:").grid(row=0, column=2, padx=8, pady=8, sticky="w")
        self.entry_nombre_mascota = ttk.Entry(frame_form, width=24)
        self.entry_nombre_mascota.grid(row=0, column=3, padx=8, pady=8)

        ttk.Label(frame_form, text="Especie:").grid(row=0, column=4, padx=8, pady=8, sticky="w")
        self.combo_especie = ttk.Combobox(
            frame_form,
            values=["Perro", "Gato", "Ave", "Otra"],
            state="readonly",
            width=18,
        )
        self.combo_especie.grid(row=0, column=5, padx=8, pady=8)

        ttk.Label(frame_form, text="Raza:").grid(row=1, column=0, padx=8, pady=8, sticky="w")
        self.entry_raza = ttk.Entry(frame_form, width=28)
        self.entry_raza.grid(row=1, column=1, padx=8, pady=8)

        ttk.Label(frame_form, text="Edad:").grid(row=1, column=2, padx=8, pady=8, sticky="w")
        self.entry_edad = ttk.Entry(frame_form, width=24)
        self.entry_edad.grid(row=1, column=3, padx=8, pady=8)

        ttk.Button(
            frame_form,
            text="Registrar mascota",
            command=self.registrar_mascota,
        ).grid(row=1, column=5, padx=12, pady=8)

        self.crear_titulo_seccion(
            self.tab_mascotas,
            "Listado de mascotas",
            "Mascotas registradas junto con su especie, raza y propietario.",
        )

        self.tree_mascotas = self.crear_tabla(
            self.tab_mascotas,
            [
                ("id", "ID", 70),
                ("nombre", "Nombre", 180),
                ("especie", "Especie", 130),
                ("raza", "Raza", 170),
                ("edad", "Edad", 90),
                ("propietario", "Propietario", 240),
            ],
            alto=12,
        )

    def crear_tab_turnos(self):
        self.tab_turnos = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_turnos, text="Turnos")

        self.crear_encabezado(
            self.tab_turnos,
            "📅 Turnos",
            "Asignación, consulta y cancelación de turnos veterinarios.",
        )

        frame_form = ttk.LabelFrame(self.tab_turnos, text="Nuevo turno")
        frame_form.pack(fill="x", padx=20, pady=(0, 12))

        ttk.Label(frame_form, text="Mascota:").grid(row=0, column=0, padx=8, pady=8, sticky="w")
        self.combo_mascota_turno = ttk.Combobox(frame_form, state="readonly", width=28)
        self.combo_mascota_turno.grid(row=0, column=1, padx=8, pady=8)

        ttk.Label(frame_form, text="Fecha:").grid(row=0, column=2, padx=8, pady=8, sticky="w")
        self.entry_fecha_turno = ttk.Entry(frame_form, width=18)
        self.entry_fecha_turno.grid(row=0, column=3, padx=8, pady=8)
        self.entry_fecha_turno.insert(0, "dd/mm/yyyy")

        ttk.Label(frame_form, text="Hora:").grid(row=0, column=4, padx=8, pady=8, sticky="w")
        self.entry_hora_turno = ttk.Entry(frame_form, width=16)
        self.entry_hora_turno.grid(row=0, column=5, padx=8, pady=8)
        self.entry_hora_turno.insert(0, "HH:MM")

        ttk.Label(frame_form, text="Nota:").grid(row=1, column=0, padx=8, pady=8, sticky="w")
        self.entry_nota_turno = ttk.Entry(frame_form, width=70)
        self.entry_nota_turno.grid(row=1, column=1, columnspan=4, padx=8, pady=8, sticky="ew")

        ttk.Button(
            frame_form,
            text="Asignar turno",
            command=self.asignar_turno,
        ).grid(row=1, column=5, padx=12, pady=8)

        ttk.Button(
            frame_form,
            text="Cancelar seleccionado",
            command=self.cancelar_turno,
            style="Danger.TButton",
        ).grid(row=1, column=6, padx=12, pady=8)

        self.crear_titulo_seccion(
            self.tab_turnos,
            "Listado de turnos",
            "Turnos pendientes, atendidos y cancelados.",
        )

        self.tree_turnos = self.crear_tabla(
            self.tab_turnos,
            [
                ("id", "ID", 70),
                ("mascota", "Mascota", 180),
                ("fecha", "Fecha", 130),
                ("hora", "Hora", 100),
                ("estado", "Estado", 130),
                ("nota", "Nota", 340),
            ],
            alto=12,
        )

    def crear_tab_atenciones(self):
        self.tab_atenciones = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_atenciones, text="Atenciones")

        self.crear_encabezado(
            self.tab_atenciones,
            "🩺 Atenciones",
            "Registro de diagnósticos, observaciones e importes de cada atención.",
        )

        frame_form = ttk.LabelFrame(self.tab_atenciones, text="Atender turno pendiente")
        frame_form.pack(fill="x", padx=20, pady=(0, 12))

        ttk.Label(frame_form, text="Turno pendiente:").grid(row=0, column=0, padx=8, pady=8, sticky="w")
        self.combo_turno_atencion = ttk.Combobox(frame_form, state="readonly", width=42)
        self.combo_turno_atencion.grid(row=0, column=1, padx=8, pady=8)

        ttk.Label(frame_form, text="Servicio:").grid(row=0, column=2, padx=8, pady=8, sticky="w")
        self.combo_servicio_atencion = ttk.Combobox(frame_form, state="readonly", width=38)
        self.combo_servicio_atencion.grid(row=0, column=3, padx=8, pady=8)

        ttk.Label(frame_form, text="Diagnóstico:").grid(row=1, column=0, padx=8, pady=8, sticky="w")
        self.entry_diagnostico = ttk.Entry(frame_form, width=42)
        self.entry_diagnostico.grid(row=1, column=1, padx=8, pady=8)

        ttk.Label(frame_form, text="Observaciones:").grid(row=1, column=2, padx=8, pady=8, sticky="w")
        self.entry_observaciones = ttk.Entry(frame_form, width=38)
        self.entry_observaciones.grid(row=1, column=3, padx=8, pady=8)

        ttk.Button(
            frame_form,
            text="Registrar atención",
            command=self.registrar_atencion,
        ).grid(row=1, column=4, padx=12, pady=8)

        self.crear_titulo_seccion(
            self.tab_atenciones,
            "Listado de atenciones",
            "Historial de consultas realizadas a través de turnos atendidos.",
        )

        self.tree_atenciones = self.crear_tabla(
            self.tab_atenciones,
            [
                ("id", "ID", 70),
                ("mascota", "Mascota", 170),
                ("servicio", "Servicio", 190),
                ("diagnostico", "Diagnóstico", 240),
                ("observaciones", "Observaciones", 280),
                ("importe", "Importe", 120),
            ],
            alto=12,
        )

    def crear_tab_seguimientos(self):
        self.tab_seguimientos = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_seguimientos, text="Vacunas / Controles")

        self.crear_encabezado(
            self.tab_seguimientos,
            "💉 Vacunas y controles",
            "Seguimiento de vacunas, controles próximos y alertas preventivas.",
        )

        frame_form = ttk.LabelFrame(self.tab_seguimientos, text="Nuevo seguimiento")
        frame_form.pack(fill="x", padx=20, pady=(0, 12))

        ttk.Label(frame_form, text="Mascota:").grid(row=0, column=0, padx=8, pady=8, sticky="w")
        self.combo_mascota_seguimiento = ttk.Combobox(frame_form, state="readonly", width=28)
        self.combo_mascota_seguimiento.grid(row=0, column=1, padx=8, pady=8)

        ttk.Label(frame_form, text="Tipo:").grid(row=0, column=2, padx=8, pady=8, sticky="w")
        self.combo_tipo_seguimiento = ttk.Combobox(
            frame_form,
            values=["Vacuna", "Control"],
            state="readonly",
            width=18,
        )
        self.combo_tipo_seguimiento.grid(row=0, column=3, padx=8, pady=8)

        ttk.Label(frame_form, text="Descripción:").grid(row=0, column=4, padx=8, pady=8, sticky="w")
        self.entry_descripcion_seguimiento = ttk.Entry(frame_form, width=32)
        self.entry_descripcion_seguimiento.grid(row=0, column=5, padx=8, pady=8)

        ttk.Label(frame_form, text="Fecha registro:").grid(row=1, column=0, padx=8, pady=8, sticky="w")
        self.entry_fecha_registro = ttk.Entry(frame_form, width=18)
        self.entry_fecha_registro.grid(row=1, column=1, padx=8, pady=8)
        self.entry_fecha_registro.insert(0, "dd/mm/yyyy")

        ttk.Label(frame_form, text="Próxima fecha:").grid(row=1, column=2, padx=8, pady=8, sticky="w")
        self.entry_proxima_fecha = ttk.Entry(frame_form, width=18)
        self.entry_proxima_fecha.grid(row=1, column=3, padx=8, pady=8)
        self.entry_proxima_fecha.insert(0, "dd/mm/yyyy")

        ttk.Label(frame_form, text="Observaciones:").grid(row=1, column=4, padx=8, pady=8, sticky="w")
        self.entry_observaciones_seguimiento = ttk.Entry(frame_form, width=32)
        self.entry_observaciones_seguimiento.grid(row=1, column=5, padx=8, pady=8)

        ttk.Button(
            frame_form,
            text="Registrar seguimiento",
            command=self.registrar_seguimiento,
        ).grid(row=1, column=6, padx=12, pady=8)

        self.crear_titulo_seccion(
            self.tab_seguimientos,
            "Vacunas y controles registrados",
            "Seguimientos preventivos asociados a cada mascota.",
        )

        self.tree_seguimientos = self.crear_tabla(
            self.tab_seguimientos,
            [
                ("id", "ID", 70),
                ("mascota", "Mascota", 170),
                ("tipo", "Tipo", 120),
                ("descripcion", "Descripción", 260),
                ("fecha_registro", "Fecha registro", 140),
                ("proxima_fecha", "Próxima fecha", 140),
                ("estado", "Estado", 120),
            ],
            alto=12,
        )

    def crear_tab_estadisticas(self):
        self.tab_estadisticas = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_estadisticas, text="Estadísticas")

        self.crear_encabezado(
            self.tab_estadisticas,
            "📊 Estadísticas",
            "Resumen numérico del funcionamiento general de la veterinaria.",
        )

        self.crear_titulo_seccion(
            self.tab_estadisticas,
            "Indicadores generales",
            "Cantidad de registros, turnos por estado, especies, recaudación y servicio más frecuente.",
        )

        self.frame_cards_estadisticas = ttk.Frame(self.tab_estadisticas)
        self.frame_cards_estadisticas.pack(fill="x", padx=11, pady=4)

        for columna in range(4):
            self.frame_cards_estadisticas.columnconfigure(columna, weight=1)

        self.card_est_total = self.crear_tarjeta(
            self.frame_cards_estadisticas,
            "Total recaudado",
            "$0.00",
            "Ingresos registrados",
            0,
            0,
        )

        self.card_est_promedio = self.crear_tarjeta(
            self.frame_cards_estadisticas,
            "Promedio por atención",
            "$0.00",
            "Valor promedio",
            0,
            1,
        )

        self.card_est_atendidos = self.crear_tarjeta(
            self.frame_cards_estadisticas,
            "Turnos atendidos",
            "0",
            "Atenciones completadas",
            0,
            2,
        )

        self.card_est_servicio = self.crear_tarjeta(
            self.frame_cards_estadisticas,
            "Servicio frecuente",
            "Sin datos",
            "Más solicitado",
            0,
            3,
        )

        self.lbl_estadisticas = ttk.Label(
            self.tab_estadisticas,
            text="",
            font=("Consolas", 12),
            justify="left",
            background=COLOR_PANEL,
            foreground=COLOR_TEXTO,
            padding=18,
            relief="solid",
            borderwidth=1,
        )
        self.lbl_estadisticas.pack(fill="both", expand=True, padx=20, pady=14)

        ttk.Button(
            self.tab_estadisticas,
            text="Actualizar estadísticas",
            command=self.refrescar_estadisticas,
            style="Secondary.TButton",
        ).pack(anchor="e", padx=20, pady=(0, 16))

    def registrar_propietario(self):
        dni = self.entry_dni.get().strip()
        nombre = self.entry_nombre_propietario.get().strip()
        telefono = self.entry_telefono.get().strip()

        if not dni.isdigit() or len(dni) != 8:
            messagebox.showerror("Error", "El DNI debe tener exactamente 8 dígitos.")
            return

        if not nombre:
            messagebox.showerror("Error", "El nombre no puede estar vacío.")
            return

        if any(caracter.isdigit() for caracter in nombre):
            messagebox.showerror("Error", "El nombre no debe contener números.")
            return

        if not telefono.isdigit():
            messagebox.showerror("Error", "El teléfono debe contener solo números.")
            return

        for propietario in propietarios:
            if propietario["dni"] == dni:
                messagebox.showerror("Error", "Ya existe un propietario con ese DNI.")
                return

        propietario = {
            "id": generar_id(propietarios),
            "dni": dni,
            "nombre": nombre.title(),
            "telefono": telefono,
        }

        propietarios.append(propietario)
        guardar()
        self.limpiar_propietario()
        self.refrescar_todo()
        messagebox.showinfo("Éxito", "Propietario registrado correctamente.")

    def limpiar_propietario(self):
        self.entry_dni.delete(0, tk.END)
        self.entry_nombre_propietario.delete(0, tk.END)
        self.entry_telefono.delete(0, tk.END)

    def registrar_mascota(self):
        id_propietario = obtener_id_combo(self.combo_propietario_mascota)
        nombre = self.entry_nombre_mascota.get().strip()
        especie = self.combo_especie.get().strip()
        raza = self.entry_raza.get().strip()
        edad_texto = self.entry_edad.get().strip()

        if id_propietario is None:
            messagebox.showerror("Error", "Debe seleccionar un propietario.")
            return

        if not nombre or not especie or not raza:
            messagebox.showerror("Error", "Debe completar nombre, especie y raza.")
            return

        if not edad_texto.isdigit():
            messagebox.showerror("Error", "La edad debe ser un número.")
            return

        for mascota in mascotas:
            mismo_nombre = mascota["nombre"].lower() == nombre.lower()
            mismo_propietario = mascota["id_propetario"] == id_propietario

            if mismo_nombre and mismo_propietario:
                messagebox.showerror(
                    "Error",
                    "Ya existe una mascota con ese nombre para el propietario seleccionado.",
                )
                return

        mascota = {
            "id": generar_id(mascotas),
            "nombre": nombre.title(),
            "especie": especie,
            "raza": raza.title(),
            "edad": int(edad_texto),
            "id_propetario": id_propietario,
        }

        mascotas.append(mascota)
        guardar()

        self.entry_nombre_mascota.delete(0, tk.END)
        self.combo_especie.set("")
        self.entry_raza.delete(0, tk.END)
        self.entry_edad.delete(0, tk.END)

        self.refrescar_todo()
        messagebox.showinfo("Éxito", "Mascota registrada correctamente.")

    def asignar_turno(self):
        id_mascota = obtener_id_combo(self.combo_mascota_turno)
        fecha = self.entry_fecha_turno.get().strip()
        hora = self.entry_hora_turno.get().strip()
        nota = self.entry_nota_turno.get().strip()

        if id_mascota is None:
            messagebox.showerror("Error", "Debe seleccionar una mascota.")
            return

        if convertir_fecha(fecha) is None:
            messagebox.showerror("Error", "La fecha debe tener formato dd/mm/yyyy.")
            return

        if not validar_hora(hora):
            messagebox.showerror("Error", "La hora debe tener formato HH:MM.")
            return

        for turno in turnos:
            misma_fecha = turno["fecha"] == fecha
            misma_hora = turno["hora"] == hora
            esta_pendiente = turno["estado"] == "Pendiente"

            if misma_fecha and misma_hora and esta_pendiente:
                messagebox.showerror("Error", "Ese horario ya está ocupado.")
                return

        turno = {
            "id": generar_id(turnos),
            "id_mascota": id_mascota,
            "fecha": fecha,
            "hora": hora,
            "nota": nota,
            "estado": "Pendiente",
        }

        turnos.append(turno)
        guardar()

        self.entry_fecha_turno.delete(0, tk.END)
        self.entry_fecha_turno.insert(0, "dd/mm/yyyy")
        self.entry_hora_turno.delete(0, tk.END)
        self.entry_hora_turno.insert(0, "HH:MM")
        self.entry_nota_turno.delete(0, tk.END)

        self.refrescar_todo()
        messagebox.showinfo("Éxito", "Turno asignado correctamente.")

    def cancelar_turno(self):
        seleccionado = self.tree_turnos.selection()

        if not seleccionado:
            messagebox.showerror("Error", "Debe seleccionar un turno.")
            return

        valores = self.tree_turnos.item(seleccionado[0], "values")
        id_turno = int(valores[0])
        turno = buscar_por_id(turnos, id_turno)

        if turno is None:
            messagebox.showerror("Error", "No se encontró el turno.")
            return

        if turno["estado"] != "Pendiente":
            messagebox.showerror("Error", "Solo se pueden cancelar turnos pendientes.")
            return

        confirmar = messagebox.askyesno(
            "Confirmar cancelación",
            "¿Seguro que desea cancelar este turno?",
        )

        if confirmar:
            turno["estado"] = "Cancelado"
            guardar()
            self.refrescar_todo()
            messagebox.showinfo("Éxito", "Turno cancelado correctamente.")

    def registrar_atencion(self):
        id_turno = obtener_id_combo(self.combo_turno_atencion)
        id_servicio = obtener_id_combo(self.combo_servicio_atencion)
        diagnostico = self.entry_diagnostico.get().strip()
        observaciones = self.entry_observaciones.get().strip()

        if id_turno is None:
            messagebox.showerror("Error", "Debe seleccionar un turno pendiente.")
            return

        if id_servicio is None:
            messagebox.showerror("Error", "Debe seleccionar un servicio.")
            return

        if not diagnostico:
            messagebox.showerror("Error", "Debe ingresar un diagnóstico.")
            return

        turno = buscar_por_id(turnos, id_turno)
        servicio = buscar_por_id(servicios, id_servicio)

        if turno is None or servicio is None:
            messagebox.showerror("Error", "Turno o servicio no encontrado.")
            return

        if turno["estado"] != "Pendiente":
            messagebox.showerror("Error", "El turno no está pendiente.")
            return

        atencion = {
            "id": generar_id(atenciones),
            "id_turno": turno["id"],
            "id_servicio": servicio["id"],
            "diagnostico": diagnostico,
            "observaciones": observaciones,
            "importe": servicio["precio"],
        }

        atenciones.append(atencion)
        turno["estado"] = "Atendido"
        guardar()

        self.entry_diagnostico.delete(0, tk.END)
        self.entry_observaciones.delete(0, tk.END)

        self.refrescar_todo()
        messagebox.showinfo("Éxito", f"Atención registrada. Importe: ${servicio['precio']}")

    def registrar_seguimiento(self):
        id_mascota = obtener_id_combo(self.combo_mascota_seguimiento)
        tipo = self.combo_tipo_seguimiento.get().strip()
        descripcion = self.entry_descripcion_seguimiento.get().strip()
        fecha_registro = self.entry_fecha_registro.get().strip()
        proxima_fecha = self.entry_proxima_fecha.get().strip()
        observaciones = self.entry_observaciones_seguimiento.get().strip()

        if id_mascota is None:
            messagebox.showerror("Error", "Debe seleccionar una mascota.")
            return

        if not tipo or not descripcion:
            messagebox.showerror("Error", "Debe completar tipo y descripción.")
            return

        if convertir_fecha(fecha_registro) is None:
            messagebox.showerror("Error", "La fecha de registro debe tener formato dd/mm/yyyy.")
            return

        if convertir_fecha(proxima_fecha) is None:
            messagebox.showerror("Error", "La próxima fecha debe tener formato dd/mm/yyyy.")
            return

        seguimiento = {
            "id": generar_id(seguimientos),
            "id_mascota": id_mascota,
            "tipo": tipo,
            "descripcion": descripcion,
            "fecha_registro": fecha_registro,
            "proxima_fecha": proxima_fecha,
            "observaciones": observaciones,
            "estado": "Pendiente",
        }

        seguimientos.append(seguimiento)
        guardar()

        self.combo_tipo_seguimiento.set("")
        self.entry_descripcion_seguimiento.delete(0, tk.END)
        self.entry_fecha_registro.delete(0, tk.END)
        self.entry_fecha_registro.insert(0, "dd/mm/yyyy")
        self.entry_proxima_fecha.delete(0, tk.END)
        self.entry_proxima_fecha.insert(0, "dd/mm/yyyy")
        self.entry_observaciones_seguimiento.delete(0, tk.END)

        self.refrescar_todo()
        messagebox.showinfo("Éxito", "Vacuna/control registrado correctamente.")

    def refrescar_todo(self):
        self.refrescar_combos()
        self.refrescar_propietarios()
        self.refrescar_mascotas()
        self.refrescar_turnos()
        self.refrescar_atenciones()
        self.refrescar_seguimientos()
        self.refrescar_estadisticas()
        self.refrescar_inicio()
        self.refrescar_alertas()

    def refrescar_combos(self):
        self.combo_propietario_mascota["values"] = [
            f"{p['id']} - {p['nombre']}" for p in propietarios
        ]

        self.combo_mascota_turno["values"] = [
            f"{m['id']} - {m['nombre']}" for m in mascotas
        ]

        self.combo_mascota_seguimiento["values"] = [
            f"{m['id']} - {m['nombre']}" for m in mascotas
        ]

        turnos_pendientes = []

        for turno in turnos:
            if turno["estado"] == "Pendiente":
                mascota = buscar_por_id(mascotas, turno["id_mascota"])
                nombre_mascota = "Mascota desconocida"

                if mascota is not None:
                    nombre_mascota = mascota["nombre"]

                turnos_pendientes.append(
                    f"{turno['id']} - {nombre_mascota} - {turno['fecha']} {turno['hora']}"
                )

        self.combo_turno_atencion["values"] = turnos_pendientes

        self.combo_servicio_atencion["values"] = [
            f"{s['id']} - {s['nombre']} - ${s['precio']}" for s in servicios
        ]

    def refrescar_propietarios(self):
        self.limpiar_tree(self.tree_propietarios)

        for propietario in propietarios:
            self.tree_propietarios.insert(
                "",
                tk.END,
                values=(
                    propietario["id"],
                    propietario["dni"],
                    propietario["nombre"],
                    propietario["telefono"],
                ),
            )

    def refrescar_mascotas(self):
        self.limpiar_tree(self.tree_mascotas)

        for mascota in mascotas:
            propietario = buscar_por_id(propietarios, mascota["id_propetario"])
            nombre_propietario = "Desconocido"

            if propietario is not None:
                nombre_propietario = propietario["nombre"]

            self.tree_mascotas.insert(
                "",
                tk.END,
                values=(
                    mascota["id"],
                    mascota["nombre"],
                    mascota["especie"],
                    mascota["raza"],
                    mascota["edad"],
                    nombre_propietario,
                ),
            )

    def refrescar_turnos(self):
        self.limpiar_tree(self.tree_turnos)

        for turno in turnos:
            mascota = buscar_por_id(mascotas, turno["id_mascota"])
            nombre_mascota = "Desconocida"

            if mascota is not None:
                nombre_mascota = mascota["nombre"]

            self.tree_turnos.insert(
                "",
                tk.END,
                values=(
                    turno["id"],
                    nombre_mascota,
                    turno["fecha"],
                    turno["hora"],
                    turno["estado"],
                    turno["nota"],
                ),
            )

    def refrescar_atenciones(self):
        self.limpiar_tree(self.tree_atenciones)

        for atencion in atenciones:
            turno = buscar_por_id(turnos, atencion["id_turno"])
            servicio = buscar_por_id(servicios, atencion["id_servicio"])

            nombre_mascota = "Desconocida"
            nombre_servicio = "Desconocido"

            if turno is not None:
                mascota = buscar_por_id(mascotas, turno["id_mascota"])
                if mascota is not None:
                    nombre_mascota = mascota["nombre"]

            if servicio is not None:
                nombre_servicio = servicio["nombre"]

            self.tree_atenciones.insert(
                "",
                tk.END,
                values=(
                    atencion["id"],
                    nombre_mascota,
                    nombre_servicio,
                    atencion["diagnostico"],
                    atencion["observaciones"],
                    f"${atencion['importe']}",
                ),
            )

    def refrescar_seguimientos(self):
        self.limpiar_tree(self.tree_seguimientos)

        for seguimiento in seguimientos:
            mascota = buscar_por_id(mascotas, seguimiento["id_mascota"])
            nombre_mascota = "Desconocida"

            if mascota is not None:
                nombre_mascota = mascota["nombre"]

            self.tree_seguimientos.insert(
                "",
                tk.END,
                values=(
                    seguimiento["id"],
                    nombre_mascota,
                    seguimiento["tipo"],
                    seguimiento["descripcion"],
                    seguimiento["fecha_registro"],
                    seguimiento["proxima_fecha"],
                    seguimiento["estado"],
                ),
            )

    def calcular_estadisticas(self):
        pendientes = 0
        atendidos = 0
        cancelados = 0

        for turno in turnos:
            if turno["estado"] == "Pendiente":
                pendientes += 1
            elif turno["estado"] == "Atendido":
                atendidos += 1
            elif turno["estado"] == "Cancelado":
                cancelados += 1

        perros = 0
        gatos = 0
        aves = 0
        otras = 0

        for mascota in mascotas:
            if mascota["especie"] == "Perro":
                perros += 1
            elif mascota["especie"] == "Gato":
                gatos += 1
            elif mascota["especie"] == "Ave":
                aves += 1
            else:
                otras += 1

        total = 0.0

        for atencion in atenciones:
            total += atencion["importe"]

        promedio = 0.0

        if len(atenciones) > 0:
            promedio = total / len(atenciones)

        servicio_frecuente = "Sin datos"
        cantidades_servicios = {}

        for atencion in atenciones:
            id_servicio = atencion["id_servicio"]

            if id_servicio in cantidades_servicios:
                cantidades_servicios[id_servicio] += 1
            else:
                cantidades_servicios[id_servicio] = 1

        if cantidades_servicios:
            id_mas_frecuente = max(cantidades_servicios, key=cantidades_servicios.get)
            servicio = buscar_por_id(servicios, id_mas_frecuente)

            if servicio is not None:
                servicio_frecuente = servicio["nombre"]

        return {
            "pendientes": pendientes,
            "atendidos": atendidos,
            "cancelados": cancelados,
            "perros": perros,
            "gatos": gatos,
            "aves": aves,
            "otras": otras,
            "total": total,
            "promedio": promedio,
            "servicio_frecuente": servicio_frecuente,
        }

    def refrescar_estadisticas(self):
        datos = self.calcular_estadisticas()

        self.actualizar_tarjeta(self.card_est_total, f"${datos['total']:.2f}")
        self.actualizar_tarjeta(self.card_est_promedio, f"${datos['promedio']:.2f}")
        self.actualizar_tarjeta(self.card_est_atendidos, datos["atendidos"])
        self.actualizar_tarjeta(self.card_est_servicio, datos["servicio_frecuente"])

        texto = (
            f"Propietarios: {len(propietarios)}\n"
            f"Mascotas: {len(mascotas)}\n"
            f"Turnos: {len(turnos)}\n"
            f"Atenciones: {len(atenciones)}\n"
            f"Vacunas / controles: {len(seguimientos)}\n\n"
            f"Turnos por estado:\n"
            f"  Pendientes: {datos['pendientes']}\n"
            f"  Atendidos: {datos['atendidos']}\n"
            f"  Cancelados: {datos['cancelados']}\n\n"
            f"Mascotas por especie:\n"
            f"  Perros: {datos['perros']}\n"
            f"  Gatos: {datos['gatos']}\n"
            f"  Aves: {datos['aves']}\n"
            f"  Otras: {datos['otras']}\n\n"
            f"Recaudación:\n"
            f"  Total recaudado: ${datos['total']:.2f}\n"
            f"  Promedio por atención: ${datos['promedio']:.2f}\n\n"
            f"Servicio más frecuente: {datos['servicio_frecuente']}"
        )

        self.lbl_estadisticas.config(text=texto)

    def refrescar_inicio(self):
        self.actualizar_tarjeta(self.card_propietarios, len(propietarios))
        self.actualizar_tarjeta(self.card_mascotas, len(mascotas))
        self.actualizar_tarjeta(self.card_turnos, len(turnos))
        self.actualizar_tarjeta(self.card_atenciones, len(atenciones))
        self.actualizar_tarjeta(self.card_seguimientos, len(seguimientos))

    def refrescar_alertas(self):
        self.limpiar_tree(self.tree_alertas)

        hoy = date.today()

        for seguimiento in seguimientos:
            proxima_fecha = convertir_fecha(seguimiento["proxima_fecha"])

            if proxima_fecha is None:
                continue

            diferencia = (proxima_fecha - hoy).days

            if diferencia < 0:
                estado = f"Vencido hace {abs(diferencia)} día/s"
            elif diferencia == 0:
                estado = "Vence hoy"
            elif diferencia <= 7:
                estado = f"Próximo: faltan {diferencia} día/s"
            else:
                continue

            mascota = buscar_por_id(mascotas, seguimiento["id_mascota"])
            nombre_mascota = "Desconocida"

            if mascota is not None:
                nombre_mascota = mascota["nombre"]

            self.tree_alertas.insert(
                "",
                tk.END,
                values=(
                    nombre_mascota,
                    seguimiento["tipo"],
                    seguimiento["descripcion"],
                    seguimiento["proxima_fecha"],
                    estado,
                ),
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = VeterinariaGUI(root)
    root.mainloop()