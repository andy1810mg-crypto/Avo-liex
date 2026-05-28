import streamlit as st
import matplotlib.pyplot as plt

# ---------------------------------------------------
# CONFIGURACIÓN GENERAL
# ---------------------------------------------------

st.set_page_config(
    page_title="AVO-LIOEX",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------
# MEMORIA GLOBAL
# ---------------------------------------------------

if "resultado_simulacion" not in st.session_state:

    st.session_state.resultado_simulacion = None

# ---------------------------------------------------
# ESTILO VISUAL
# ---------------------------------------------------

st.markdown("""
<style>

[data-testid="stAppViewContainer"] {

    background:
    linear-gradient(
        135deg,
        #f9faf7,
        #eef7ea,
        #e2f1dc
    );
}

[data-testid="stSidebar"] {

    background-color: #edf4e8;

    border-right: 1px solid #cbd5c0;
}

html, body, [class*="css"] {

    color: #1f2937;

    font-family: 'Segoe UI', sans-serif;
}

[data-testid="stSidebar"] * {

    color: #1f2937 !important;
}

h1 {

    color: #0f172a !important;

    font-size: 3rem;

    font-weight: 700;
}

h2, h3 {

    color: #1e293b !important;
}

p {

    color: #374151;
}

[data-testid="metric-container"] {

    background-color: rgba(255,255,255,0.92);

    border: 1px solid #d1d5db;

    padding: 20px;

    border-radius: 18px;

    box-shadow:
        0px 4px 20px rgba(0,0,0,0.08);

    transition: 0.3s;
}

[data-testid="metric-container"]:hover {

    transform: translateY(-3px);

    border: 1px solid #22c55e;
}

.stButton > button {

    background: linear-gradient(
        to right,
        #16a34a,
        #15803d
    );

    color: white;

    border: none;

    border-radius: 12px;

    padding: 12px;

    font-size: 16px;

    font-weight: 600;
}

.stNumberInput input {

    background-color: white;

    color: #111827;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

col1, col2, col3 = st.columns([1,4,2])

with col1:

    st.image(
        "images/uvglogo.jpeg",
        width=120
    )

with col2:

    st.title("AVO-LIOEX")

    st.caption(
        "Sistema de simulación industrial para extracción de aceite de aguacate Hass"
    )

with col3:

    st.image(
        "images/avo.jpeg.jpeg",
        width=230
    )

st.divider()

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

st.sidebar.title("Panel de navegación")

menu = st.sidebar.radio(
    "",
    [
        "Inicio",
        "Simulador",
        "Dashboard",
        "Panel de Control",
        "Resultados"
    ]
)

# ---------------------------------------------------
# INICIO
# ---------------------------------------------------

if menu == "Inicio":

    st.header("Bienvenido a AVO-LIOEX")

    st.write("""
    Plataforma de simulación industrial enfocada
    en el proceso de extracción sólido-líquido
    de aceite de aguacate Hass mediante el uso
    de hexano como solvente.
    """)

    st.info("""
    1. Seleccione el tipo de muestra.
    2. Ingrese variables operativas.
    3. Ejecute la simulación.
    4. Revise Dashboard y Resultados.
    """)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Temperatura recomendada",
        "70 - 78.5 °C"
    )

    col2.metric(
        "Ciclos de lavado",
        "5 - 10"
    )

    col3.metric(
        "Recuperación de hexano",
        "80 %"
    )

    col4.metric(
        "Rendimiento esperado",
        "55.3 %"
    )

# ---------------------------------------------------
# SIMULADOR
# ---------------------------------------------------

elif menu == "Simulador":

    st.header("Simulación del proceso")

    tab1, tab2, tab3 = st.tabs([
        "Operación",
        "Costos y sostenibilidad",
        "Calidad del aceite"
    ])

    # ---------------------------------------------------
    # TAB OPERACIÓN
    # ---------------------------------------------------

    with tab1:

        tipo_muestra = st.radio(
            "Seleccione el material a procesar",
            [
                "Pulpa de aguacate",
                "Cáscara de aguacate"
            ]
        )

        col1, col2 = st.columns(2)

        with col1:

            st.caption(
                "Rango recomendado: 500 - 5000 g"
            )

            masa_muestra = st.number_input(
                "Masa de muestra (g)",
                min_value=100.0,
                max_value=5000.0,
                value=1000.0
            )

            st.caption(
                "Rango recomendado: 0 - 80 %"
            )

            humedad = st.slider(
                "Humedad de la muestra (%)",
                0,
                100,
                75
            )

        with col2:

            st.caption(
                "Rango recomendado: 200 - 1500 mL"
            )

            hexano = st.number_input(
                "Volumen de hexano (mL)",
                min_value=100.0,
                max_value=2000.0,
                value=500.0
            )

            st.caption(
                "Rango recomendado: 70 - 78.5 °C"
            )

            temperatura = st.slider(
                "Temperatura de evaporación del hexano (°C)",
                40,
                100,
                75
            )

            st.caption(
                "Rango recomendado: 5 - 10 ciclos"
            )

            ciclos = st.slider(
                "Ciclos de lavado",
                1,
                15,
                5
            )

        lote = st.selectbox(
            "Tamaño de lote",
            [
                "Laboratorio",
                "Piloto",
                "Industrial"
            ]
        )

        col1, col2, col3 = st.columns(3)

        tiempo_extraccion = col1.number_input(
            "Tiempo de extracción (min)",
            min_value=1,
            max_value=120,
            value=15
        )

        tiempo_evaporacion = col2.number_input(
            "Tiempo de evaporación (min)",
            min_value=1,
            max_value=120,
            value=20
        )

        tiempo_enfriamiento = col3.number_input(
            "Tiempo de enfriamiento (min)",
            min_value=1,
            max_value=60,
            value=10
        )

    # ---------------------------------------------------
    # TAB COSTOS
    # ---------------------------------------------------

    with tab2:

        costo_hexano = st.number_input(
            "Costo de hexano ($)",
            min_value=0.0,
            value=25.0
        )

        costo_energia = st.number_input(
            "Costo energético ($)",
            min_value=0.0,
            value=18.0
        )

        costo_materia = st.number_input(
            "Costo de materia prima ($)",
            min_value=0.0,
            value=30.0
        )

        reciclaje = st.slider(
            "Hexano reciclado (%)",
            0,
            100,
            80
        )

        impacto = st.slider(
            "Impacto ambiental estimado (%)",
            0,
            100,
            35
        )

    # ---------------------------------------------------
    # TAB CALIDAD
    # ---------------------------------------------------

    with tab3:

        pureza = st.slider(
            "Pureza estimada (%)",
            0,
            100,
            92
        )

        acidez = st.slider(
            "Índice de acidez (mg KOH/g)",
            0.0,
            5.0,
            1.2
        )

        if pureza > 90:

            st.success(
                "Aceite de alta calidad"
            )

        elif pureza > 70:

            st.warning(
                "Calidad moderada"
            )

        else:

            st.error(
                "Calidad baja"
            )

    # ---------------------------------------------------
    # MODOS
    # ---------------------------------------------------

    modo = st.selectbox(
        "Modo de simulación",
        [
            "Operación normal",
            "Optimización automática",
            "¿Qué pasaría si...?"
        ]
    )

    # ---------------------------------------------------
    # BOTÓN
    # ---------------------------------------------------

    if st.button("Iniciar simulación"):

        if tipo_muestra == "Pulpa de aguacate":

            porcentaje_aceite = 0.15
            eficiencia_base = 0.553

        else:

            porcentaje_aceite = 0.05
            eficiencia_base = 0.32

        if modo == "Optimización automática":

            temperatura = 75
            ciclos = 8
            humedad = 20

        agua_eliminada = (
            masa_muestra * (humedad / 100)
        )

        aceite_teorico = (
            masa_muestra * porcentaje_aceite
        )

        eficiencia_ciclos = (
            eficiencia_base + ((ciclos - 5) * 0.015)
        )

        if eficiencia_ciclos > 0.75:
            eficiencia_ciclos = 0.75

        aceite_recuperado = (
            aceite_teorico * eficiencia_ciclos
        )

        hexano_recuperado = (
            hexano * (reciclaje / 100)
        )

        rendimiento = (
            aceite_recuperado / aceite_teorico
        ) * 100

        eficiencia_global = (
            aceite_recuperado / masa_muestra
        ) * 100

        residuos = (
            masa_muestra
            - agua_eliminada
            - aceite_recuperado
        )

        costo_total = (
            costo_hexano
            + costo_energia
            + costo_materia
        )

        st.session_state.resultado_simulacion = {

            "aceite_recuperado": aceite_recuperado,
            "agua_eliminada": agua_eliminada,
            "hexano_recuperado": hexano_recuperado,
            "rendimiento": rendimiento,
            "eficiencia_global": eficiencia_global,
            "residuos": residuos,
            "pureza": pureza,
            "acidez": acidez,
            "impacto": impacto,
            "costo_total": costo_total,
            "temperatura": temperatura,
            "ciclos": ciclos,
            "modo": modo
        }

        st.success(
            "Simulación ejecutada correctamente."
        )

# ---------------------------------------------------
# DASHBOARD
# ---------------------------------------------------

elif menu == "Dashboard":

    st.header("Dashboard industrial")

    if st.session_state.resultado_simulacion is None:

        st.warning(
            "Primero debe ejecutar una simulación."
        )

    else:

        datos = st.session_state.resultado_simulacion

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Rendimiento",
            f"{datos['rendimiento']:.2f} %"
        )

        col2.metric(
            "Pureza",
            f"{datos['pureza']} %"
        )

        col3.metric(
            "Hexano recuperado",
            f"{datos['hexano_recuperado']:.2f} mL"
        )

        col4.metric(
            "Costo total",
            f"${datos['costo_total']:.2f}"
        )

        st.progress(
            int(datos['rendimiento'])
        )

# ---------------------------------------------------
# PANEL DE CONTROL
# ---------------------------------------------------

elif menu == "Panel de Control":

    st.header("Panel de control industrial")

    temperatura_panel = st.slider(
        "Temperatura de evaporación del hexano (°C)",
        40,
        100,
        75
    )

    ciclos_panel = st.slider(
        "Ciclos de lavado",
        1,
        15,
        5
    )

    humedad_panel = st.slider(
        "Humedad de la muestra (%)",
        0,
        20,
        3
    )

    if 70 <= temperatura_panel <= 78.5:

        st.success(
            "Temperatura estable"
        )

    else:

        st.error(
            "Temperatura fuera de límites"
        )

# ---------------------------------------------------
# RESULTADOS
# ---------------------------------------------------

elif menu == "Resultados":

    st.header("Resultados y análisis")

    if st.session_state.resultado_simulacion is None:

        st.warning(
            "Primero debe ejecutar una simulación."
        )

    else:

        datos = st.session_state.resultado_simulacion

        rendimiento_teorico = 55.3

        diferencia = (
            datos["rendimiento"]
            - rendimiento_teorico
        )

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Simulado",
            f"{datos['rendimiento']:.2f} %"
        )

        col2.metric(
            "Teórico",
            f"{rendimiento_teorico:.2f} %"
        )

        col3.metric(
            "Diferencia",
            f"{diferencia:.2f} %"
        )

        opcion_grafica = st.selectbox(
            "Seleccione visualización",
            [
                "Distribución del proceso",
                "Comparación teórica",
                "Rendimiento vs Temperatura",
                "Costos del proceso"
            ]
        )

        # ---------------------------------------------------
        # DISTRIBUCIÓN
        # ---------------------------------------------------

        if opcion_grafica == "Distribución del proceso":

            etiquetas = [
                "Aceite",
                "Agua",
                "Residuos"
            ]

            valores = [
                datos["aceite_recuperado"],
                datos["agua_eliminada"],
                datos["residuos"]
            ]

            fig, ax = plt.subplots(
                figsize=(5,4)
            )

            ax.pie(
                valores,
                labels=etiquetas,
                autopct='%1.1f%%',
                startangle=90
            )

            st.pyplot(fig)

        # ---------------------------------------------------
        # COMPARACIÓN
        # ---------------------------------------------------

        elif opcion_grafica == "Comparación teórica":

            categorias = [
                "Simulado",
                "Teórico"
            ]

            valores = [
                datos["rendimiento"],
                rendimiento_teorico
            ]

            fig, ax = plt.subplots(
                figsize=(5,4)
            )

            ax.bar(
                categorias,
                valores,
                color=["#16a34a", "#14532d"]
            )

            ax.set_ylabel(
                "Rendimiento (%)"
            )

            st.pyplot(fig)

        # ---------------------------------------------------
        # TEMPERATURA
        # ---------------------------------------------------

        elif opcion_grafica == "Rendimiento vs Temperatura":

            temperaturas = [
                50, 60, 70, 75, 80, 90
            ]

            rendimiento_temp = [
                30, 40, 50, 55.3, 48, 35
            ]

            fig, ax = plt.subplots(
                figsize=(6,4)
            )

            ax.plot(
                temperaturas,
                rendimiento_temp,
                marker='o',
                linewidth=3,
                color='#15803d'
            )

            ax.grid(True)

            st.pyplot(fig)

        # ---------------------------------------------------
        # COSTOS
        # ---------------------------------------------------

        elif opcion_grafica == "Costos del proceso":

            categorias = [
                "Costo total"
            ]

            valores = [
                datos["costo_total"]
            ]

            fig, ax = plt.subplots(
                figsize=(5,4)
            )

            ax.bar(
                categorias,
                valores,
                color='#166534'
            )

            ax.set_ylabel(
                'Costo ($)'
            )

            st.pyplot(fig)
            