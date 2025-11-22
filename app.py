import streamlit as st
from PIL import Image

# --- CONFIGURACIÓN DE ESTADO ---
if 'page' not in st.session_state:
    st.session_state.page = "Inicio"

def navigate_to(page_name):
    st.session_state.page = page_name

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="KRONOS SYSTEMS | Future Tech",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ESTILOS CSS AVANZADOS (SOLUCIÓN DE CONTRASTE) ---
st.markdown("""
    <style>
    /* Importar fuente moderna (Google Fonts) */
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Montserrat', sans-serif;
    }

    /* TÍTULOS */
    h1, h2, h3 {
        font-weight: 700 !important;
    }
    
    /* ESTILO DEL HEADER PRINCIPAL */
    .tagline {
        font-size: 1.5rem; 
        color: #555; 
        text-align: center; 
        font-weight: 300; 
        margin-top: -10px;
        margin-bottom: 20px;
    }

    /* TARJETAS DE PRODUCTO MEJORADAS */
    /* Tarjeta TITAN (Oscura) */
    .pro-card {
        background: linear-gradient(135deg, #0A192F 0%, #1C2E4A 100%);
        color: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        transition: transform 0.3s ease;
        border: 1px solid #333;
        height: 100%;
    }
    .pro-card h2 { color: #F0F0F0 !important; border-bottom: 2px solid #00BFFF; padding-bottom: 10px;}
    .pro-card p { color: #B0C4DE !important; font-size: 1rem;}

    /* Tarjeta SPARK (Clara) */
    .lite-card {
        background: linear-gradient(135deg, #FFFFFF 0%, #FFF5E6 100%);
        color: #333;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        border: 1px solid #FF8C00;
        height: 100%;
    }
    .lite-card h2 { color: #FF4500 !important; border-bottom: 2px solid #FF8C00; padding-bottom: 10px;}
    .lite-card p { color: #555 !important; font-size: 1rem;}

    /* BOTONES PERSONALIZADOS */
    div.stButton > button {
        width: 100%;
        border-radius: 8px;
        height: 3em;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }
    /* Botón Titan */
    button[key="btn_a"] { background-color: #0A192F; color: white; }
    
    /* CENTRADO DE IMÁGENES */
    .img-container {
        display: flex;
        justify_content: center;
    }
    </style>
""", unsafe_allow_html=True)

# --- BARRA LATERAL ---
with st.sidebar:
    # Intentamos cargar el logo, si falla no rompe la app
    try:
        st.image("logo.jpeg", use_container_width=True)
    except:
        st.title("KRONOS")
        
    st.markdown("---")
    st.radio("Navegación:", ["Inicio", "Modelo A (Titan)", "Modelo B (Spark)", "Contacto"], key="page")
    st.markdown("---")
    st.info("🎓 Proyecto Académico\nMarketing & Dirección de Empresas")

# ==========================================
# PÁGINA DE INICIO (REDDISEÑADA)
# ==========================================
if st.session_state.page == "Inicio":
    
    # 1. HEADER CON LOGO Y TAGLINE
    # CAMBIO: Usamos [3, 2, 3] para centrar visualmente. 
    # La columna central (2) es más estrecha, obligando al contenido a quedarse en el medio.
    col_spacer1, col_logo, col_spacer2 = st.columns([3, 2, 3])
    
    with col_logo:
        # Logo principal centrado
        try:
            # Usamos 'use_container_width=True' para que llene la columna central (que ya está centrada)
            st.image("logo.jpeg", use_container_width=True) 
        except:
            st.markdown("<h1 style='text-align: center; color: #0A192F;'>KRONOS SYSTEMS</h1>", unsafe_allow_html=True)

    st.markdown('<p class="tagline" style="color: #FFFFFF; font-size: 2.5rem;">"Tu ambición, nuestro motor."</p>', unsafe_allow_html=True)

    # 2. VIDEO HERO (Cinemático)
    # Video centrado y con ancho fijo (no ocupa todo el ancho)
    try:
        col_l, col_vid, col_r = st.columns([1, 2, 1])
        with col_vid:
            st.video("video_promo.mp4", width=640)  # ajustar ancho en píxeles según necesidad
    except Exception:
        st.warning("⚠️ Archivo 'video_promo.mp4' no encontrado. Súbelo al repositorio.")

    st.markdown("###") # Espaciador

    # 3. SECCIÓN DE ELECCIÓN (DOBLE REALIDAD)
    st.markdown("<h2 style='text-align: center; margin-bottom: 30px;'>ELIGE TU REALIDAD</h2>", unsafe_allow_html=True)
    
    col_titan, col_img, col_spark = st.columns([1, 0.8, 1], gap="large")

    with col_titan:
        st.markdown("""
        <div class="pro-card">
            <h2>MUNDO TITAN</h2>
            <p><b>PROFESIONAL / IA</b></p>
            <p>"Diseñado para lo imposible". Rendimiento extremo para arquitectura, ingeniería y modelado 3D.</p>
            <br>
        </div>
        """, unsafe_allow_html=True)
        st.button("EXPLORAR TITAN ➜", on_click=navigate_to, args=("Modelo A (Titan)",), key="btn_a_home")

    with col_img:
        # Imagen central vertical (Opcional, si queda muy cargado se puede quitar)
        try:
            st.image("cartel.jpeg", caption="Campaña Visual Key", use_container_width=True)
        except:
            st.write("Visual Key")

    with col_spark:
        st.markdown("""
        <div class="lite-card">
            <h2>MUNDO SPARK</h2>
            <p><b>LITE / VERSÁTIL</b></p>
            <p>"Todo lo que necesitas". Agilidad, diseño fresco y potencia optimizada para tu día a día.</p>
            <br>
        </div>
        """, unsafe_allow_html=True)
        st.button("EXPLORAR SPARK ➜", on_click=navigate_to, args=("Modelo B (Spark)",), key="btn_b_home")

    st.divider()
    
    # 4. KPIs / OBJETIVOS (Toque Académico)
    kpi1, kpi2, kpi3 = st.columns(3)
    kpi1.metric(label="Objetivo Leads/Mes", value="450+", delta="Estrategia Digital")
    kpi2.metric(label="Crecimiento Ventas", value="18%", delta="Anual")
    kpi3.metric(label="Rotación Stock", value="Alta", delta="Sell-out")


# ==========================================
# PÁGINA MODELO A (TITAN)
# ==========================================
elif st.session_state.page == "Modelo A (Titan)":
    st.markdown('<p class="tagline" style="color: #FFFFFF; font-size: 4rem;">"*KRONOS TITAN*"</p>', unsafe_allow_html=True)
    st.markdown('<p class="tagline" style="color: #FFFFFF; font-size: 2rem; font-weight: bold; font-style: italic;">Potencia que define tu mundo</p>', unsafe_allow_html=True)
    # Banner Heroico para el producto
    try:
        st.image("image_pro.png", width=None, use_container_width=True) # Reusamos el cartel o una imagen especifica
    except:
        pass

    c1, c2 = st.columns([1, 1])
    with c1:
        st.markdown("""
        <div class="pro-card" style="margin-top: 20px;">
            <h3>Ficha Técnica Estratégica</h3>
            <ul>
                <li><b>Target:</b> Profesionales 30-55 años (Ingenieros, Arquitectos).</li>
                <li><b>Key Feature:</b> Aceleración por Hardware para IA.</li>
                <li><b>Posicionamiento:</b> Premium / Alto Rendimiento.</li>
                <li><b>Mensaje:</b> "No aceptes límites".</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with c2:
        st.write("### ¿Por qué Titan?")
        st.write("""
        El **Modelo A** responde a la necesidad de *fiabilidad absoluta*. 
        En un mercado saturado, Titan se diferencia no por precio, sino por **capacidad de cómputo**.
        
        > *"Es una inversión con la que buscan obtener una ventaja competitiva."* 
        """)
        st.progress(95, text="Potencia de Rendimiento")
        st.progress(90, text="Fiabilidad")
        st.progress(60, text="Portabilidad")

# ==========================================
# PÁGINA MODELO B (SPARK)
# ==========================================
elif st.session_state.page == "Modelo B (Spark)":
    st.markdown('<p class="tagline" style="color: #FFFFFF; font-size: 4rem;">"*KRONOS TITAN*"</p>', unsafe_allow_html=True)
    st.markdown('<p class="tagline" style="color: #FFFFFF; font-size: 2rem; font-weight: bold; font-style: italic;">Tu día a día, elevado</p>', unsafe_allow_html=True)
    
        # Banner Heroico para el producto
    try:
        st.image("image_lite.png", width=None, use_container_width=True) # Reusamos el cartel o una imagen especifica
    except:
        pass
    c1, c2 = st.columns([1, 1])
    with c1:
        st.write("### ¿Por qué Spark?")
        st.write("""
        El **Modelo B** ataca el segmento masivo (estudiantes y familias) que busca **calidad-precio** sin sacrificar estilo.
        
        * Diseño ligero para movilidad.
        * Batería optimizada.
        * Estética 'Fresh' (Naranja/Blanco).
        """)
        st.progress(70, text="Potencia de Rendimiento")
        st.progress(85, text="Fiabilidad")
        st.progress(100, text="Portabilidad")

    with c2:
        st.markdown("""
        <div class="lite-card" style="margin-top: 20px;">
            <h3>Ficha Técnica Estratégica</h3>
            <ul>
                <li><b>Target:</b> Gen Z, Estudiantes, Uso Doméstico.</li>
                <li><b>Key Feature:</b> Versatilidad y Diseño.</li>
                <li><b>Posicionamiento:</b> Accessible Premium.</li>
                <li><b>Mensaje:</b> "Todo lo que necesitas, al instante".</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# PÁGINA CONTACTO
# ==========================================
elif st.session_state.page == "Contacto":
    c_izq, c_der = st.columns(2)
    with c_izq:
        st.header("Conecta con KRONOS")
        st.write("Ayúdanos a alcanzar nuestra meta de **5,400 leads anuales**.")
        st.image("logo.jpeg", width=500)
    
    with c_der:
        with st.form("lead_form"):
            st.write("**Formulario de Captación (Simulación)**")
            st.text_input("Nombre")
            st.text_input("Email Corporativo")
            st.selectbox("Sector:", ["Arquitectura/Ingeniería", "Educación", "Retail/Distribución", "Otro"])
            
            submitted = st.form_submit_button("SOLICITAR INFORMACIÓN")
            if submitted:
                st.success("Lead registrado correctamente en el CRM.")