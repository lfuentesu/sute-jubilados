import streamlit as st
import streamlit.components.v1 as components

# Configuración de la página
st.set_page_config(
    page_title="SUTE - Pensionados",
    page_icon="📣",
    layout="wide"
)

# Estilos visuales personalizados (Colores oficiales: Rojo, Blanco, Negro)
st.markdown("""
    <style>
    .main-title {
        color: #D32F2F;
        text-align: center;
        font-weight: bold;
        margin-bottom: 0px;
    }
    .sub-title {
        color: #212121;
        text-align: center;
        font-size: 1.2rem;
        margin-bottom: 25px;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #f1f1f1;
        border-radius: 5px;
        padding-top: 10px;
        padding-bottom: 10px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #D32F2F !important;
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# Encabezado Principal
st.markdown("<h1 class='main-title'>SINDICATO INDEPENDIENTE DE TRABAJADORES DE LA EDUCACIÓN CON DAÑO PREVISIONAL</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='sub-title'>(SUTE - PENSIONADOS)</h3>", unsafe_allow_html=True)

# Pestañas de la aplicación web
tab_inicio, tab_plataforma, tab_estatutos, tab_afiliacion = st.tabs([
    "🏠 Inicio", 
    "📜 Plataforma de Lucha", 
    "📄 Estatutos Oficiales", 
    "✍️ Afiliación"
])

# --- PESTAÑA 1: INICIO ---
with tab_inicio:
    st.header("¡Sindicato Legalmente Constituido!")
    st.write(
        "Estimados compañeros y compañeras: Damos la bienvenida a nuestro sitio oficial. "
        "Nos hemos organizado legalmente para luchar de forma organizada por nuestras demandas previsionales, "
        "el reajuste de pensiones y el fin al daño histórico de los trabajadores de la educación."
    )
    st.info("📌 **Sitio Web Oficial:** https://sute-jubilados.vercel.app")

# --- PESTAÑA 2: PLATAFORMA DE LUCHA ---
with tab_plataforma:
    st.header("Nuestras Demandas")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("1. Demandas Inmediatas")
        st.write("- Reajuste de pensiones (IPC 2 veces al año) + Extraordinario si IPC > 2%.")
        st.write("- Pago de deudas (Cajas y Financieras) - Dividendos < 5% ingresos.")
        
    with col2:
        st.subheader("2. Mediano Plazo")
        st.write("- Eliminación cobro 7% salud + Impuesto a grandes fortunas.")
        st.write("- Estado financia institución de cuidado de pensionados.")
        st.write("- Fondo editorial y socialización de experiencias.")
        
    with col3:
        st.subheader("3. Largo Plazo")
        st.write("- Fin a las AFP.")
        st.write("- Estatización de la educación con financiamiento basal.")
        st.write("- Fin a la carrera docente; reemplazo por carrera funcionaria.")

# --- PESTAÑA 3: ESTATUTOS ---
with tab_estatutos:
    st.header("Estatuto Legal del Sindicato")
    st.write("Aprobado en Asamblea Constitutiva ante el Ministro de Fe de la Inspección del Trabajo.")
    st.write("Consta de 46 artículos en 11 títulos reglamentarios.")

# --- PESTAÑA 4: FORMULARIO DE AFILIACIÓN ---
with tab_afiliacion:
    st.header("✍️ Solicitud de Afiliación")
    st.write(
        "Complete el siguiente formulario con sus datos personales y de contacto para solicitar su "
        "incorporación al **SUTE-Pensionados**. Cada solicitud será revisada y aprobada por el directorio "
        "de acuerdo a lo establecido en los estatutos institucionales."
    )
    st.warning("⚠️ **Requisito:** No ser ni haber sido sostenedor de un establecimiento educacional.")
    
    # ---------------------------------------------------------------------------------------------
    # Reemplaza la siguiente URL con el enlace 'embed' de tu Google Form
    # ---------------------------------------------------------------------------------------------
    URL_FORMULARIO_GOOGLE = "https://docs.google.com/spreadsheets/d/1ZSgVcC3XcjUnDjcboIZy4Kfwwlts3y5_7GW6WjtFHUs/edit?usp=sharing"
    
    # Renderizar el formulario dentro del sitio web
    components.iframe(URL_FORMULARIO_GOOGLE, height=950, scrolling=True)

# Pie de página
st.markdown("---")
st.caption("Sindicato Independiente de Trabajadores de la Educación con Daño Previsional (SUTE-Pensionados) © 2026")