import streamlit as st
import matplotlib.pyplot as plt

# ---------------------------------------------------
# CONFIGURACIÓN GENERAL
# ---------------------------------------------------

st.set_page_config(
    page_title="AVO-LIOEX",
    layout="wide"
)

# ---------------------------------------------------
# ESTILO VISUAL
# ---------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: #0f1117;
}

h1, h2, h3 {
    color: #E8E8E8;
}

.stMetric {
    background-color: #1c1f26;
    padding: 15px;
    border-radius: 12px;
    border: 1px solid #2d3139;
}

.stButton>button {
    background-color: #4CAF50;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 16px;
}

.stButton>button:hover {
    background-color: #45a049;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# TÍTULO
# ---------------------------------------------------

col1, col2 = st.columns([1,5])

with col1:
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/7/75/Logo_UVG.png",
        width=90
    )

with col2:
    st.title("AVO-LIOEX")
    st.subheader(
        "Simulador de extracción de aceite de aguacate Hass"
    )

st.divider()

# ---------------------------------------------------
# MENÚ
# ---------------------------------------------------

st.sidebar.title("Panel de navegación")

st.sidebar.info(
    "Seleccione una sección del simulador."
)

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

    st.header("Descripción del sistema")

    st.write("""
    El simulador AVO-LIOEX permite modelar el proceso
    de extracción sólido-líquido de aceite de aguacate
    Hass utilizando etanol como solvente.

    El sistema analiza variables críticas del proceso
    para estimar el rendimiento y la producción de aceite.
    """)

    st.divider()

    st.info("""
    Instrucciones de uso:

    1. Ingrese a la sección "Simulador".
    2. Ajuste las variables operativas.
    3. Ejecute la simulación.
    4. Analice los resultados obtenidos.
    """)

    st.divider()

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Temperatura óptima",
        "70 - 78.5 °C"
    )

    col2.metric(
        "Relación sólido-solvente",
        "1:3 - 1:5"
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

    st.write("""
    Ingrese los parámetros operativos del sistema.
    """)

    st.divider()

    # ---------------------------------------------------
    # VARIABLES DE ENTRADA
    # ---------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        masa_aguacate = st.number_input(
            "Masa de aguacate (g)",
            min_value=0.0,
            value=1000.0,
            help="Cantidad total de aguacate procesado."
        )

        masa_cascara = st.number_input(
            "Masa de cáscara (g)",
            min_value=0.0,
            value=150.0,
            help="Cantidad de cáscara removida."
        )

        humedad = st.slider(
            "Humedad de la pulpa (%)",
            0,
            100,
            75,
            help="La humedad afecta directamente la eficiencia."
        )

    with col2:

        etanol = st.number_input(
            "Volumen de etanol (mL)",
            min_value=0.0,
            value=500.0,
            help="Cantidad de solvente utilizada."
        )

        temperatura = st.slider(
            "Temperatura de evaporación (°C)",
            40,
            100,
            75,
            help="Rango recomendado: 70 - 78.5 °C"
        )

        ciclos = st.slider(
            "Ciclos de extracción",
            1,
            15,
            5,
            help="Cantidad de ciclos sólido-solvente realizados."
        )

    st.divider()

    st.caption("Rangos recomendados:")
    st.caption("• Temperatura: 70 - 78.5 °C")
    st.caption("• Ciclos recomendados: 5 - 10")
    st.caption("• Humedad baja mejora el rendimiento")

    st.divider()

    # ---------------------------------------------------
    # BOTÓN DE SIMULACIÓN
    # ---------------------------------------------------

    if st.button("Ejecutar simulación"):

        # ---------------------------------------------------
        # CÁLCULOS
        # ---------------------------------------------------

        masa_pulpa = masa_aguacate - masa_cascara

        agua_eliminada = masa_pulpa * (humedad / 100)

        aceite_teorico = masa_pulpa * 0.15

        # Ajuste dinámico según ciclos

        eficiencia_ciclos = 0.553 + ((ciclos - 5) * 0.015)

        if eficiencia_ciclos > 0.75:
            eficiencia_ciclos = 0.75

        aceite_recuperado = (
            aceite_teorico * eficiencia_ciclos
        )

        etanol_recuperado = etanol * 0.80

        rendimiento = (
            aceite_recuperado / aceite_teorico
        ) * 100

        eficiencia_global = (
            aceite_recuperado / masa_pulpa
        ) * 100

        # ---------------------------------------------------
        # RESULTADOS
        # ---------------------------------------------------

        st.success(
            "Simulación completada correctamente."
        )

        st.divider()

        st.subheader("Resultados del proceso")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Pulpa útil",
            f"{masa_pulpa:.2f} g"
        )

        col2.metric(
            "Aceite recuperado",
            f"{aceite_recuperado:.2f} g"
        )

        col3.metric(
            "Rendimiento",
            f"{rendimiento:.2f} %"
        )

        col4, col5, col6 = st.columns(3)

        col4.metric(
            "Agua eliminada",
            f"{agua_eliminada:.2f} g"
        )

        col5.metric(
            "Etanol recuperado",
            f"{etanol_recuperado:.2f} mL"
        )

        col6.metric(
            "Eficiencia global",
            f"{eficiencia_global:.2f} %"
        )

        st.divider()

        st.success(
            f"Producción estimada de aceite: {aceite_recuperado:.2f} g"
        )

        # ---------------------------------------------------
        # ALERTAS
        # ---------------------------------------------------

        st.divider()

        st.subheader("Estado del sistema")

        if temperatura > 78.5:

            st.error(
                "Temperatura fuera del rango recomendado."
            )

        elif temperatura < 70:

            st.warning(
                "Temperatura baja: posible reducción del rendimiento."
            )

        else:

            st.success(
                "Temperatura dentro del rango óptimo."
            )

        if ciclos > 10:

            st.warning(
                "Número elevado de ciclos: posible aumento energético."
            )

        else:

            st.success(
                "Número de ciclos adecuado."
            )

        if humedad > 80:

            st.error(
                "Humedad excesiva: posible disminución de eficiencia."
            )

        # ---------------------------------------------------
        # GRÁFICA
        # ---------------------------------------------------

        st.divider()

        st.subheader(
            "Distribución estimada del proceso"
        )

        etiquetas = [
            "Aceite",
            "Agua",
            "Cáscara"
        ]

        valores = [
            aceite_recuperado,
            agua_eliminada,
            masa_cascara
        ]

        fig, ax = plt.subplots()

        ax.pie(
            valores,
            labels=etiquetas,
            autopct='%1.1f%%',
            startangle=90
        )

        st.pyplot(fig)

# ---------------------------------------------------
# PANEL DE CONTROL
# ---------------------------------------------------

elif menu == "Panel de Control":

    st.header("Panel de control")

    st.write("""
    Monitoreo de variables críticas del sistema.
    """)

    st.divider()

    temperatura_panel = st.slider(
        "Temperatura del sistema",
        40,
        100,
        75
    )

    ciclos_panel = st.slider(
        "Ciclos de extracción",
        1,
        15,
        5
    )

    humedad_panel = st.slider(
        "Humedad residual",
        0,
        20,
        3
    )

    st.divider()

    st.subheader("Estado operativo")

    if 70 <= temperatura_panel <= 78.5:

        st.success(
            "Sistema térmico estable."
        )

    else:

        st.error(
            "Temperatura fuera de límites operativos."
        )

    if 5 <= ciclos_panel <= 10:

        st.success(
            "Número de ciclos adecuado."
        )

    else:

        st.warning(
            "Número de ciclos fuera del rango recomendado."
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

    st.header("Análisis de resultados")

    st.divider()

    temperaturas = [50, 60, 70, 75, 80, 90]

    rendimiento = [30, 40, 50, 55.3, 48, 35]

    fig, ax = plt.subplots()

    ax.plot(
        temperaturas,
        rendimiento,
        marker='o',
        linewidth=3
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

    st.divider()

    st.info("""
    El rendimiento máximo se obtiene cerca de los 75 °C.
    Temperaturas superiores pueden afectar la calidad del aceite.
    """) 