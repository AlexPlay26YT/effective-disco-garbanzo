import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="The IA Amoung Us",
    page_icon="🧠",
    layout="centered"
)

# Estilos CSS personalizados para el diseño minimalista y bordes redondeados
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
        line-height: 1.2;
    }

    .quote-container {
        text-align: right;
        font-style: italic;
        color: #6B7280;
        margin-bottom: 40px;
        padding-right: 10px;
        border-right: 3px solid #3B82F6;
    }

    .article-box {
        background-color: #F9FAFB;
        border: 1px solid #E5E7EB;
        border-radius: 20px;
        padding: 40px;
        color: #374151;
        line-height: 1.6;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }

    .section-header {
        color: #1E40AF;
        font-weight: 700;
        margin-top: 25px;
        margin-bottom: 10px;
        font-size: 20px;
    }

    .highlight-box {
        background-color: #EFF6FF;
        border-left: 4px solid #3B82F6;
        padding: 15px;
        margin: 20px 0;
        border-radius: 5px;
        font-weight: 500;
        text-align: center;
    }
    
    hr {
        margin: 30px 0;
        border: 0;
        border-top: 1px solid #D1D5DB;
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

# --- CUERPO DEL ARTÍCULO ---
with st.container():
    st.markdown("""
    <div class="article-box">
        <h2 style='text-align: center; color: #111827; margin-bottom: 30px;'>
            ¿Un algoritmo en el diván? Cómo la Inteligencia Artificial se ha convertido en el nuevo aliado de la psicología
        </h2>
        
        <p>En un mundo donde el estrés y la ansiedad parecen ser la norma, la demanda de ayuda profesional ha crecido más rápido que la capacidad de los sistemas de salud para responder. Ante esta "crisis de atención", ha surgido un invitado inesperado en la consulta: la Inteligencia Artificial (IA).</p>
        
        <p>Pero, ¿realmente puede un código de programación entender el sufrimiento humano? La ciencia sugiere que no se trata de reemplazar al psicólogo, sino de darle "superpoderes" para que pueda enfocarse en lo que mejor sabe hacer: conectar con el paciente.</p>

        <div class="section-header">1. Más que simples máquinas: Un apoyo en la crisis</div>
        <p>La IA en salud mental se define como la capacidad de los sistemas tecnológicos para aprender, razonar y resolver problemas complejos. Actualmente, no se utiliza para sustituir el criterio del profesional, sino para procesar cantidades masivas de información —como historias clínicas digitales, patrones en redes sociales o incluso escalas de humor— que a un humano le tomaría años analizar.</p>

        <div class="section-header">2. El "ojo clínico" potenciado por datos</div>
        <p>Uno de los mayores retos de la psicología es la precisión en el diagnóstico, especialmente cuando los síntomas de diferentes trastornos se solapan. Aquí es donde entra el <b>Machine Learning</b>, una rama de la IA que identifica patrones invisibles al ojo humano.</p>
        <ul>
            <li><b>Precisión sorprendente:</b> Estudios recientes indican que estos modelos alcanzan una precisión diagnóstica del 85%, superando en exactitud a muchos enfoques tradicionales.</li>
            <li><b>Herramientas en acción:</b> Plataformas como Limbic Access o Censeo ya están ayudando a clasificar a los pacientes desde su primer contacto.</li>
        </ul>

        <div class="section-header">3. Terapia en el bolsillo: El auge de los acompañantes virtuales</div>
        <p>¿Puede un "chatbot" ser empático? Herramientas como Woebot, Wysa o Youper ya aplican técnicas de Terapia Cognitivo-Conductual directamente en el teléfono. Un caso avanzado es <b>CaiTI</b>, un terapeuta basado en modelos de lenguaje extenso que monitorea hasta 37 dimensiones del funcionamiento diario.</p>

        <div class="section-header">4. Menos papeleo, más presencia humana</div>
        <p>Plataformas como Eholo, Texta AI o Mentalyc automatizan la transcripción de sesiones y la generación de notas clínicas. Al delegar estas tareas repetitivas, el terapeuta puede centrar toda su atención en la persona que tiene enfrente.</p>

        <div class="highlight-box">
            "La IA no busca reemplazar al facultativo, sino complementar su práctica clínica para ofrecer diagnósticos más objetivos".
        </div>

        <div class="section-header">5. El dilema del "Elemento Humano"</div>
        <p>A pesar de estos avances, surge una pregunta inevitable: ¿Se perderá la calidez de la terapia? La evidencia sugiere que, si se usa de forma ética, la IA se percibe como una herramienta de precisión que no sustituye el afecto ni la empatía, sino que libera al profesional para ejercerlos con mayor libertad.</p>

        <div class="section-header">6. Los retos del futuro: Privacidad y Ética</div>
        <p>No todo es color de rosa. El uso de IA en psicología enfrenta desafíos críticos como la <b>privacidad</b> de datos sensibles y los <b>sesgos algorítmicos</b>, asegurando que los modelos funcionen igual para todas las personas sin importar su origen.</p>
    </div>
    """, unsafe_allow_html=True)

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
