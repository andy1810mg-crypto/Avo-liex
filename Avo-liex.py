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
# TÍTULO
# ---------------------------------------------------

st.title("AVO-LIOEX")
st.subheader("Simulador de extracción de aceite de aguacate Hass")

st.divider()

# ---------------------------------------------------
# MENÚ
# ---------------------------------------------------

menu = st.sidebar.radio(
    "Navegación",
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
    Este simulador permite modelar el proceso de extracción
    sólido-líquido de aceite de aguacate Hass utilizando etanol
    como solvente.

    El usuario puede modificar variables operativas críticas
    para analizar el rendimiento del sistema y la recuperación
    del aceite.
    """)

    st.divider()

    st.info("""
    Instrucciones:
    
    1. Dirígete a la sección 'Simulador'
    2. Ingresa los parámetros del proceso
    3. Ejecuta la simulación
    4. Analiza los resultados obtenidos
    """)

    st.divider()

    col1, col2, col3 = st.columns(3)

    col1.metric("Temperatura óptima", "70 - 78.5 °C")
    col2.metric("Relación sólido-solvente", "1:3 - 1:5")
    col3.metric("Rendimiento esperado", "55.3 %")

# ---------------------------------------------------
# SIMULADOR
# ---------------------------------------------------

elif menu == "Simulador":

    st.header("Simulación del proceso")

    st.write("Ingrese los parámetros operativos del sistema.")

    st.divider()

    # ---------------------------------------------------
    # VARIABLES DE ENTRADA
    # ---------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        masa_aguacate = st.number_input(
            "Masa de aguacate (g)",
            min_value=0.0,
            value=1000.0
        )

        masa_cascara = st.number_input(
            "Masa de cáscara (g)",
            min_value=0.0,
            value=150.0
        )

        humedad = st.slider(
            "Humedad de la pulpa (%)",
            0,
            100,
            75
        )

    with col2:

        etanol = st.number_input(
            "Volumen de etanol (mL)",
            min_value=0.0,
            value=500.0
        )

        temperatura = st.slider(
            "Temperatura de evaporación (°C)",
            40,
            100,
            75
        )

        tiempo = st.slider(
            "Tiempo de extracción (min)",
            1,
            30,
            10
        )

    st.divider()

    st.caption("Rangos recomendados:")
    st.caption("- Temperatura: 70 - 78.5 °C")
    st.caption("- Tiempo de extracción: 5 - 10 min")
    st.caption("- Humedad baja mejora la eficiencia")

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

        aceite_recuperado = aceite_teorico * 0.553

        etanol_recuperado = etanol * 0.80

        rendimiento = (
            aceite_recuperado / aceite_teorico
        ) * 100

        # ---------------------------------------------------
        # RESULTADOS
        # ---------------------------------------------------

        st.success("Simulación completada correctamente.")

        st.divider()

        st.subheader("Resultados obtenidos")

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
                "Temperatura baja: posible disminución del rendimiento."
            )

        else:
            st.success(
                "Temperatura dentro del rango óptimo."
            )

        if tiempo > 10:
            st.warning(
                "Tiempo elevado de extracción."
            )

        else:
            st.success(
                "Tiempo de extracción adecuado."
            )

        if humedad > 80:
            st.error(
                "Humedad excesiva: posible reducción de eficiencia."
            )

        # ---------------------------------------------------
        # GRÁFICA
        # ---------------------------------------------------

        st.divider()

        st.subheader("Distribución estimada del proceso")

        etiquetas = [
            "Aceite",
            "Agua",
            "Residuos"
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
    Monitoreo de parámetros críticos del sistema.
    """)

    st.divider()

    temperatura_panel = st.slider(
        "Temperatura del sistema",
        40,
        100,
        75
    )

    tiempo_panel = st.slider(
        "Tiempo de extracción",
        1,
        30,
        10
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
        st.success("Sistema térmico estable.")

    else:
        st.error("Temperatura fuera de límites operativos.")

    if 5 <= tiempo_panel <= 10:
        st.success("Tiempo de extracción adecuado.")

    else:
        st.warning("Tiempo fuera del rango recomendado.")

    if humedad_panel < 5:
        st.success("Humedad controlada.")

    else:
        st.error("Humedad elevada.")

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
    Temperaturas mayores pueden afectar la calidad del aceite.
    """)