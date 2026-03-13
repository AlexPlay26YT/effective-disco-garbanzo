import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="The IA Among Us",
    page_icon="🧠",
    layout="centered"
)

# 1. Estilos CSS (Mantenemos tu diseño minimalista)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .main-title {
        font-size: 42px;
        font-weight: 700;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 10px;
    }

    .quote-container {
        text-align: right;
        font-style: italic;
        color: #6B7280;
        margin-bottom: 40px;
        padding-right: 10px;
        border-right: 3px solid #3B82F6;
    }

    /* Estilo para el contenedor del artículo */
    [.element-container]:has(div.article-content) {
        background-color: #F9FAFB;
        border: 1px solid #E5E7EB;
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    
    .highlight-text {
        background-color: #EFF6FF;
        border-left: 4px solid #3B82F6;
        padding: 15px;
        margin: 20px 0;
        border-radius: 5px;
        text-align: center;
        font-weight: 500;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ENCABEZADO ---
st.markdown('<h1 class="main-title">The IA Among Us like Kerosene in Oil</h1>', unsafe_allow_html=True)

st.markdown("""
    <div class="quote-container">
        “Saber usar la IA en la actualidad es como saber escribir, respirar o comer; <br>
        todos saben hacerlo pero no todos lo llegan a hacer del todo bien”
    </div>
    """, unsafe_allow_html=True)

# --- CUERPO DEL ARTÍCULO (FORMATO PROSA/MARKDOWN) ---

# Usamos st.container con una clase personalizada para el borde redondeado
with st.container(border=True): # El parámetro border=True crea el recuadro redondeado automáticamente en versiones modernas
    
    st.markdown("## ¿Un algoritmo en el diván? Cómo la Inteligencia Artificial se ha convertido en el nuevo aliado de la psicología")
    
    st.write("""
    En un mundo donde el estrés y la ansiedad parecen ser la norma, la demanda de ayuda profesional ha crecido más rápido que la capacidad de los sistemas de salud para responder. Ante esta "crisis de atención", ha surgido un invitado inesperado en la consulta: la Inteligencia Artificial (IA).

    Pero, ¿realmente puede un código de programación entender el sufrimiento humano? La ciencia sugiere que no se trata de reemplazar al psicólogo, sino de darle **"superpoderes"** para que pueda enfocarse en lo que mejor sabe hacer: conectar con el paciente.
    """)

    st.markdown("### 1. Más que simples máquinas: Un apoyo en la crisis")
    st.write("""
    La IA en salud mental se define como la capacidad de los sistemas tecnológicos para aprender, razonar y resolver problemas complejos. Actualmente, no se utiliza para sustituir el criterio del profesional, sino para procesar cantidades masivas de información —como historias clínicas digitales, patrones en redes sociales o incluso escalas de humor— que a un humano le tomaría años analizar. El objetivo es claro: ofrecer diagnósticos más objetivos y menos dependientes de la subjetividad del momento.
    """)

    st.markdown("### 2. El \"ojo clínico\" potenciado por datos")
    st.write("""
    Uno de los mayores retos de la psicología es la precisión en el diagnóstico, especialmente cuando los síntomas de diferentes trastornos se solapan. Aquí es donde entra el **Machine Learning** (o aprendizaje automático), una rama de la IA que identifica patrones invisibles al ojo humano.
    """)
    
    st.markdown("""
    * **Precisión sorprendente:** Estudios recientes indican que estos modelos alcanzan una precisión diagnóstica del 85%, superando en exactitud a muchos enfoques tradicionales.
    * **Herramientas en acción:** Plataformas como Limbic Access o Censeo ya están ayudando a clasificar a los pacientes desde su primer contacto, reduciendo los tiempos de espera.
    """)

    st.markdown("### 3. Terapia en el bolsillo: El auge de los acompañantes virtuales")
    st.write("""
    ¿Puede un "chatbot" ser empático? Aunque parezca ciencia ficción, herramientas como **Woebot, Wysa o Youper** ya aplican técnicas de Terapia Cognitivo-Conductual directamente en el teléfono del usuario. 
    
    Un caso avanzado es **CaiTI**, un terapeuta basado en modelos de lenguaje extenso que monitorea hasta 37 dimensiones del funcionamiento diario de una persona. Estos sistemas no solo escuchan; validan las emociones del usuario en tiempo real.
    """)

    st.markdown("### 4. Menos papeleo, más presencia humana")
    st.write("""
    Plataformas como **Eholo, Texta AI o Mentalyc** están cambiando las reglas del juego al automatizar la transcripción de sesiones y la generación de notas clínicas. Al delegar estas tareas repetitivas a la IA, el terapeuta puede centrar toda su atención y energía en la persona que tiene enfrente.
    """)

    # Recuadro destacado
    st.markdown('<div class="highlight-text">"La IA no busca reemplazar al facultativo, sino complementar su práctica clínica para ofrecer diagnósticos más objetivos".</div>', unsafe_allow_html=True)

    st.markdown("### 5. El dilema del \"Elemento Humano\"")
    st.write("""
    A pesar de estos avances, surge una pregunta inevitable: ¿Se perderá la calidez de la terapia? Existe la preocupación de que la tecnología erosione la **"alianza terapéutica"**, ese vínculo de confianza entre paciente y profesional que es vital para la cura.
    
    Sin embargo, la evidencia sugiere que, si se usa de forma ética, la IA libera al profesional para que pueda ejercer la empatía con mayor libertad.
    """)

    st.markdown("### 6. Los retos del futuro: Privacidad y Ética")
    st.write("""
    No todo es color de rosa. El uso de IA en psicología enfrenta desafíos críticos:
    * **Privacidad:** La confidencialidad de los datos sensibles es la piedra angular de la confianza.
    * **Sesgos algorítmicos:** Es vital asegurar que los algoritmos no hereden prejuicios y funcionen igual de bien para todas las personas.
    """)

# --- SECCIÓN DE REFERENCIAS ---
st.write("---")
st.subheader("📚 Referencias Bibliográficas")

referencias = {
    "Graham, S. et al. (2019) - AI for Mental Health": """
        **Resumen:** La tecnología de la inteligencia artificial (IA) representa tanto una gran promesa para transformar la atención a la salud mental como posibles riesgos. 
        Este artículo ofrece una visión general de la IA y sus aplicaciones actuales en la salud, sugiriendo que puede ayudar a redefinir las enfermedades mentales 
        de manera más objetiva que el DSM-5 e identificarlas en etapas tempranas.
    """,
    "Rollwage, M. et al. (2023) - Conversational AI Efficiency": """
        **Resumen:** Este estudio examina cómo las soluciones digitales basadas en IA ayudan a los profesionales a usar su tiempo de manera más eficiente, 
        reduciendo la presión sobre los servicios y mejorando los resultados clínicos de los pacientes en el mundo real.
    """,
    "Rauf, M. et al. (2025) - Integrating AI in Clinical Psychology": """
        **Resumen:** Explora la perspectiva de los profesionales sobre cómo la IA incrementa la precisión diagnóstica. Se centra en desvelar el nivel de conocimiento 
        actual de los psicólogos sobre la IA y los factores que influyen en su adopción.
    """,
    "de la Fuente Tambo & Armayones Ruiz (2025) - La IA en la Práctica Psicológica": """
        **Resumen:** Revisión de 12 herramientas de IA disponibles en psicología asistencial. Concluye que, aunque no todas cumplen con criterios de seguridad, 
        existen opciones establecidas que ayudan en tareas administrativas permitiendo al terapeuta centrarse en casos complejos.
    """,
    "Beg, M. J. et al. (2025) - AI for Psychotherapy Review": """
        **Resumen:** Revisión narrativa sobre aplicaciones de IA en psicoterapia, centrándose en trastornos depresivos y de ansiedad. 
        Analiza mecanismos de eficacia y las persistentes preocupaciones éticas sobre su integración.
    """,
    "Gual-Montolio, P. et al. (2022) - AI for Emotional Problems": """
        **Resumen:** Revisión sistemática sobre el uso de IA para proporcionar recomendaciones en tiempo real basadas en la respuesta del paciente. 
        Busca optimizar el tratamiento para ese 40% de pacientes que no responden a la terapia tradicional.
    """,
    "Rony, M. K. K. et al. (2025) - AI in Psychiatry Systematic Review": """
        **Resumen:** Meta-análisis que evalúa la precisión diagnóstica y eficacia terapéutica de la IA en psiquiatría, 
        ofreciendo soluciones innovadoras al solapamiento de síntomas y la necesidad de personalización.
    """,
    "Rebelo, A. D. et al. (2023) - Impact on Mental Healthcare Workers": """
        **Resumen:** Explora cómo la IA mejora los procesos diagnósticos y los enfoques personalizados desde la perspectiva del trabajador de salud mental 
        y su utilidad en la práctica diaria.
    """,
    "Cruz-Gonzalez, P. et al. (2025) - AI in Diagnosis and Monitoring": """
        **Resumen:** Revisión sistemática que demuestra la precisión de las herramientas de IA en la detección, clasificación y predicción de riesgos, 
        así como en el monitoreo del pronóstico continuo de trastornos mentales.
    """,
    "Pacheco, C. R. & Scheeringa, M. S. (2022) - Clinical Wisdom in App Age": """
        **Resumen:** Analiza aplicaciones móviles comerciales para trastornos psiquiátricos. Concluye que cuatro funciones clínicas clave pueden 
        potenciarse significativamente, aunque el pleno potencial de procesamiento aún no se ha alcanzado.
    """
}

# Selector de referencias
seleccion = st.selectbox("Selecciona un artículo para ver su resumen:", list(referencias.keys()))

if seleccion:
    st.info(referencias[seleccion])

# Footer
st.markdown("<br><p style='text-align: center; color: #9CA3AF;'>Dashboard de Divulgación Científica - 2026</p>", unsafe_allow_html=True)
