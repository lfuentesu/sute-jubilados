import streamlit as st
import streamlit.components.v1 as components

# Configuración de la página
st.set_page_config(
    page_title="SUTE - Pensionados",
    page_icon="📣",
    layout="wide"
)

# Estilos visuales personalizados (Colores oficiales: Azul, Blanco, Rojo)
st.markdown("""
    <style>
    .main-title {
        color: #0A438B;
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
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 45px;
        background-color: #f1f1f1;
        border-radius: 5px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #0A438B !important;
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# Encabezado Principal
st.markdown("<h1 class='main-title'>SUTE JUBILADOS / SUTE-PENSIONADOS</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='sub-title'>Sindicato Único de Trabajadores de la Educación - Sección Jubilados</h3>", unsafe_allow_html=True)

# Pestañas de la aplicación web
tab_noticias, tab_galeria, tab_literatura, tab_documentos, tab_afiliacion, tab_contacto = st.tabs([
    "📰 Noticias", 
    "📷 Galería", 
    "📚 Literatura", 
    "📄 Documentos", 
    "✍️ Afiliación",
    "✉️ Contacto"
])

# --- PESTAÑA: NOTICIAS ---
with tab_noticias:
    st.header("¡Sindicato Legalmente Constituido!")
    st.write(
        "Estimados compañeros y compañeras: Damos la bienvenida a nuestro sitio oficial. "
        "Nos hemos organizado legalmente para luchar por nuestras demandas previsionales, "
        "el reajuste de pensiones y el fin al daño histórico de los trabajadores de la educación."
    )

# --- PESTAÑA: GALERÍA ---
with tab_galeria:
    st.header("Galería de Actividades")
    st.write("Registro fotográfico de nuestras asambleas y encuentros.")

# --- PESTAÑA: LITERATURA ---
with tab_literatura:
    st.header("Espacio Cultural y Literatura")
    st.write("Publicaciones, artículos y creaciones de los asociados.")

# --- PESTAÑA: DOCUMENTOS ---
with tab_documentos:
    st.header("Documentos y Estatutos Oficiales")
    st.write("Estatuto Legal y actas constitutivas del sindicato.")

# --- PESTAÑA: AFILIACIÓN (NUEVA) ---
with tab_afiliacion:
    st.header("✍️ Solicitud de Afiliación")
    st.write(
        "Complete el siguiente formulario con sus datos personales y de contacto para solicitar su "
        "incorporación al **SUTE-Pensionados**. Cada solicitud será revisada y aprobada por la directiva."
    )
    st.warning("⚠️ **Requisito:** No ser ni haber sido sostenedor de un establecimiento educacional.")
    
    # ---------------------------------------------------------------------------------------------
    # Reemplaza la siguiente URL con el enlace 'embed' de tu Google Form
    # ---------------------------------------------------------------------------------------------
    URL_FORMULARIO_GOOGLE = "https://docs.google.com/forms/d/e/git add admin/app.py
git commit -m "Actualizar formulario de afiliacion en admin"
git push origin main/viewform?embedded=true"
    
    components.iframe(URL_FORMULARIO_GOOGLE, height=950, scrolling=True)

# --- PESTAÑA: CONTACTO ---
with tab_contacto:
    st.header("Contacto y Colaboraciones")
    st.write("Canales oficiales de comunicación con el directorio.")

# Pie de página
st.markdown("---")
st.caption("Sindicato Único de Trabajadores de la Educación - Sección Jubilados / SUTE-Pensionados © 2026")