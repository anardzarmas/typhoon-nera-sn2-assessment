import streamlit as st
import datetime
import os
import base64
from fpdf import FPDF

st.set_page_config(
    page_title="Typhoon Technology – NERA Secure Networking",
    layout="wide",
    page_icon="🔒",
)

# ── Rutas de logos ────────────────────────────────────────────────
DIRECTORIO_ACTUAL = os.path.dirname(os.path.abspath(__file__))
logo_typhoon = os.path.join(DIRECTORIO_ACTUAL, "logo_typhoon.jpg")
logo_cisco   = os.path.join(DIRECTORIO_ACTUAL, "logo_cisco.jpg")

def _b64(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except Exception:
        return ""

b64_typhoon = _b64(logo_typhoon)
b64_cisco   = _b64(logo_cisco)

# ── CSS – Manual de Identidad BEST Typhoon ────────────────────────
st.markdown("""
<style>
/* ── Fuentes y base ── */
html, body, [class*="css"] {
    font-family: 'Segoe UI', Arial, sans-serif;
    color: #1A1A2E;
}

/* ── Fondo de la app ── */
.stApp {
    background-color: #F7F9FC;
}

/* ── Ocultar menú hamburguesa y footer Streamlit ── */
#MainMenu, footer { visibility: hidden; }

/* ── Headers ── */
h1 { color: #002B5C !important; font-weight: 800 !important; font-size: 1.9rem !important; }
h2 { color: #002B5C !important; font-weight: 700 !important;
     border-left: 5px solid #FF8F21; padding-left: 12px; margin-top: 1.4rem !important; }
h3 { color: #049FD9 !important; font-weight: 600 !important; font-size: 1.05rem !important; }

/* ── Separador ── */
hr { border: none; border-top: 2px solid #FF8F21; margin: 1.2rem 0; }

/* ── Tabs: lista ── */
.stTabs [data-baseweb="tab-list"] {
    background-color: #002B5C;
    border-radius: 10px 10px 0 0;
    padding: 4px 6px 0;
    gap: 4px;
}

/* ── Tabs: botón inactivo ── */
.stTabs [data-baseweb="tab"] {
    color: #CBD8F0 !important;
    background-color: transparent !important;
    border-radius: 8px 8px 0 0;
    font-weight: 600;
    font-size: 0.82rem;
    padding: 8px 16px;
    border: none !important;
    transition: background 0.2s;
}
.stTabs [data-baseweb="tab"]:hover {
    background-color: rgba(255,143,33,0.25) !important;
    color: #FFFFFF !important;
}

/* ── Tabs: activo ── */
.stTabs [aria-selected="true"] {
    background-color: #FF8F21 !important;
    color: #FFFFFF !important;
    border-radius: 8px 8px 0 0;
}

/* ── Tab panel ── */
.stTabs [data-baseweb="tab-panel"] {
    background-color: #FFFFFF;
    border: 1px solid #DDE4F0;
    border-top: 3px solid #FF8F21;
    border-radius: 0 0 10px 10px;
    padding: 24px 28px;
}

/* ── Inputs y textareas ── */
textarea, input[type="text"], input[type="number"] {
    border: 1px solid #C5D0E8 !important;
    border-radius: 6px !important;
    background-color: #FAFBFF !important;
    color: #1A1A2E !important;
}
textarea:focus, input:focus {
    border-color: #049FD9 !important;
    box-shadow: 0 0 0 2px rgba(4,159,217,0.18) !important;
    color: #1A1A2E !important;
}
/* Streamlit envuelve los inputs en divs con clases dinámicas */
[data-baseweb="textarea"] textarea,
[data-baseweb="input"] input,
.stTextArea textarea,
.stTextInput input {
    color: #1A1A2E !important;
    background-color: #FAFBFF !important;
}

/* ── Labels ── */
label { color: #002B5C !important; font-weight: 600 !important; font-size: 0.88rem !important; }

/* ── Radio y checkbox ── */
[data-testid="stRadio"] label, [data-testid="stMultiSelect"] label {
    font-weight: 400 !important;
    color: #1A1A2E !important;
}

/* ── Selectbox ── */
[data-baseweb="select"] {
    border-color: #C5D0E8 !important;
    border-radius: 6px !important;
}

/* ── Info box ── */
[data-testid="stInfo"] {
    background-color: #EAF4FB !important;
    border-left: 4px solid #049FD9 !important;
    border-radius: 8px !important;
    color: #002B5C !important;
}

/* ── Botón de descarga ── */
.stDownloadButton > button {
    background: linear-gradient(135deg, #002B5C 0%, #049FD9 100%) !important;
    color: #FFFFFF !important;
    font-weight: 700 !important;
    font-size: 1rem !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.65rem 2rem !important;
    box-shadow: 0 4px 14px rgba(0,43,92,0.25) !important;
    transition: opacity 0.2s !important;
}
.stDownloadButton > button:hover { opacity: 0.88 !important; }

/* ── Bloque de markdown de preguntas ── */
[data-testid="stMarkdownContainer"] ul {
    margin-left: 1.1rem;
    color: #2C3E6B;
}
[data-testid="stMarkdownContainer"] p strong {
    color: #002B5C;
}

/* ── Columnas info general ── */
[data-testid="column"] {
    background: #FFFFFF;
    border-radius: 10px;
    padding: 14px 18px !important;
    border: 1px solid #DDE4F0;
}
</style>
""", unsafe_allow_html=True)

# ── HEADER CON LOGOS ──────────────────────────────────────────────
logo_typhoon_tag = (f'<img src="data:image/jpeg;base64,{b64_typhoon}" '
                    f'style="height:48px;object-fit:contain;">'
                    if b64_typhoon else
                    '<span style="color:#FF8F21;font-weight:800;font-size:1.3rem;">BEST Typhoon</span>')

logo_cisco_tag = (f'<img src="data:image/jpeg;base64,{b64_cisco}" '
                  f'style="height:44px;object-fit:contain;">'
                  if b64_cisco else
                  '<span style="color:#049FD9;font-weight:800;font-size:1.3rem;">Cisco</span>')

st.markdown(f"""
<div style="
    background: linear-gradient(90deg,#002B5C 0%,#00407A 100%);
    border-radius: 12px;
    padding: 18px 28px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 24px;
    box-shadow: 0 4px 18px rgba(0,43,92,0.22);
">
    <div style="display:flex;align-items:center;gap:18px;">
        {logo_typhoon_tag}
        <div>
            <div style="color:#FF8F21;font-size:0.75rem;font-weight:700;
                        letter-spacing:2px;text-transform:uppercase;">
                Partner de Cisco
            </div>
            <div style="color:#FFFFFF;font-size:1.35rem;font-weight:800;line-height:1.2;">
                Formulario de Evaluación de Red Segura
            </div>
            <div style="color:#CBD8F0;font-size:0.82rem;margin-top:2px;">
                NERA Secure Networking Assessment · Typhoon Technology
            </div>
        </div>
    </div>
    <div style="display:flex;align-items:center;gap:12px;">
        {logo_cisco_tag}
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown(
    '<p style="color:#4A5568;font-size:0.93rem;margin-bottom:8px;">'
    'Complete este cuestionario simplificado para descubrir la arquitectura de '
    'Enterprise Networking recomendada para sus proyectos.</p>',
    unsafe_allow_html=True
)
st.markdown("---")

# ── 1. INFORMACIÓN GENERAL ────────────────────────────────────────
st.header("Información General del Proyecto")
col1, col2, col3 = st.columns(3)
with col1:
    empresa_nombre    = st.text_input("Nombre de la empresa")
    contacto_cliente  = st.text_input("Contacto principal")
    correo_contacto   = st.text_input("Correo del contacto")
    puesto_contacto   = st.text_input("Puesto")
with col2:
    am_cisco          = st.text_input("AM de Cisco")
    responsable_best  = st.text_input("Responsable de Best")
    fecha_evaluacion  = st.date_input("Fecha de evaluación", datetime.date.today())
with col3:
    vertical_negocio  = st.selectbox(
        "Vertical de negocio",
        ["Finanzas", "Educación", "Salud", "Manufactura", "Retail", "Sector Público", "Otro"]
    )

st.markdown("---")

# ── 2. DOMINIOS DE EVALUACIÓN ─────────────────────────────────────
st.header("Dominios de Evaluación")
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🎯 Estrategia y Visión",
    "🖧 Topología y Operación",
    "📶 Rendimiento (LAN/WLAN/WAN)",
    "🔍 Aseguramiento y Visibilidad",
    "🔒 Seguridad de Red",
])

with tab1:
    st.subheader("1. Estrategia y Visión de la Red")
    st.markdown("**Objetivos y Adopción Tecnológica:**\n* ¿Cuáles son los objetivos estratégicos a 1-3 años y cómo encaja la red?\n* ¿Hay próximos proyectos que requieran cambios en la red?\n* ¿Qué nuevas tecnologías (IoT, IA, 5G) buscan adoptar?\n* ¿Tienen planes de modernizar su arquitectura (SDN, Edge)?")
    est_objetivos = st.text_area("Respuestas:", key="e1", height=100)

    st.markdown("**Presupuesto y Cumplimiento:**\n* ¿Cómo manejan los costos y cómo miden el ROI de la red?\n* ¿Tienen políticas documentadas de seguridad de red?\n* ¿Existen nuevos estándares de la industria o compliance por cumplir?")
    est_presupuesto = st.text_area("Respuestas:", key="e2", height=100)

    st.markdown("**Trabajo Remoto y Continuidad:**\n* ¿Cómo controlan y aseguran el acceso a la nube para remotos?\n* ¿Cómo se alinea la red con sus planes de Disaster Recovery?\n* ¿Tienen iniciativas de sostenibilidad y eficiencia energética?")
    est_remoto = st.text_area("Respuestas:", key="e3", height=100)

    st.markdown("**Nube, Gestión y Proveedores:**\n* ¿Existen desafíos para integrar servicios en la nube a la red?\n* ¿Hay planes para implementar automatización o herramientas de gestión con IA?\n* ¿Están satisfechos con sus proveedores actuales o abiertos a nuevas asociaciones?")
    est_nube = st.text_area("Respuestas:", key="e4", height=100)

with tab2:
    st.subheader("2. Topología, Configuración y Operación")
    st.markdown("**Estado de la Topología:**\n* ¿Cuál es el layout físico y lógico (switches, routers, APs, firewalls)?\n* ¿Existen equipos en End-of-Life (EOL) o cuellos de botella identificados?\n* ¿Cómo gestionan y protegen los dispositivos actuales?")
    top_estado = st.text_area("Respuestas:", key="t1", height=100)

    st.markdown("**Conectividad e Integración:**\n* ¿Cómo se conectan los sitios (WAN, MPLS, VPN)?\n* ¿Qué servicios de nube o integraciones de terceros debe soportar la red?\n* ¿Qué nivel de redundancia requieren los componentes críticos?")
    top_conectividad = st.text_area("Respuestas:", key="t2", height=100)

    st.markdown("**Operación y Mantenimiento:**\n* ¿Cuáles son los requisitos operativos (staffing, entrenamiento)?\n* ¿Cuál es el proceso para actualizar software y parches (Patch Management)?\n* ¿Cómo documentan e informan los cambios de red?")
    top_operacion = st.text_area("Respuestas:", key="t3", height=100)

    st.markdown("**Presupuesto y Selección tecnológica:**\n* ¿Cuál es el presupuesto para el proyecto de red o actualizaciones?\n* ¿Existen restricciones de costos en el diseño?\n* ¿Hay proveedores o tecnologías preferidas para el equipamiento?")
    top_presupuesto = st.text_area("Respuestas:", key="t4", height=100)

with tab3:
    st.subheader("3. Rendimiento de Red (Switching, Routing, Wireless)")
    st.markdown("**Métricas y Tráfico:**\n* ¿Cuáles son las métricas base (ancho de banda, latencia, jitter, packet loss)?\n* ¿Tienen políticas QoS para priorizar aplicaciones críticas?\n* ¿Han reportado los usuarios lentitud o degradación en ciertos horarios?")
    ren_metricas = st.text_area("Respuestas:", key="r1", height=100)

    st.markdown("**Estrategia Wireless:**\n* ¿Cómo manejan el acceso de invitados y políticas BYOD?\n* ¿Tienen políticas para mitigar Rogue APs e interferencias?\n* ¿Qué estándares (ej. Wi-Fi 6) y controladores usan actualmente?")
    ren_wireless = st.text_area("Respuestas:", key="r2", height=100)

    st.markdown("**Estrategia Routing y Switching:**\n* ¿Implementan Local Breakouts para acceso directo a internet?\n* ¿Cómo aseguran el transporte de datos entre sucursales?\n* ¿Tienen planes para implementar automatización tipo Fabric (SD-Access)?")
    ren_routing = st.text_area("Respuestas:", key="r3", height=100)

    st.markdown("**Energía y Aplicaciones:**\n* ¿Cómo rastrean y gestionan actualmente su consumo de energía (ej. software, excel, manual)?\n* ¿Existen SLAs específicos para aplicaciones críticas?\n* ¿Cómo impactaría al negocio una caída de estas aplicaciones?")
    ren_energia = st.text_area("Respuestas:", key="r4", height=100)

    col_poe, col_smart = st.columns(2)
    with col_poe:
        st.markdown("**Requerimientos de Energía (PoE)**")
        poe_req = st.radio("Requisitos máximos de clase PoE requeridos:", [
            "15.4W (PoE - IEEE 802.3af)", "30W (PoE+ - IEEE 802.3at)",
            "60W (UPOE/PoE++ - IEEE 802.3bt)", "90W (UPoE+/PoE+++ - IEEE 802.3bt)",
            "Sin requerimientos PoE", "Otro"
        ])
    with col_smart:
        st.markdown("**Edificios Inteligentes (Smart Buildings)**")
        smart_build = st.multiselect("Áreas que se beneficiarían de Smart Buildings:", [
            "Eficiencia Energética (iluminación y HVAC)", "Seguridad y Control de Acceso",
            "Calidad del Aire Interior", "Gestión de Ocupación", "Mantenimiento Preventivo"
        ])

with tab4:
    st.subheader("4. Aseguramiento (Assurance) y Visibilidad")
    st.markdown("**Herramientas y Alcance:**\n* ¿Qué plataformas usan para visibilidad y análisis de tráfico?\n* ¿Existen puntos ciegos o retos para rastrear dispositivos BYOD/IoT?\n* ¿Cómo manejan la visibilidad en ambientes híbridos (Cloud/On-premise)?")
    vis_herramientas = st.text_area("Respuestas:", key="v1", height=100)

    st.markdown("**KPIs y Análisis:**\n* ¿Qué KPIs y SLAs son más importantes para su organización?\n* ¿Requieren monitoreo de anomalías en tiempo real o histórico?\n* ¿Cómo miden la satisfacción del usuario final con la red?")
    vis_kpis = st.text_area("Respuestas:", key="v2", height=100)

    st.markdown("**Respuesta a Incidentes:**\n* ¿Cuál es el proceso para detectar, diagnosticar y resolver incidentes?\n* ¿Cómo se integran sus herramientas con sistemas IT (SIEM, ITSM)?\n* ¿Buscan adoptar IA/Machine Learning para optimizar la red?")
    vis_incidentes = st.text_area("Respuestas:", key="v3", height=100)

    st.markdown("**Reportes, Escalabilidad y Presupuesto:**\n* ¿Qué tipos de reportes generan y qué stakeholders los revisan?\n* ¿Puede su solución actual escalar para crecimientos futuros?\n* ¿Cuál es el presupuesto para soluciones de assurance y cómo evalúan su ROI?")
    vis_reportes = st.text_area("Respuestas:", key="v4", height=100)

with tab5:
    st.subheader("5. Seguridad de Red")
    st.markdown("**Arquitectura y Protección:**\n* ¿Qué diseño de arquitectura de seguridad y firewalls tienen?\n* ¿Cómo protegen y encriptan los datos sensibles en tránsito?\n* ¿Cómo descubren vulnerabilidades y parchean equipos perimetrales?")
    seg_medidas = st.text_area("Respuestas:", key="s1", height=100)

    st.markdown("**Control de Accesos (NAC):**\n* ¿Qué métodos usan para autenticación (802.1X, MAB, TrustSec)?\n* ¿Cómo segmentan la red para empleados, invitados y dispositivos IoT?\n* ¿Cómo aseguran el acceso de terceros o proveedores a la Extranet?")
    seg_acceso = st.text_area("Respuestas:", key="s2", height=100)

    st.markdown("**Monitoreo de Amenazas:**\n* ¿Qué sistemas usan para monitorear incidentes de seguridad de red?\n* ¿Han experimentado brechas recientes?\n* ¿Cómo manejan la gobernanza y políticas de seguridad?")
    seg_monitoreo = st.text_area("Respuestas:", key="s3", height=100)

    st.markdown("**Riesgos, Entrenamiento y Presupuesto:**\n* ¿Tienen un proceso formal de gestión de riesgos (Risk Management)?\n* ¿Proporcionan entrenamiento de ciberseguridad a sus empleados?\n* ¿Cuál es su presupuesto para seguridad y cómo priorizan las inversiones?")
    seg_riesgos = st.text_area("Respuestas:", key="s4", height=100)

st.markdown("---")

# ── 3. SIGUIENTES PASOS ───────────────────────────────────────────
st.header("Siguientes Pasos y Soluciones Cisco")
st.info(
    "💡 **Recomendación preliminar:**\n\n"
    "Con base en la información capturada, sugerimos diseñar una arquitectura **Cisco Secure Networking**.\n"
    "🔗 **Portafolio Oficial de Soluciones:** [https://www.cisco.com/site/us/en/products/index.html](https://www.cisco.com/site/us/en/products/index.html)\n\n"
    "*(Nota: Esta información es previa a los comentarios y validación de un profesional preventa).*"
)
st.markdown("<br>", unsafe_allow_html=True)

# ── FUNCIONES PDF (sin cambios) ───────────────────────────────────
def clean_text(text):
    if not text or str(text).strip() == "": return "No especificado"
    replacements = {
        'á':'a','é':'e','í':'i','ó':'o','ú':'u',
        'Á':'A','É':'E','Í':'I','Ó':'O','Ú':'U',
        'ñ':'n','Ñ':'N','¿':'?','¡':'!','\u2013':'-','\u2014':'-'
    }
    texto_limpio = str(text)
    for s, r in replacements.items():
        texto_limpio = texto_limpio.replace(s, r)
    return texto_limpio.encode('latin-1', 'ignore').decode('latin-1')

def generar_analisis_dinamico():
    recomendaciones = []
    recomendaciones.append(
        "- Cisco Catalyst 9000 Series (Switching & Routing)\n"
        "Al requerir una infraestructura de red moderna y escalable, los equipos Catalyst proporcionan alto rendimiento, capacidades Zero-Trust integradas y telemetria avanzada para soportar las operaciones de red."
    )
    if str(ren_wireless).strip() != "":
        recomendaciones.append(
            "- Cisco Catalyst Wireless / Cisco Meraki\n"
            "Para soportar la estrategia inalambrica, politicas BYOD y acceso de invitados, los Access Points de Cisco proporcionan alta densidad, seguridad WPA3 y mitigacion de interferencias con gestion centralizada."
        )
    if smart_build and len(smart_build) > 0:
        recomendaciones.append(
            "- Cisco Spaces\n"
            "Para cumplir con las iniciativas de Smart Buildings identificadas, Cisco Spaces actua como puente entre la red inalambrica y los sistemas del edificio, proveyendo analiticos de ocupacion, monitoreo ambiental y seguridad fisica."
        )
    if str(vis_herramientas).strip() != "" or str(vis_incidentes).strip() != "":
        recomendaciones.append(
            "- Cisco ThousandEyes & Catalyst Center\n"
            "Dado el requerimiento de visibilidad de extremo a extremo y monitoreo de incidentes, estas plataformas eliminan los puntos ciegos mediante inteligencia de red proactiva y automatizacion impulsada por IA."
        )
    if str(seg_acceso).strip() != "":
        recomendaciones.append(
            "- Cisco Identity Services Engine (ISE)\n"
            "Para implementar el control de acceso a la red (NAC) y segmentacion estricta, ISE centraliza y unifica el control de politicas de seguridad, asegurando que solo usuarios y dispositivos autorizados ingresen al entorno."
        )
    if str(seg_medidas).strip() != "":
        recomendaciones.append(
            "- Cisco Secure Firewall\n"
            "Para asegurar la arquitectura perimetral y proteger los datos en transito, la implementacion de Secure Firewall ofrece defensa inteligente contra amenazas e inspeccion profunda de paquetes."
        )
    if str(est_remoto).strip() != "":
        recomendaciones.append(
            "- Cisco Secure Access (SSE) / Cisco Catalyst SD-WAN\n"
            "Para cubrir las necesidades de la fuerza laboral remota y la gestion de nubes hibridas, esta arquitectura garantiza conectividad segura y optimizada hacia las aplicaciones core y SaaS."
        )
    return "\n\n".join(recomendaciones)

def generar_pdf():
    # ── Paleta de colores ──────────────────────────────────────────
    C_DARK   = (60,  60,  60)
    C_MGRAY  = (80,  80,  80)
    C_ORANGE = (255, 143, 0)
    C_LGRAY  = (245, 245, 245)
    C_WHITE  = (255, 255, 255)
    C_TEXT   = (50,  50,  50)

    PAGE_W  = 210
    LM      = 15
    CONT_W  = 180   # 210 - 15 - 15

    # ── Clase PDF con header/footer de marca ──────────────────────
    class NERAP(FPDF):
        def header(self):
            # Barra gris oscura
            self.set_fill_color(*C_DARK)
            self.rect(0, 0, PAGE_W, 22, 'F')
            # Logo Typhoon izquierda
            try:
                if os.path.exists(logo_typhoon):
                    self.image(logo_typhoon, x=5, y=2, h=18)
            except Exception:
                pass
            # Logo Cisco derecha
            try:
                if os.path.exists(logo_cisco):
                    self.image(logo_cisco, x=171, y=3, h=16)
            except Exception:
                pass
            # Texto central
            self.set_font("Arial", 'I', 9)
            self.set_text_color(*C_ORANGE)
            self.set_xy(55, 8)
            self.cell(100, 6, txt="BECOME. EVOLVE. SUCCEED. THRIVE.", align='C')
            # Barra naranja delgada
            self.set_fill_color(*C_ORANGE)
            self.rect(0, 22, PAGE_W, 1.5, 'F')
            # Reset
            self.set_text_color(*C_TEXT)
            self.set_xy(LM, 28)

        def footer(self):
            # Barra gris oscura en pie
            self.set_fill_color(*C_DARK)
            self.rect(0, 274, PAGE_W, 23, 'F')
            self.set_font("Arial", '', 6.5)
            self.set_text_color(190, 190, 190)
            self.set_xy(10, 278)
            self.cell(190, 4,
                      txt="Corporativo Sentura, Perif. Blvd. Manuel Avila Camacho 2610,"
                          " 54040 Tlalnepantla, Mex.",
                      align='C')
            self.set_font("Arial", 'B', 7)
            self.set_text_color(*C_ORANGE)
            self.set_xy(10, 283)
            self.cell(190, 4,
                      txt=f"www.best.org.mx  |  Soporte: 55 5350 9600  |  Pagina {self.page_no()}",
                      align='C')

    pdf = NERAP()
    pdf.set_auto_page_break(auto=True, margin=32)
    pdf.set_margins(LM, 28, LM)
    pdf.add_page()
    pdf.set_text_color(*C_TEXT)

    # ── Helpers ────────────────────────────────────────────────────
    def sec_header(title):
        """Caja gris oscura con acento naranja izquierdo."""
        y = pdf.get_y()
        pdf.set_fill_color(*C_ORANGE)
        pdf.rect(LM, y, 3, 8, 'F')
        pdf.set_fill_color(*C_MGRAY)
        pdf.rect(LM + 3, y, CONT_W - 3, 8, 'F')
        pdf.set_font("Arial", 'B', 11)
        pdf.set_text_color(*C_WHITE)
        pdf.set_xy(LM + 7, y + 1.5)
        pdf.cell(CONT_W - 7, 6, txt=clean_text(title))
        pdf.ln(11)
        pdf.set_text_color(*C_TEXT)

    def sub_title(title):
        """Título de sub-sección en naranja bold."""
        pdf.set_font("Arial", 'B', 10)
        pdf.set_text_color(*C_ORANGE)
        pdf.set_x(LM)
        pdf.cell(CONT_W, 7, txt=clean_text(title))
        pdf.ln()
        pdf.set_text_color(*C_TEXT)

    def info_row(label, value):
        """Fila label-valor para información general."""
        pdf.set_x(LM)
        pdf.set_font("Arial", 'B', 9)
        pdf.cell(52, 6, txt=clean_text(label))
        pdf.set_font("Arial", '', 9)
        pdf.set_x(LM + 52)
        pdf.cell(CONT_W - 52, 6, txt=clean_text(str(value)))
        pdf.ln()

    def qa_block(num, titulo, bullets, respuesta):
        """Bloque Q&A con fondo gris claro."""
        pdf.set_fill_color(*C_LGRAY)
        # Título de la pregunta
        pdf.set_font("Arial", 'B', 9)
        pdf.set_text_color(*C_TEXT)
        pdf.set_x(LM)
        pdf.multi_cell(CONT_W, 5, txt=clean_text(f"{num}. {titulo}:"), fill=True)
        # Sub-bullets
        pdf.set_font("Arial", '', 9)
        for b in bullets:
            pdf.set_x(LM + 3)
            pdf.multi_cell(CONT_W - 3, 4.5, txt=clean_text(f"- {b}"), fill=True)
        # Respuesta
        resp_val = clean_text(respuesta) if respuesta and str(respuesta).strip() else "Sin respuesta"
        pdf.set_font("Arial", 'I', 9)
        pdf.set_text_color(100, 100, 100)
        pdf.set_x(LM)
        pdf.multi_cell(CONT_W, 4.5, txt=f"Respuesta: {resp_val}", fill=True)
        pdf.set_text_color(*C_TEXT)
        pdf.ln(3)

    # ══════════════════════════════════════════════════════════════
    # PÁGINA 1 — Portada e Información General
    # ══════════════════════════════════════════════════════════════
    # Título principal
    pdf.set_font("Arial", 'B', 16)
    pdf.set_text_color(*C_TEXT)
    pdf.set_x(LM)
    pdf.cell(CONT_W, 10,
             txt="Assessment: Secure Networking - BEST Typhoon Technologies",
             align='C')
    pdf.ln()

    # Sub-título naranja
    pdf.set_font("Arial", 'I', 10)
    pdf.set_text_color(*C_ORANGE)
    pdf.set_x(LM)
    empresa_str = clean_text(empresa_nombre) if empresa_nombre.strip() else "Sin empresa"
    pdf.cell(CONT_W, 7,
             txt=f"Formulario NERA  |  {str(fecha_evaluacion)}  |  {empresa_str}",
             align='C')
    pdf.ln(10)
    pdf.set_text_color(*C_TEXT)

    # 1. Información General
    sec_header("1. Informacion General")
    info_row("Empresa:",            empresa_nombre)
    info_row("Contacto:",           contacto_cliente)
    info_row("Correo contacto:",    correo_contacto)
    info_row("Puesto:",             puesto_contacto)
    info_row("AM Cisco:",           am_cisco)
    info_row("Responsable Best:",   responsable_best)
    info_row("Vertical de negocio:", vertical_negocio)
    info_row("Fecha de evaluacion:", str(fecha_evaluacion))
    pdf.ln(6)

    # 2. Análisis Preliminar
    sec_header("2. Analisis Preliminar")
    pdf.set_font("Arial", '', 9)
    pdf.set_text_color(*C_TEXT)
    pdf.set_x(LM)
    pdf.multi_cell(CONT_W, 5, txt=clean_text(generar_analisis_dinamico()))
    pdf.ln(5)

    # ══════════════════════════════════════════════════════════════
    # PÁGINAS 2+ — Resultados del Assessment
    # ══════════════════════════════════════════════════════════════
    pdf.add_page()
    sec_header("3. Resultados del Assessment")
    pdf.ln(2)

    # ── Estrategia y Vision ────────────────────────────────────────
    sub_title("Estrategia y Vision de la Red")
    qa_block(1, "Objetivos y Adopcion Tecnologica",
        ["Cuales son los objetivos estrategicos a 1-3 anos y como encaja la red?",
         "Hay proximos proyectos que requieran cambios en la red?",
         "Que nuevas tecnologias (IoT, IA, 5G) buscan adoptar?",
         "Tienen planes de modernizar su arquitectura (SDN, Edge)?"],
        est_objetivos)
    qa_block(2, "Presupuesto y Cumplimiento",
        ["Como manejan los costos y como miden el ROI de la red?",
         "Tienen politicas documentadas de seguridad de red?",
         "Existen nuevos estandares de la industria o compliance por cumplir?"],
        est_presupuesto)
    qa_block(3, "Trabajo Remoto y Continuidad",
        ["Como controlan y aseguran el acceso a la nube para remotos?",
         "Como se alinea la red con sus planes de Disaster Recovery?",
         "Tienen iniciativas de sostenibilidad y eficiencia energetica?"],
        est_remoto)
    qa_block(4, "Nube, Gestion y Proveedores",
        ["Existen desafios para integrar servicios en la nube a la red?",
         "Hay planes para implementar automatizacion o herramientas de gestion con IA?",
         "Estan satisfechos con sus proveedores actuales o abiertos a nuevas asociaciones?"],
        est_nube)

    # ── Topología ─────────────────────────────────────────────────
    sub_title("Topologia, Configuracion y Operacion")
    qa_block(5, "Estado de la Topologia",
        ["Cual es el layout fisico y logico (switches, routers, APs, firewalls)?",
         "Existen equipos en End-of-Life (EOL) o cuellos de botella identificados?",
         "Como gestionan y protegen los dispositivos actuales?"],
        top_estado)
    qa_block(6, "Conectividad e Integracion",
        ["Como se conectan los sitios (WAN, MPLS, VPN)?",
         "Que servicios de nube o integraciones de terceros debe soportar la red?",
         "Que nivel de redundancia requieren los componentes criticos?"],
        top_conectividad)
    qa_block(7, "Operacion y Mantenimiento",
        ["Cuales son los requisitos operativos (staffing, entrenamiento)?",
         "Cual es el proceso para actualizar software y parches (Patch Management)?",
         "Como documentan e informan los cambios de red?"],
        top_operacion)
    qa_block(8, "Presupuesto y Seleccion tecnologica",
        ["Cual es el presupuesto para el proyecto de red o actualizaciones?",
         "Existen restricciones de costos en el diseno?",
         "Hay proveedores o tecnologias preferidas para el equipamiento?"],
        top_presupuesto)

    # ── Rendimiento ───────────────────────────────────────────────
    sub_title("Rendimiento de Red (LAN/WLAN/WAN)")
    qa_block(9, "Metricas y Trafico",
        ["Cuales son las metricas base (ancho de banda, latencia, jitter, packet loss)?",
         "Tienen politicas QoS para priorizar aplicaciones criticas?",
         "Han reportado los usuarios lentitud o degradacion en ciertos horarios?"],
        ren_metricas)
    qa_block(10, "Estrategia Wireless",
        ["Como manejan el acceso de invitados y politicas BYOD?",
         "Tienen politicas para mitigar Rogue APs e interferencias?",
         "Que estandares (ej. Wi-Fi 6) y controladores usan actualmente?"],
        ren_wireless)
    qa_block(11, "Estrategia Routing y Switching",
        ["Implementan Local Breakouts para acceso directo a internet?",
         "Como aseguran el transporte de datos entre sucursales?",
         "Tienen planes para implementar automatizacion tipo Fabric (SD-Access)?"],
        ren_routing)
    qa_block(12, "Energia y Aplicaciones",
        ["Como rastrean y gestionan actualmente su consumo de energia?",
         "Existen SLAs especificos para aplicaciones criticas?",
         "Como impactaria al negocio una caida de estas aplicaciones?"],
        ren_energia)
    qa_block(13, "Requerimientos de Energia (PoE)",
        ["Cuales son los requisitos maximos de clase PoE requeridos?"],
        poe_req)
    smart_build_str = ", ".join(smart_build) if smart_build else "Sin seleccion"
    qa_block(14, "Edificios Inteligentes (Smart Buildings)",
        ["Que areas se beneficiarian? Seleccione todos los que correspondan."],
        smart_build_str)

    # ── Aseguramiento ─────────────────────────────────────────────
    sub_title("Aseguramiento y Visibilidad")
    qa_block(15, "Herramientas y Alcance",
        ["Que plataformas usan para visibilidad y analisis de trafico?",
         "Existen puntos ciegos o retos para rastrear dispositivos BYOD/IoT?",
         "Como manejan la visibilidad en ambientes hibridos (Cloud/On-premise)?"],
        vis_herramientas)
    qa_block(16, "KPIs y Analisis",
        ["Que KPIs y SLAs son mas importantes para su organizacion?",
         "Requieren monitoreo de anomalias en tiempo real o historico?",
         "Como miden la satisfaccion del usuario final con la red?"],
        vis_kpis)
    qa_block(17, "Respuesta a Incidentes",
        ["Cual es el proceso para detectar, diagnosticar y resolver incidentes?",
         "Como se integran sus herramientas con sistemas IT (SIEM, ITSM)?",
         "Buscan adoptar IA/Machine Learning para optimizar la red?"],
        vis_incidentes)
    qa_block(18, "Reportes, Escalabilidad y Presupuesto",
        ["Que tipos de reportes generan y que stakeholders los revisan?",
         "Puede su solucion actual escalar para crecimientos futuros?",
         "Cual es el presupuesto para soluciones de assurance y como evaluan su ROI?"],
        vis_reportes)

    # ── Seguridad ─────────────────────────────────────────────────
    sub_title("Seguridad de Red")
    qa_block(19, "Arquitectura y Proteccion",
        ["Que diseno de arquitectura de seguridad y firewalls tienen?",
         "Como protegen y encriptan los datos sensibles en transito?",
         "Como descubren vulnerabilidades y parchean equipos perimetrales?"],
        seg_medidas)
    qa_block(20, "Control de Accesos (NAC)",
        ["Que metodos usan para autenticacion (802.1X, MAB, TrustSec)?",
         "Como segmentan la red para empleados, invitados y dispositivos IoT?",
         "Como aseguran el acceso de terceros o proveedores a la Extranet?"],
        seg_acceso)
    qa_block(21, "Monitoreo de Amenazas",
        ["Que sistemas usan para monitorear incidentes de seguridad de red?",
         "Han experimentado brechas recientes?",
         "Como manejan la gobernanza y politicas de seguridad?"],
        seg_monitoreo)
    qa_block(22, "Riesgos, Entrenamiento y Presupuesto",
        ["Tienen un proceso formal de gestion de riesgos (Risk Management)?",
         "Proporcionan entrenamiento de ciberseguridad a sus empleados?",
         "Cual es su presupuesto para seguridad y como priorizan las inversiones?"],
        seg_riesgos)

    # ══════════════════════════════════════════════════════════════
    # ÚLTIMA PÁGINA — Soluciones Cisco Recomendadas
    # ══════════════════════════════════════════════════════════════
    pdf.add_page()
    sec_header("4. Soluciones Cisco Recomendadas")
    pdf.ln(3)

    recs = [r.strip() for r in generar_analisis_dinamico().split("\n\n") if r.strip()]
    for rec in recs:
        partes = rec.split("\n", 1)
        producto = partes[0]
        descripcion = partes[1] if len(partes) > 1 else ""
        pdf.set_font("Arial", 'B', 10)
        pdf.set_text_color(*C_ORANGE)
        pdf.set_x(LM)
        pdf.multi_cell(CONT_W, 6, txt=clean_text(producto))
        if descripcion:
            pdf.set_font("Arial", '', 9)
            pdf.set_text_color(*C_TEXT)
            pdf.set_x(LM + 4)
            pdf.multi_cell(CONT_W - 4, 5, txt=clean_text(descripcion))
        pdf.ln(3)

    # Nota al pie en caja
    pdf.ln(5)
    pdf.set_fill_color(*C_LGRAY)
    pdf.set_font("Arial", 'I', 8.5)
    pdf.set_text_color(80, 80, 80)
    pdf.set_x(LM)
    pdf.multi_cell(CONT_W, 5,
        txt=clean_text(
            "Nota: Esta informacion es preliminar y queda sujeta a validacion tecnica "
            "por parte de un profesional preventa o arquitecto certificado de BEST Typhoon."
        ),
        border=1, fill=True)

    result = pdf.output(dest='S')
    if isinstance(result, (bytes, bytearray)):
        return bytes(result)
    return result.encode('latin-1', 'replace')


# ── BOTÓN DE DESCARGA ─────────────────────────────────────────────
pdf_bytes = None
try:
    pdf_bytes = generar_pdf()
except Exception as e:
    st.error(f"Error al compilar el PDF: {e}")

if pdf_bytes:
    nombre_archivo_pdf = "NERA_Assessment_SN.pdf"
    if empresa_nombre.strip():
        nombre_archivo_pdf = f"NERA_Assessment_SN_{empresa_nombre.strip()}.pdf"

    st.download_button(
        label="📄 Descargar PDF Completo del Formulario NERA",
        data=pdf_bytes,
        file_name=nombre_archivo_pdf,
        mime="application/pdf",
        use_container_width=True,
    )

# ── FOOTER ────────────────────────────────────────────────────────
st.markdown(f"""
<div style="
    margin-top: 40px;
    background: linear-gradient(90deg,#002B5C 0%,#00407A 100%);
    border-radius: 10px;
    padding: 14px 28px;
    display: flex;
    align-items: center;
    justify-content: space-between;
">
    <span style="color:#CBD8F0;font-size:0.78rem;">
        © 2026 BEST Typhoon Technologies &nbsp;·&nbsp; Cisco Partner &nbsp;·&nbsp; Confidencial
    </span>
    <div style="display:flex;align-items:center;gap:14px;">
        {logo_typhoon_tag}
        {logo_cisco_tag}
    </div>
</div>
""", unsafe_allow_html=True)
