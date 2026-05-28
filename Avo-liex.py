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

/* Fondo principal */

[data-testid="stAppViewContainer"] {

    background:
    linear-gradient(
        135deg,
        #f9faf7,
        #eef7ea,
        #e2f1dc
    );
}

/* Sidebar */

[data-testid="stSidebar"] {

    background-color: #edf4e8;

    border-right: 1px solid #cbd5c0;
}

/* Texto general */

html, body, p, label, div, span {

    color: #111827 !important;

    font-family: 'Segoe UI', sans-serif;
}

/* Sidebar */

[data-testid="stSidebar"] * {

    color: #111827 !important;
}

/* Títulos */

h1 {

    color: #0f172a !important;

    font-size: 3rem;

    font-weight: 700;
}

h2, h3 {

    color: #1e293b !important;
}

/* Tabs */

button[data-baseweb="tab"] {

    color: #111827 !important;

    font-weight: 600 !important;
}

/* Radios */

.stRadio * {

    color: #111827 !important;
}

/* Sliders */

.stSlider * {

    color: #111827 !important;
}

/* INPUTS */

.stNumberInput input {

    background-color: white !important;

    color: #111827 !important;

    border-radius: 8px !important;
}

/* BOTONES + Y - */

button {

    color: #111827 !important;
}

/* Selectbox */

.stSelectbox * {

    color: #111827 !important;
}

/* Captions */

small {

    color: #374151 !important;
}

/* Métricas */

[data-testid="metric-container"] {

    background-color: rgba(255,255,255,0.92);

    border: 1px solid #d1d5db;

    padding: 20px;

    border-radius: 18px;

    box-shadow:
        0px 4px 20px rgba(0,0,0,0.08);
}

/* Botones principales */

.stButton > button {

    background: linear-gradient(
        to right,
        #16a34a,
        #15803d
    );

    color: white !important;

    border: none;

    border-radius: 12px;

    padding: 12px;

    font-size: 16px;

    font-weight: 600;
}

/* Alertas */

.stAlert {

    border-radius: 14px;
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
    4. Revise resultados y comparaciones.
    """)

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Temperatura recomendada",
        "70 - 78.5 °C"
    )

    col2.metric(
        "Ciclos de lavado",
        "5 - 10"
    )

    col3.metric(
        "Rendimiento esperado",
        "55.3 %"
    )

# ---------------------------------------------------
# SIMULADOR
# ---------------------------------------------------

elif menu == "Simulador":

    st.header("Simulación del proceso")

    tab1, tab2 = st.tabs([
        "Operación",
        "Calidad y sostenibilidad"
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

        st.divider()

        col1, col2, col3 = st.columns(3)

        with col1:

            st.caption(
                "Rango recomendado: 10 - 30 min"
            )

            tiempo_extraccion = st.number_input(
                "Tiempo de extracción (min)",
                min_value=1,
                max_value=120,
                value=15
            )

        with col2:

            st.caption(
                "Rango recomendado: 15 - 40 min"
            )

            tiempo_evaporacion = st.number_input(
                "Tiempo de evaporación (min)",
                min_value=1,
                max_value=120,
                value=20
            )

        with col3:

            st.caption(
                "Rango recomendado: 5 - 20 min"
            )

            tiempo_enfriamiento = st.number_input(
                "Tiempo de enfriamiento (min)",
                min_value=1,
                max_value=60,
                value=10
            )

    # ---------------------------------------------------
    # TAB CALIDAD Y SOSTENIBILIDAD
    # ---------------------------------------------------

    with tab2:

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
    # BOTÓN
    # ---------------------------------------------------

    if st.button("Iniciar simulación"):

        if tipo_muestra == "Pulpa de aguacate":

            porcentaje_aceite = 0.15
            eficiencia_base = 0.553

        else:

            porcentaje_aceite = 0.05
            eficiencia_base = 0.32

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

        costo_hexano = (
            hexano * 0.08
        )

        costo_energia = (
            (
                tiempo_extraccion
                + tiempo_evaporacion
                + tiempo_enfriamiento
            ) * 0.15
        )

        costo_total = (
            costo_hexano
            + costo_energia
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
            "costo_hexano": costo_hexano,
            "costo_energia": costo_energia,
            "temperatura": temperatura,
            "ciclos": ciclos,
            "tipo_muestra": tipo_muestra
        }

        st.success(
            "Simulación ejecutada correctamente."
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
        "Ciclos de lavado del sistema",
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

    st.divider()

    if 70 <= temperatura_panel <= 78.5:

        st.success(
            "Temperatura estable"
        )

    else:

        st.error(
            "Temperatura fuera de límites"
        )

    if 5 <= ciclos_panel <= 10:

        st.success(
            "Ciclos adecuados"
        )

    else:

        st.warning(
            "Ciclos fuera del rango"
        )

    if humedad_panel < 5:

        st.success(
            "Humedad controlada"
        )

    else:

        st.error(
            "Humedad elevada"
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

        st.divider()

        st.subheader(
            "Interpretación automática"
        )

        if datos["rendimiento"] >= 55:

            st.success(
                "El rendimiento obtenido es cercano al valor teórico esperado."
            )

        elif datos["rendimiento"] >= 40:

            st.warning(
                "El sistema presenta un rendimiento moderado."
            )

        else:

            st.error(
                "El rendimiento obtenido es bajo."
            )

        st.divider()

        st.subheader(
            "Análisis económico"
        )

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Costo de hexano",
            f"Q {datos['costo_hexano']:.2f}"
        )

        col2.metric(
            "Costo energético",
            f"Q {datos['costo_energia']:.2f}"
        )

        col3.metric(
            "Costo total",
            f"Q {datos['costo_total']:.2f}"
        )

        st.divider()

        opcion_grafica = st.selectbox(
            "Seleccione visualización",
            [
                "Distribución del proceso",
                "Comparación teórica",
                "Rendimiento vs Temperatura",
                "Costos del proceso"
            ]
        )

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

        elif opcion_grafica == "Costos del proceso":

            categorias = [
                "Hexano",
                "Energía",
                "Total"
            ]

            valores = [
                datos["costo_hexano"],
                datos["costo_energia"],
                datos["costo_total"]
            ]

            fig, ax = plt.subplots(
                figsize=(5,4)
            )

            ax.bar(
                categorias,
                valores,
                color=[
                    '#16a34a',
                    '#15803d',
                    '#166534'
                ]
            )

            ax.set_ylabel(
                'Costo (Q)'
            )

            st.pyplot(fig)
            