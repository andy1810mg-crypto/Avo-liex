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
# ESTILO VISUAL PROFESIONAL
# ---------------------------------------------------

st.markdown("""
<style>

/* Fondo principal */

[data-testid="stAppViewContainer"] {

    background:
    linear-gradient(
        135deg,
        #f8faf5,
        #eef7ea,
        #dff3d8
    );
}

/* Sidebar */

[data-testid="stSidebar"] {

    background-color: #f1f5ee;

    border-right: 1px solid #c7d2c0;
}

/* Texto */

html, body, [class*="css"] {

    color: #1f2937;

    font-family: 'Segoe UI', sans-serif;
}

/* Títulos */

h1 {

    color: #14532d;

    font-size: 3rem;

    font-weight: 700;
}

h2, h3 {

    color: #166534;
}

/* Tarjetas */

[data-testid="metric-container"] {

    background-color: rgba(255,255,255,0.85);

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
# HEADER PRINCIPAL
# ---------------------------------------------------

col1, col2, col3 = st.columns([1,3,2])

with col1:

    st.image(
        "images/uvg.jpeg",
        width=110
    )

with col2:

    st.title("AVO-LIOEX")

    st.caption(
        "Sistema de simulación industrial para extracción de aceite de aguacate Hass"
    )

with col3:

    st.image(
        "images/avo.jpeg",
        width=230
    )

st.divider()

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

st.sidebar.title("Panel de navegación")

st.sidebar.caption(
    "Seleccione una sección."
)

st.sidebar.divider()

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
    El simulador AVO-LIOEX modela el proceso de extracción
    sólido-líquido de aceite de aguacate Hass utilizando
    etanol como solvente.
    """)

    st.divider()

    st.info("""
    1. Ingrese al simulador.
    2. Ajuste variables operativas.
    3. Ejecute la simulación.
    4. Analice los resultados.
    """)

    st.divider()

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Temperatura óptima",
        "70 - 78.5 °C"
    )

    col2.metric(
        "Ciclos recomendados",
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

    st.progress(75)

    st.caption(
        "Sistema listo para ejecutar simulación."
    )

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
    # BOTÓN
    # ---------------------------------------------------

    if st.button("Iniciar simulación"):

        # ---------------------------------------------------
        # CÁLCULOS
        # ---------------------------------------------------

        masa_pulpa = masa_aguacate - masa_cascara

        agua_eliminada = masa_pulpa * (humedad / 100)

        aceite_teorico = masa_pulpa * 0.15

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
            "Simulación ejecutada correctamente."
        )

        st.divider()

        st.metric(
            "Producción estimada de aceite",
            f"{aceite_recuperado:.2f} g"
        )

        st.divider()

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Pulpa útil",
            f"{masa_pulpa:.2f} g"
        )

        col2.metric(
            "Agua eliminada",
            f"{agua_eliminada:.2f} g"
        )

        col3.metric(
            "Rendimiento",
            f"{rendimiento:.2f} %"
        )

        col4, col5, col6 = st.columns(3)

        col4.metric(
            "Etanol recuperado",
            f"{etanol_recuperado:.2f} mL"
        )

        col5.metric(
            "Eficiencia global",
            f"{eficiencia_global:.2f} %"
        )

        col6.metric(
            "Ciclos aplicados",
            f"{ciclos}"
        )

        st.divider()

        # ---------------------------------------------------
        # ALERTAS
        # ---------------------------------------------------

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

    temperatura_panel = st.slider(
        "Temperatura",
        40,
        100,
        75
    )

    ciclos_panel = st.slider(
        "Ciclos",
        1,
        15,
        5
    )

    humedad_panel = st.slider(
        "Humedad",
        0,
        20,
        3
    )

    st.divider()

    if 70 <= temperatura_panel <= 78.5:

        st.success(
            "Sistema térmico estable."
        )

    else:

        st.error(
            "Temperatura fuera de límites."
        )

    if 5 <= ciclos_panel <= 10:

        st.success(
            "Ciclos dentro del rango."
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

    st.header("Análisis de resultados")

    temperaturas = [50, 60, 70, 75, 80, 90]

    rendimiento = [30, 40, 50, 55.3, 48, 35]

    fig, ax = plt.subplots()

    ax.plot(
        temperaturas,
        rendimiento,
        marker='o',
        linewidth=3,
        color="#15803d"
    )

    ax.set_facecolor("#ffffff")

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
    