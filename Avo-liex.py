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

    border-right: 1px solid #c7d2c0;
}

/* Texto general */

html, body, [class*="css"] {

    color: #1f2937;

    font-family: 'Segoe UI', sans-serif;
}

/* Sidebar texto */

[data-testid="stSidebar"] * {

    color: #1f2937 !important;
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

/* Párrafos */

p {

    color: #374151;
}

/* Tarjetas */

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

/* Botones */

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

    transition: 0.3s;
}

.stButton > button:hover {

    transform: scale(1.02);

    background: linear-gradient(
        to right,
        #15803d,
        #166534
    );
}

/* Inputs */

.stNumberInput input {

    background-color: white;

    color: #111827;
}

/* Alertas */

.stAlert {

    border-radius: 14px;
}

/* Separadores */

hr {

    border: 1px solid #d1d5db;
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
# VARIABLES GLOBALES
# ---------------------------------------------------

rendimiento = 0
aceite_recuperado = 0
hexano_recuperado = 0
eficiencia_global = 0

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

    st.divider()

    st.info("""
    1. Seleccione el tipo de muestra.
    2. Ingrese las variables operativas.
    3. Ejecute la simulación.
    4. Analice los resultados.
    """)

    st.divider()

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
        "Rendimiento teórico",
        "55.3 %"
    )

# ---------------------------------------------------
# SIMULADOR
# ---------------------------------------------------

elif menu == "Simulador":

    st.header("Simulación del proceso")

    st.divider()

    st.subheader("Tipo de muestra")

    tipo_muestra = st.radio(
        "Seleccione el material a procesar",
        [
            "Pulpa de aguacate",
            "Cáscara de aguacate"
        ]
    )

    st.divider()

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
            "Temperatura de evaporación (°C)",
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

    if st.button("Iniciar simulación"):

        # ---------------------------------------------------
        # DIFERENCIA ENTRE MUESTRAS
        # ---------------------------------------------------

        if tipo_muestra == "Pulpa de aguacate":

            porcentaje_aceite = 0.15

            eficiencia_base = 0.553

        else:

            porcentaje_aceite = 0.05

            eficiencia_base = 0.32

        # ---------------------------------------------------
        # CÁLCULOS
        # ---------------------------------------------------

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
            hexano * 0.80
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

        # ---------------------------------------------------
        # RESULTADOS
        # ---------------------------------------------------

        st.success(
            "Simulación ejecutada correctamente."
        )

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Aceite recuperado",
            f"{aceite_recuperado:.2f} g"
        )

        col2.metric(
            "Rendimiento",
            f"{rendimiento:.2f} %"
        )

        col3.metric(
            "Hexano recuperado",
            f"{hexano_recuperado:.2f} mL"
        )

        st.divider()

        # ---------------------------------------------------
        # VALIDACIÓN
        # ---------------------------------------------------

        st.subheader(
            "Comparación teórica vs simulada"
        )

        rendimiento_teorico = 55.3

        diferencia = (
            rendimiento - rendimiento_teorico
        )

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Resultado simulado",
            f"{rendimiento:.2f} %"
        )

        col2.metric(
            "Resultado teórico",
            f"{rendimiento_teorico:.2f} %"
        )

        col3.metric(
            "Diferencia",
            f"{diferencia:.2f} %"
        )

        st.divider()

        # ---------------------------------------------------
        # RESUMEN
        # ---------------------------------------------------

        st.subheader("Resumen del proceso")

        if rendimiento >= 55:

            st.success(
                "El sistema presenta un rendimiento cercano al valor teórico esperado."
            )

        elif rendimiento >= 40:

            st.warning(
                "El sistema presenta una eficiencia moderada."
            )

        else:

            st.error(
                "El rendimiento obtenido es bajo respecto al esperado."
            )

        st.divider()

        # ---------------------------------------------------
        # SELECTOR DE GRÁFICAS
        # ---------------------------------------------------

        opcion_grafica = st.selectbox(
            "Seleccione la visualización",
            [
                "Solo resultados",
                "Distribución del proceso",
                "Rendimiento vs Temperatura",
                "Comparación teórica"
            ]
        )

        # ---------------------------------------------------
        # GRÁFICA 1
        # ---------------------------------------------------

        if opcion_grafica == "Distribución del proceso":

            etiquetas = [
                "Aceite",
                "Agua",
                "Residuos"
            ]

            valores = [
                aceite_recuperado,
                agua_eliminada,
                residuos
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
        # GRÁFICA 2
        # ---------------------------------------------------

        elif opcion_grafica == "Rendimiento vs Temperatura":

            temperaturas = [50, 60, 70, 75, 80, 90]

            rendimiento_temp = [30, 40, 50, 55.3, 48, 35]

            fig, ax = plt.subplots(
                figsize=(6,4)
            )

            ax.plot(
                temperaturas,
                rendimiento_temp,
                marker='o',
                linewidth=3,
                color="#15803d"
            )

            ax.set_title(
                "Rendimiento vs Temperatura"
            )

            ax.set_xlabel(
                "Temperatura (°C)"
            )

            ax.set_ylabel(
                "Rendimiento (%)"
            )

            ax.grid(True)

            st.pyplot(fig)

        # ---------------------------------------------------
        # GRÁFICA 3
        # ---------------------------------------------------

        elif opcion_grafica == "Comparación teórica":

            categorias = [
                "Simulado",
                "Teórico"
            ]

            valores = [
                rendimiento,
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

            ax.set_title(
                "Comparación de rendimiento"
            )

            st.pyplot(fig)

# ---------------------------------------------------
# PANEL DE CONTROL
# ---------------------------------------------------

elif menu == "Panel de Control":

    st.header("Panel de control industrial")

    st.divider()

    st.subheader("Evaporador")

    temperatura_panel = st.slider(
        "Temperatura de evaporación del hexano (°C)",
        40,
        100,
        75
    )

    st.divider()

    st.subheader("Sistema de lavado")

    ciclos_panel = st.slider(
        "Ciclos de lavado del sistema",
        1,
        15,
        5
    )

    st.divider()

    st.subheader("Muestra procesada")

    humedad_panel = st.slider(
        "Humedad de la muestra (%)",
        0,
        20,
        3
    )

    st.divider()

    st.subheader("Estado operativo")

    if 70 <= temperatura_panel <= 78.5:

        st.success(
            "Temperatura del evaporador estable."
        )

    else:

        st.error(
            "Temperatura fuera de límites operativos."
        )

    if 5 <= ciclos_panel <= 10:

        st.success(
            "Ciclos de lavado adecuados."
        )

    else:

        st.warning(
            "Ciclos fuera del rango recomendado."
        )

    if humedad_panel < 5:

        st.success(
            "Humedad controlada."
        )

    else:

        st.error(
            "Humedad elevada."
        )

# ---------------------------------------------------
# RESULTADOS
# ---------------------------------------------------

elif menu == "Resultados":

    st.header("Resultados generales")

    st.info("""
    Esta sección muestra el análisis general
    del comportamiento del sistema de extracción.
    """)

    st.divider()

    st.metric(
        "Rendimiento teórico de referencia",
        "55.3 %"
    )

    st.metric(
        "Recuperación esperada de hexano",
        "80 %"
    )
    