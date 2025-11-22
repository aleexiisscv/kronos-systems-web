import streamlit as st
from PIL import Image

# --- 1. CONFIGURACIÓN DE LA PÁGINA (Debe ser lo primero) ---
st.set_page_config(
    page_title="KRONOS SYSTEMS | Future Tech",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. CONSTANTES Y CONFIGURACIÓN ---
VALID_PAGES = ["Inicio", "Modelo A (Titan)", "Modelo B (Spark)", "Contacto"]

# --- 3. GESTIÓN DE ESTADO Y NAVEGACIÓN (Lógica del botón Atrás) ---
# Inicializar estado si no existe
if 'page' not in st.session_state:
    st.session_state.page = "Inicio"

# Leer la URL actual
query_params = st.query_params
url_view = query_params.get("view", "Inicio")

# Validar que la vista de la URL sea válida
if url_view not in VALID_PAGES:
    url_view = "Inicio"

# CORE LOGIC: Si la URL es diferente al estado interno, actualizamos y recargamos.
# Esto es lo que hace que el botón "Atrás" del navegador funcione.
if st.session_state.page != url_view:
    st.session_state.page = url_view
    st.rerun()

# Función para actualizar la URL cuando se hace clic en botones
def navigate_to(page_name):
    st.session_state.page = page_name
    st.query_params["view"] = page_name

# Función callback para la barra lateral
def update_url_from_sidebar():
    st.query_params["view"] = st.session_state.page

# --- 4. ESTILOS CSS AVANZADOS ---
st.markdown("""
    <style>
    /* Importar fuente moderna */
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Montserrat', sans-serif;
    }

    /* Estilos Generales */
    h1, h2, h3 { font-weight: 700 !important; }
    
    /* Taglines */
    .tagline-main {
        font-size: 2.5rem; 
        color: #FFFFFF; 
        text-align: center; 
        font-weight: bold; 
        font-style: italic;
        margin-top: -10px; 
        margin-bottom: 20px;
        text-shadow: 0px 0px 10px rgba(0,0,0,0.5);
    }

    /* TARJETAS - MUNDO TITAN (PRO) */
    .pro-card {
        background: linear-gradient(135deg, #0A192F 0%, #162447 100%);
        color: white;
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 10px 25px rgba(10, 25, 47, 0.3);
        border: 1px solid #1F4068;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify_content: center;
    }
    .pro-card h2 { color: #E0E0E0 !important; font-size: 1.8rem; margin-bottom: 10px; }
    .pro-card p { color: #B0C4DE !important; font-size: 1rem; line-height: 1.5; }

    /* TARJETAS - MUNDO SPARK (LITE) */
    .lite-card {
        background: linear-gradient(135deg, #FFFFFF 0%, #FFF3E0 100%);
        color: #333;
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 10px 25px rgba(255, 140, 0, 0.15);
        border: 1px solid #FFCC80;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify_content: center;
    }
    .lite-card h2 { color: #E65100 !important; font-size: 1.8rem; margin-bottom: 10px; }
    .lite-card p { color: #5D4037 !important; font-size: 1rem; line-height: 1.5; }

    /* BOTONES */
    div.stButton > button {
        width: 100%;
        border-radius: 8px;
        height: 3.5em;
        font-weight: 700;
        border: none;
        transition: all 0.3s ease;
    }
    button[key="btn_a_home"], button[key="btn_a"] { background-color: #0A192F; color: white; }
    button[key="btn_b_home"] { background-color: #FF8C00; color: white; }

    </style>
""", unsafe_allow_html=True)

# --- 5. BARRA LATERAL ---
with st.sidebar:
    try:
        st.image("logo.jpeg", use_container_width=True)
    except:
        st.title("KRONOS")
    
    st.markdown("---")
    st.radio(
        "Navegación:", 
        VALID_PAGES, 
        key="page",
        on_change=update_url_from_sidebar # Importante para el historial
    )
    st.markdown("---")
    st.info("🎓 Estrategia: Segmentación Dual")

# --- 6. PÁGINA DE INICIO ---
if st.session_state.page == "Inicio":
    
    # Header con Logo Centrado (Usando columnas 3-2-3)
    col_spacer1, col_logo, col_spacer2 = st.columns([3, 2, 3])
    with col_logo:
        try:
            st.image("logo.jpeg", use_container_width=True) 
        except:
            st.markdown("<h1 style='text-align: center; color: #0A192F;'>KRONOS SYSTEMS</h1>", unsafe_allow_html=True)

    # Tagline Principal (Blanco, Negrita, Cursiva) - Asegúrate que el fondo contraste o usa sombra
    st.markdown('<p class="tagline-main" style="color: #333;">"Tu ambición, nuestro motor."</p>', unsafe_allow_html=True)

    # Video Promocional
    try:
        c_video = st.container()
        with c_video:
            col_l, col_v, col_r = st.columns([1, 3, 1])
            with col_v:
                st.video("video_promo.mp4")
    except:
        st.warning("⚠️ Sube el video 'video_promo.mp4' al repositorio.")

    st.write("###") 

    # Sección de Elección
    st.markdown("<h2 style='text-align: center; font-size: 1.8rem; margin-bottom: 40px; color: #333;'>ELIGE TU REALIDAD</h2>", unsafe_allow_html=True)
    
    col_titan, col_img, col_spark = st.columns([1, 0.05, 1], gap="small")

    with col_titan:
        st.markdown("""
        <div class="pro-card">
            <h2>MUNDO TITAN</h2>
            <p><b>PROFESIONAL / IA</b></p>
            <p>Rendimiento extremo para quienes diseñan el futuro.</p>
        </div>
        """, unsafe_allow_html=True)
        st.write("")
        st.button("EXPLORAR TITAN ➜", on_click=navigate_to, args=("Modelo A (Titan)",), key="btn_a_home")

    with col_spark:
        st.markdown("""
        <div class="lite-card">
            <h2>MUNDO SPARK</h2>
            <p><b>LITE / VERSÁTIL</b></p>
            <p>Todo lo que necesitas. Agilidad y diseño para tu día a día.</p>
        </div>
        """, unsafe_allow_html=True)
        st.write("")
        st.button("EXPLORAR SPARK ➜", on_click=navigate_to, args=("Modelo B (Spark)",), key="btn_b_home")
    
    st.divider()
    
    # KPIs
    c1, c2, c3 = st.columns(3)
    c1.metric("Objetivo Leads", "450/mes", "Marketing Digital")
    c2.metric("Crecimiento", "+18%", "Interanual")
    c3.metric("Posicionamiento", "Top 3", "Sector IA")


# --- 7. PÁGINA MODELO A (TITAN) ---
elif st.session_state.page == "Modelo A (Titan)":
    # Header Estilizado
    st.markdown("""
    <div style="background-color: #0A192F; padding: 40px; border-radius: 15px; text-align: center; margin-bottom: 30px;">
        <h1 style="color: white; font-size: 3.5rem; margin: 0;">KRONOS TITAN</h1>
        <p style="color: #FFFFFF; font-size: 1.8rem; font-weight: bold; font-style: italic;">Potencia que define tu mundo</p>
    </div>
    """, unsafe_allow_html=True)
    
    try:
        st.image("cartel.jpeg", use_container_width=True) 
    except:
        pass

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        <div class="pro-card">
            <h3>🎯 Ficha Estratégica</h3>
            <ul>
                <li><b>Target:</b> Ingenieros, Arquitectos y Desarrolladores IA.</li>
                <li><b>Hardware:</b> Núcleos dedicados para Inteligencia Artificial.</li>
                <li><b>Mensaje:</b> "No aceptes límites".</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.info("💎 **Posicionamiento:** Premium High-End.")
        st.write("La inversión segura para obtener ventaja competitiva.")
        st.progress(98, text="Rendimiento IA")
        st.progress(95, text="Fiabilidad")


# --- 8. PÁGINA MODELO B (SPARK) ---
elif st.session_state.page == "Modelo B (Spark)":
    # Header Estilizado
    st.markdown("""
    <div style="background-color: #FF8C00; padding: 40px; border-radius: 15px; text-align: center; margin-bottom: 30px;">
        <h1 style="color: white; font-size: 3.5rem; margin: 0;">KRONOS SPARK</h1>
        <p style="color: #FFFFFF; font-size: 1.8rem; font-weight: bold; font-style: italic;">Tu día a día, elevado</p>
    </div>
    """, unsafe_allow_html=True)
    
    try:
        st.image("cartel.jpeg", use_container_width=True) 
    except:
        pass

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        <div class="lite-card">
            <h3>🎒 Ficha Estratégica</h3>
            <ul>
                <li><b>Target:</b> Estudiantes y Emprendedores Digitales.</li>
                <li><b>Ventaja:</b> Ligereza y batería optimizada.</li>
                <li><b>Mensaje:</b> "Todo lo que necesitas, al instante".</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.warning("⚡ **Posicionamiento:** Calidad-Precio Imbatible.")
        st.write("Diseño 'Fresh' (Naranja/Blanco) para el público masivo.")
        st.progress(85, text="Portabilidad")
        st.progress(90, text="Autonomía")


# --- 9. PÁGINA CONTACTO ---
elif st.session_state.page == "Contacto":
    c_izq, c_der = st.columns([1, 2])
    with c_izq:
        st.header("Únete")
        st.write("Impulsando la revolución tecnológica.")
        try:
            st.image("logo.jpeg", width=200)
        except:
            pass
    
    with c_der:
        with st.form("lead"):
            st.write("📩 **Suscríbete a la Newsletter**")
            st.text_input("Email")
            st.text_input("Sector")
            st.form_submit_button("ENVIAR")
            st.success("Gracias por tu interés en Kronos Systems.")