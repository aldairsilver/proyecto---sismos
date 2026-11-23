import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Catálogo Sísmico del Perú", layout="wide")
st.title("Catálogo Sísmico del Perú (1960-2025)")

# Leer los datos
df = pd.read_csv("data/catalogo_sismico.csv", encoding="latin-1", sep=";")

# Año del sismo y periodo de 5 años (ej. 1963 -> 1960)
df["AÑO"] = df["FECHA_UTC"].astype(str).str[:4].astype(int)
df["PERIODO"] = df["AÑO"] // 5 * 5


def grafico(datos):
    """Dibuja las barras de sismos por periodo de 5 años."""
    if datos.empty:
        st.warning("No hay sismos en ese rango.")
        return

    conteo = datos["PERIODO"].value_counts().sort_index().reset_index()
    conteo.columns = ["PERIODO", "SISMOS"]

    fig = px.bar(conteo, x="PERIODO", y="SISMOS",
                 labels={"PERIODO": "Año de inicio del periodo (cada 5 años)",
                         "SISMOS": "Cantidad de sismos"})
    fig.update_traces(marker_color="#D6E0F5", marker_line_color="black",
                      marker_line_width=1, width=3)
    fig.update_xaxes(dtick=5, tickangle=-90)
    fig.update_layout(template="plotly_white")
    st.plotly_chart(fig, use_container_width=True)

    mejor = conteo.loc[conteo["SISMOS"].idxmax()]
    st.info(f"El periodo con más sismos fue {int(mejor['PERIODO'])}-"
            f"{int(mejor['PERIODO']) + 4} ({int(mejor['SISMOS'])} sismos).")
def texto(contenido):
    """Párrafo con letra más grande y justificado."""
    st.markdown(
        f"<p style='font-size:18px; line-height:1.7; text-align:justify'>{contenido}</p>",
        unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Descripción",
    "Magnitud",
    "Profundidad",
    "Distribución de Magnitudes",
    "Mapa de calor sísmico"
])

# TAB 1: descripción y contexto
with tab1:
    # ----- Descripción del problema -----
    st.header("Descripción del problema")
    col_texto, col_img = st.columns([5, 3], vertical_alignment="center")
    with col_texto:
        texto(
            "El Perú es uno de los países con mayor actividad sísmica del mundo debido a su "
            "ubicación en el Cinturón de Fuego del Pacífico. Esta condición lo expone "
            "constantemente a terremotos de diferentes magnitudes y profundidades, que pueden "
            "generar importantes consecuencias sociales, económicas y ambientales."
        )
        texto(
            "Comprender el comportamiento de los sismos registrados a lo largo del tiempo "
            "permite identificar patrones de actividad sísmica, reconocer los periodos de mayor "
            "ocurrencia de eventos de gran magnitud y analizar las características de los "
            "movimientos telúricos. Esta información resulta fundamental para comprender el "
            "riesgo sísmico del territorio peruano y contribuir a una mejor planificación de la "
            "prevención y gestión del riesgo de desastres."
        )
        texto(
            "Este proyecto analiza más de 24 000 registros sísmicos del Instituto Geofísico del "
            "Perú (IGP), correspondientes al periodo 1960-2025, mediante herramientas de análisis "
            "y visualización de datos. Se estudian principalmente dos variables: la magnitud y la "
            "profundidad de los sismos, con el propósito de identificar tendencias y responder "
            "preguntas como: ¿en qué periodos se registraron los sismos de mayor magnitud?, "
            "¿qué profundidades presentan con mayor frecuencia? y ¿cómo se distribuye la "
            "actividad sísmica en el territorio peruano?"
        )
    with col_img:
        st.image("imagenes/cinturon_de_fuego.png",
                 caption="Cinturón de Fuego del Pacífico. Fuente: (escribe aquí la fuente)")

    st.divider()

        # ----- Contexto geológico -----
        # ----- Contexto geológico -----
    st.header("Contexto geológico")
    col_texto, col_img = st.columns([5, 3], vertical_alignment="center")
    with col_texto:
        texto(
            "La actividad sísmica del Perú está estrechamente relacionada con el proceso de "
            "subducción, en el cual la placa de Nazca se introduce por debajo de la placa "
            "Sudamericana. Este movimiento genera acumulación y liberación de energía en el "
            "interior de la Tierra, originando gran parte de los terremotos que ocurren en el país."
        )
        texto(
            "Este proceso provoca fricción entre ambas placas tectónicas, acumulando tensiones "
            "que, al liberarse repentinamente, generan ondas sísmicas que se propagan por la "
            "corteza terrestre. Debido a esta dinámica, el Perú forma parte del Cinturón de Fuego "
            "del Pacífico, una de las zonas con mayor actividad sísmica del mundo."
        )
        texto(
            "Además, la interacción de estas placas contribuye a la formación de la cordillera de "
            "los Andes y a la actividad volcánica del sur del país. Por ello, es importante "
            "estudiar los movimientos sísmicos para identificar las zonas de mayor riesgo y "
            "establecer medidas de prevención que permitan reducir los daños materiales y la "
            "pérdida de vidas humanas."
        )
    with col_img:
        st.image("imagenes/subduccion_real.png",
                 caption="Ilustración referencial de la subducción de la placa de Nazca. "
                         "Fuente: (escribe aquí la fuente)")

    col_texto, col_img = st.columns([5, 3], vertical_alignment="center")
    with col_texto:
        texto(
            "Cada registro sísmico contiene información relevante, como la fecha, hora, "
            "ubicación geográfica, magnitud y profundidad del evento. Estas variables permiten "
            "caracterizar los sismos y analizar sus principales características, identificando "
            "patrones en su ocurrencia y distribución dentro del territorio peruano."
        )
        texto(
            "Mediante el análisis de estos datos, es posible reconocer las regiones con mayor "
            "actividad sísmica, comparar la magnitud de los eventos e identificar los periodos en "
            "los que se registraron mayores movimientos. Asimismo, la información geográfica "
            "permite visualizar la distribución de los sismos y relacionarla con las principales "
            "zonas de actividad tectónica del país."
        )
        texto(
            "De esta manera, el proyecto busca transformar los registros históricos en información "
            "comprensible e interactiva, facilitando la exploración y el estudio de la actividad "
            "sísmica del Perú durante el periodo 1960-2025. Esto permitirá comprender mejor el "
            "comportamiento sísmico del territorio y resaltar la importancia del análisis de datos "
            "para la prevención y gestión del riesgo de desastres."
        )
    with col_img:
        st.image("imagenes/sismografo.png",
                 caption="Monitoreo sísmico (imagen referencial). Fuente: (escribe aquí la fuente)")
# TAB 2: gráfico por magnitud
with tab2:
    rango = st.selectbox("Rango escala de Richter",
                         ["Menor a 5", "5 a 5.9", "6 a 6.9", "7 o más"], index=2)

    if rango == "Menor a 5":
        datos = df[df["MAGNITUD"] < 5]
    elif rango == "5 a 5.9":
        datos = df[(df["MAGNITUD"] >= 5) & (df["MAGNITUD"] < 6)]
    elif rango == "6 a 6.9":
        datos = df[(df["MAGNITUD"] >= 6) & (df["MAGNITUD"] < 7)]
    else:
        datos = df[df["MAGNITUD"] >= 7]

    grafico(datos)

# TAB 3: gráfico por profundidad
with tab3:
    prof = st.selectbox("Rango de profundidad",
                        ["Superficial (hasta 70 km)",
                         "Intermedia (71 a 300 km)",
                         "Profunda (más de 300 km)"])

    if prof.startswith("Superficial"):
        datos = df[df["PROFUNDIDAD"] <= 70]
    elif prof.startswith("Intermedia"):
        datos = df[(df["PROFUNDIDAD"] > 70) & (df["PROFUNDIDAD"] <= 300)]
    else:
        datos = df[df["PROFUNDIDAD"] > 300]

    grafico(datos)

# TAB 4: distribución de magnitudes por año
with tab4:
    st.header("Distribución de sismos según magnitud")
    st.write("Selecciona un año para visualizar la proporción "
             "de sismos registrados según su magnitud.")

    anios = sorted(df["AÑO"].dropna().astype(int).unique())
    anio_seleccionado = st.selectbox("Selecciona el año:", anios, index=len(anios) - 1)

    datos_anio = df[df["AÑO"] == anio_seleccionado].copy()

    datos_anio["RANGO"] = pd.cut(
        datos_anio["MAGNITUD"],
        bins=[float("-inf"), 5, 6, 7, float("inf")],
        labels=["Menor a 5", "5 a 5.9", "6 a 6.9", "7 o más"],
        right=False
    )

    conteo_anio = datos_anio["RANGO"].value_counts().reset_index()
    conteo_anio.columns = ["Magnitud", "Cantidad"]

    if conteo_anio["Cantidad"].sum() > 0:
        fig_pie = px.pie(
            conteo_anio,
            names="Magnitud",
            values="Cantidad",
            title=f"Sismos registrados en {anio_seleccionado}"
        )
        fig_pie.update_traces(textposition="inside", textinfo="percent")
        st.plotly_chart(fig_pie, use_container_width=True)

        st.subheader("Tabla de resultados")
        st.dataframe(conteo_anio, hide_index=True, use_container_width=True)
    else:
        st.warning("No hay registros para este año.")

# TAB 5: mapa de calor sísmico
with tab5:
    st.header("Mapa de calor de los sismos en el Perú")
    st.write("Este mapa muestra las zonas donde se concentran "
             "los sismos registrados en el Perú entre 1960 y 2025.")

    rango_anios = st.slider("Selecciona el rango de años", 1960, 2025, (1960, 2025))
    mag_minima = st.slider("Magnitud mínima", 0.0, 9.0, 5.0, 0.5)

    datos_mapa = df[
        (df["AÑO"] >= rango_anios[0]) &
        (df["AÑO"] <= rango_anios[1]) &
        (df["MAGNITUD"] >= mag_minima)
    ].copy()

    datos_mapa["LATITUD"] = pd.to_numeric(datos_mapa["LATITUD"], errors="coerce")
    datos_mapa["LONGITUD"] = pd.to_numeric(datos_mapa["LONGITUD"], errors="coerce")
    datos_mapa = datos_mapa.dropna(subset=["LATITUD", "LONGITUD"])

    if not datos_mapa.empty:
        fig_mapa = px.density_map(
            datos_mapa,
            lat="LATITUD",
            lon="LONGITUD",
            radius=15,
            center={"lat": -9.2, "lon": -75},
            zoom=4,
            map_style="open-street-map",
            color_continuous_scale="YlOrRd"
        )
        fig_mapa.update_layout(height=600, margin=dict(l=0, r=0, t=0, b=0))
        st.plotly_chart(fig_mapa, use_container_width=True)
    else:
        st.warning("No hay sismos para estos filtros.")