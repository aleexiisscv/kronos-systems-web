import streamlit as st

# --- CONFIGURACIÓN DE ESTADO (Para que los botones funcionen) ---
if 'page' not in st.session_state:
    st.session_state.page = "Inicio"

def navigate_to(page_name):
    st.session_state.page = page_name

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="KRONOS SYSTEMS | Distribución Oficial",
    page_icon="⚡",
    layout="wide"
)

# --- ESTILOS CSS PERSONALIZADOS (MEJORADO PARA LEGIBILIDAD) ---
st.markdown("""
    <style>
    /* Títulos principales */
    .main-header {
        font-family: 'Helvetica Neue', sans-serif;
        font-size: 3.5rem; 
        color: #0A192F; 
        text-align: center; 
        font-weight: 800;
        letter-spacing: -1px;
    }
    .sub-header {
        font-size: 1.2rem; 
        color: #555; 
        text-align: center;
        margin-bottom: 2rem;
    }
    
    /* MUNDO PRO (Modelo A) - Fondo Azul Marino, Texto Plata/Blanco */
    .pro-card {
        background-color: #0A192F; 
        color: #F0F0F0; /* Texto Plata Claro para contraste */
        padding: 30px; 
        border-radius: 15px; 
        border-left: 5px solid #C0C0C0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    .pro-card h2 { color: #FFFFFF !important; }
    .pro-card h3 { color: #C0C0C0 !important; }
    .pro-card p { color: #E0E0E0 !important; font-size: 1.1rem;}

    /* MUNDO LITE (Modelo B) - Fondo Blanco, Texto Oscuro/Naranja */
    .lite-card {
        background-color: #FFFFFF; 
        color: #333333; 
        padding: 30px; 
        border-radius: 15px; 
        border-right: 5px solid #FF8C00;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .lite-card h2 { color: #FF8C00 !important; }
    
    /* Ajuste de botones nativos de Streamlit */
    div.stButton > button {
        width: 100%;
        border-radius: 5px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# --- BARRA LATERAL DE NAVEGACIÓN ---
st.sidebar.title("Navegación KRONOS")
# El widget radio ahora escucha y actualiza el session_state
st.sidebar.radio(
    "Ir a:", 
    ["Inicio", "Modelo A (Titan)", "Modelo B (Spark)", "Contacto"],
    key="page" # Vincula el widget a la variable de estado
)

# --- LÓGICA DE PÁGINAS ---

# 1. PÁGINA DE INICIO
if st.session_state.page == "Inicio":
    st.markdown('<p class="main-header">KRONOS SYSTEMS</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="sub-header"><i>"Tu ambición, nuestro motor."</i> [cite: 124]</p>', unsafe_allow_html=True)
    
    st.divider()
    
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        # Lado Izquierdo: Mundo PRO [cite: 129]
        st.markdown("""
        <div class="pro-card">
            <h2 style='text-align: center;'>MUNDO PRO / IA</h2>
            <h3 style='text-align: center;'>KRONOS TITAN</h3>
            <hr style='border-color: #555;'>
            <p style='text-align: center; font-style: italic;'>"Diseñado para lo imposible"</p>
            <p style='text-align: center;'>Arquitectura optimizada para Inteligencia Artificial.</p>
            <br>
        </div>
        """, unsafe_allow_html=True)
        # El botón llama a la función para cambiar el estado
        st.button("Explorar Modelo A ➜", on_click=navigate_to, args=("Modelo A (Titan)",))

    with col2:
        # Lado Derecho: Mundo LITE [cite: 135]
        st.markdown("""
        <div class="lite-card">
            <h2 style='text-align: center;'>MUNDO LITE</h2>
            <h3 style='text-align: center;'>KRONOS SPARK</h3>
            <hr style='border-color: #FF8C00;'>
            <p style='text-align: center; font-style: italic;'>"Todo lo que necesitas, al instante"</p>
            <p style='text-align: center;'>Versatilidad inteligente y diseño premium.</p>
            <br>
        </div>
        """, unsafe_allow_html=True)
        st.button("Explorar Modelo B ➜", on_click=navigate_to, args=("Modelo B (Spark)",))

    st.info("💡 Proyecto académico: Plan de Comunicación Integral. [cite: 3]")

# 2. PÁGINA MODELO A
elif st.session_state.page == "Modelo A (Titan)":
    st.markdown("# KRONOS TITAN")
    st.markdown("### *La herramienta definitiva para la era de la IA*")
    
    c1, c2 = st.columns([1, 1])
    with c1:
        # Placeholder más profesional
        st.image("image_pro.png", 
                 caption="Entorno de alto rendimiento y renderizado 3D")
    with c2:
        st.markdown("""
        <div class="pro-card">
            <h3>Especificaciones Estratégicas</h3>
            <ul>
                <li><b>Target:</b> Ingenieros, Arquitectos y Data Scientists[cite: 60].</li>
                <li><b>Ventaja:</b> Potencia de cálculo superior para algoritmos de IA[cite: 107].</li>
                <li><b>Promesa:</b> Fiabilidad total. Cero interrupciones.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        st.warning("💰 **Posicionamiento:** Solución Premium de alta inversión.")

# 3. PÁGINA MODELO B
elif st.session_state.page == "Modelo B (Spark)":
    st.markdown("# KRONOS SPARK")
    st.markdown("### *Tu compañero diario: ligero, rápido y capaz*")
    
    c1, c2 = st.columns([1, 1])
    with c1:
        st.markdown("""
        <div class="lite-card">
            <h3>Versatilidad Cotidiana</h3>
            <ul>
                <li><b>Target:</b> Estudiantes y emprendedores digitales[cite: 69].</li>
                <li><b>Ventaja:</b> Optimización y batería para todo el día[cite: 108].</li>
                <li><b>Promesa:</b> La mejor relación calidad-precio del mercado.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        st.success("✅ **Posicionamiento:** Compra inteligente y accesible.")
    with c2:
         st.image("image_lite.png", 
                 caption="Diseño ligero para movilidad total")

# 4. PÁGINA CONTACTO
elif st.session_state.page == "Contacto":
    st.header("Siguiente paso: La Conexión")
    st.write("Impulsando el objetivo de **450 leads/mes** a través de ferias y medios digitales[cite: 54].")
    
    with st.form("lead_form"):
        col_a, col_b = st.columns(2)
        with col_a:
            st.text_input("Nombre Completo")
            st.text_input("Empresa / Universidad")
        with col_b:
            st.selectbox("Interés Principal:", ["Alto Rendimiento (IA)", "Uso General / Estudiante", "Distribución"])
            st.text_input("Correo Electrónico")
        
        st.markdown("**Privacidad:** Tus datos impulsan nuestra innovación.")
        submitted = st.form_submit_button("UNIRSE A KRONOS")
        if submitted:
            st.balloons()
            st.success("¡Registro completado! Bienvenido al futuro. [cite: 50]")