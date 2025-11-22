import streamlit as st

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="KRONOS SYSTEMS | Distribución Oficial",
    page_icon="⚡",
    layout="wide"
)

# --- ESTILOS CSS PERSONALIZADOS (Basado en Identidad Visual [cite: 120, 121, 122]) ---
# Azul Marino Profundo (Corporativo) y Naranja Eléctrico (Modelo B)
st.markdown("""
    <style>
    .main-header {font-size: 3rem; color: #0A192F; text-align: center; font-weight: bold;}
    .sub-header {font-size: 1.5rem; color: #555; text-align: center;}
    .pro-card {background-color: #0A192F; color: #E0E0E0; padding: 20px; border-radius: 10px; border: 1px solid #C0C0C0;}
    .lite-card {background-color: #FFFFFF; color: #333; padding: 20px; border-radius: 10px; border: 1px solid #FF8C00;}
    .highlight {color: #FF4500; font-weight: bold;}
    </style>
""", unsafe_allow_html=True)

# --- BARRA LATERAL DE NAVEGACIÓN ---
st.sidebar.title("Navegación")
page = st.sidebar.radio("Ir a:", ["Inicio", "Modelo A (Titan)", "Modelo B (Spark)", "Contacto"])

# --- PÁGINA DE INICIO: CONCEPTO DOBLE REALIDAD [cite: 126] ---
if page == "Inicio":
    st.markdown('<p class="main-header">KRONOS SYSTEMS</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="sub-header"><i>"Tu ambición, nuestro motor."</i> [cite: 123]</p>', unsafe_allow_html=True)
    
    st.divider()
    
    # Layout de dos columnas para simular el cartel publicitario [cite: 127]
    col1, col2 = st.columns(2)
    
    with col1:
        # Lado Izquierdo: Mundo PRO/IA [cite: 128]
        st.markdown("""
        <div class="pro-card">
            <h2 style='text-align: center; color: #C0C0C0;'>MUNDO PRO / IA</h2>
            <h3 style='text-align: center;'>KRONOS TITAN</h3>
            <p style='text-align: center;'><i>"Diseñado para lo imposible"</i></p>
            <p>Para ingenieros, arquitectos y creadores que dominan la IA.</p>
            <br>
        </div>
        """, unsafe_allow_html=True)
        st.button("Explorar Modelo A ➜", key="btn_a")

    with col2:
        # Lado Derecho: Mundo LITE [cite: 134]
        st.markdown("""
        <div class="lite-card">
            <h2 style='text-align: center; color: #FF8C00;'>MUNDO LITE</h2>
            <h3 style='text-align: center;'>KRONOS SPARK</h3>
            <p style='text-align: center;'><i>"Todo lo que necesitas, al instante"</i></p>
            <p>Para estudiantes y emprendedores. Versatilidad inteligente.</p>
            <br>
        </div>
        """, unsafe_allow_html=True)
        st.button("Explorar Modelo B ➜", key="btn_b")

    st.info("📢 Simulación académica para la asignatura de Administración de Empresas. [cite: 3]")

# --- PÁGINA MODELO A (PREMIUM) [cite: 128] ---
elif page == "Modelo A (Titan)":
    st.markdown("# KRONOS TITAN: Dominio de la IA")
    st.markdown("### *Arquitectura optimizada para Inteligencia Artificial* [cite: 132]")
    
    c1, c2 = st.columns([1, 2])
    with c1:
        # Aquí iría una imagen generada o placeholder
        st.image("https://placehold.co/400x400/0A192F/C0C0C0?text=KRONOS+TITAN", caption="Estética Premium Dark")
    with c2:
        st.write("""
        **Perfil del Usuario:** Ingenieros, Arquitectos (30-55 años)[cite: 59].
        
        **Propuesta de Valor:**
        * 🚀 **Rendimiento Extremo:** Potencia de cálculo para algoritmos de IA y renderizado 3D[cite: 62].
        * 🛡️ **Fiabilidad Total:** Inversión segura, sin fallos críticos[cite: 63].
        * 💎 **Estatus:** Tecnología punta que te da ventaja competitiva.
        """)
        st.success("Precio justificado por la integración profunda de IA y materiales premium. [cite: 40]")

# --- PÁGINA MODELO B (LITE) [cite: 134] ---
elif page == "Modelo B (Spark)":
    st.markdown("# KRONOS SPARK: Versatilidad Pura")
    st.markdown("### *Todo lo que necesitas, al instante* [cite: 137]")
    
    c1, c2 = st.columns([2, 1])
    with c1:
        st.write("""
        **Perfil del Usuario:** Estudiantes, Familias, Público General[cite: 68].
        
        **Propuesta de Valor:**
        * ⚡ **Agilidad:** Perfecto para el día a día, estudio y entretenimiento[cite: 71].
        * 💰 **Relación Calidad-Precio:** Prestaciones superiores a la media de su gama[cite: 41].
        * 🎨 **Diseño Fresco:** Estilizado y ligero, listo para moverte[cite: 136].
        """)
        st.warning("La mejor opción para quien busca eficiencia sin costes innecesarios.")
    with c2:
        # Placeholder visual con colores naranja/blanco
        st.image("https://placehold.co/400x400/FFFFFF/FF8C00?text=KRONOS+SPARK", caption="Estética Fresh Lite")

# --- PÁGINA DE CONTACTO / OBJETIVOS ---
elif page == "Contacto":
    st.header("Únete a la Revolución KRONOS")
    st.write("Nuestro objetivo es alcanzar **450 leads cualificados al mes**[cite: 53].")
    
    with st.form("lead_form"):
        st.write("Suscríbete para recibir novedades:")
        col_a, col_b = st.columns(2)
        with col_a:
            st.text_input("Nombre")
        with col_b:
            st.selectbox("Me interesa:", ["Modelo A (Profesional)", "Modelo B (Estudiante)"])
        st.text_input("Email")
        
        submitted = st.form_submit_button("Enviar Solicitud")
        if submitted:
            st.balloons()
            st.success("¡Gracias! Tu ambición es nuestro motor. [cite: 123]")
