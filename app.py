import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="The IA Among Us",
    page_icon="🧠",
    layout="centered"
)

# 1. Estilos CSS (Diseño minimalista)
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

# --- CUERPO DEL ARTÍCULO ---
with st.container(border=True):
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
    * **Herramientas en acción:** Plataformas como Limbic Access o Censeo ya están ayudando a clasificar a los pacientes desde su primer contacto, reduciendo los tiempos de espera y asegurando que cada persona llegue al especialista adecuado.
    """)

    st.markdown("### 3. Terapia en el bolsillo: El auge de los acompañantes virtuales")
    st.write("""
    ¿Puede un "chatbot" ser empático? Aunque parezca ciencia ficción, herramientas como **Woebot, Wysa o Youper** ya aplican técnicas de Terapia Cognitivo-Conductual directamente en el teléfono del usuario. 
    
    Un caso avanzado es **CaiTI**, un terapeuta basado en modelos de lenguaje extenso que monitorea hasta 37 dimensiones del funcionamiento diario de una persona. Estos sistemas no solo escuchan; validan las emociones del usuario en tiempo real y personalizan el tratamiento según cómo se sienta la persona en ese preciso instante.
    """)

    st.markdown("### 4. Menos papeleo, más presencia humana")
    st.write("""
    Plataformas como **Eholo, Texta AI o Mentalyc** están cambiando las reglas del juego al automatizar la transcripción de sesiones y la generación de notas clínicas. Al delegar estas tareas repetitivas a la IA, el terapeuta puede centrar toda su atención y energía en la persona que tiene enfrente.
    """)

    st.markdown('<div class="highlight-text">"La IA no busca reemplazar al facultativo, sino complementar su práctica clínica para ofrecer diagnósticos más objetivos".</div>', unsafe_allow_html=True)

    st.markdown("### 5. El dilema del \"Elemento Humano\"")
    st.write("""
    A pesar de estos avances, surge una pregunta inevitable: ¿Se perderá la calidez de la terapia? Existe la preocupación de que la tecnología erosione la **"alianza terapéutica"**, ese vínculo de confianza entre paciente y profesional que es vital para la cura.
    
    Sin embargo, la percepción está cambiando. La evidencia científica sugiere que, si se usa de forma ética, la IA se percibe como una herramienta de precisión que no sustituye el afecto ni la empatía, sino que libera al profesional para que pueda ejercerlos con mayor libertad.
    """)

    st.markdown("### 6. Los retos del futuro: Privacidad y Ética")
    st.write("""
    No todo es color de rosa. El uso de IA en psicología enfrenta desafíos críticos:
    * **Privacidad:** La confidencialidad de los datos sensibles es la piedra angular de la confianza.
    * **Sesgos algorítmicos:** Es vital asegurar que los algoritmos no hereden prejuicios y funcionen igual de bien para todas las personas, sin importar su origen o cultura.
    """)

# --- SECCIÓN DE REFERENCIAS ---
st.write("---")
st.subheader("📚 Referencias Bibliográficas")

referencias = {
    "Graham, S. et al. (2019)": """
        **Resumen:** La tecnología de la inteligencia artificial (IA) representa tanto una gran promesa para transformar la atención a la salud mental como posibles riesgos. Este artículo ofrece una visión general de la IA y sus aplicaciones actuales en la salud, una revisión de investigaciones originales recientes sobre la IA específica para la salud mental y una discusión sobre cómo la IA puede complementar la práctica clínica, considerando sus limitaciones actuales, las áreas que requieren investigación adicional y las implicaciones éticas de esta tecnología.

        A medida que las técnicas de IA continúen perfeccionándose y mejorando, será posible ayudar a los profesionales de la salud mental a redefinir las enfermedades mentales de manera más objetiva de lo que se hace actualmente en el DSM-5, e identificar estas patologías en una etapa temprana o prodrómica, cuando las intervenciones pueden ser más efectivas.
    """,
    "Rollwage, M. et al. (2023)": """
        **Resumen:** En este estudio, examinamos si las soluciones digitales basadas en inteligencia artificial (IA) pueden ayudar a los profesionales de la salud mental a utilizar su tiempo de manera más eficiente y, de este modo, reducir la presión sobre los servicios y mejorar los resultados de los pacientes.
        Nuestros resultados enfatizan la utilidad del empleo de soluciones de IA para brindar soporte al personal de salud mental, destacando además el potencial de estas herramientas para incrementar la eficiencia en la prestación de cuidados y mejorar los resultados clínicos de los pacientes.
    """,
    "Rauf, M. et al. (2025)": """
        **Resumen:** Los psicólogos clínicos han reportado que la IA parece poseer una capacidad prometedora para mejorar los procesos diagnósticos y los enfoques terapéuticos individualizados. El propósito de esta investigación es explorar la perspectiva de los profesionales de la salud mental sobre cómo la IA puede incrementar la precisión diagnóstica y las formas en que diversos pacientes podrían beneficiarse de sus aplicaciones.
        El objetivo de la investigación se centrará en desvelar lo siguiente: el nivel de conocimiento actual de los profesionales de la salud mental sobre la IA, el grado en que estos profesionales consideran que la IA es útil y los factores clave que podrían influir en su adopción por parte de este colectivo.
    """,
    "de la Fuente Tambo & Armayones Ruiz (2025)": """
        **Resumen:** Este artículo revisa el uso de la Inteligencia Artificial (IA) en el ámbito de la Psicología asistencial, evaluando herramientas que apoyan a profesionales de la psicología en su trabajo diario. Se realizó un análisis de productos basados en IA disponibles actualmente (fecha: mayo 2024), de los cuales se seleccionaron 12 para una evaluación más detallada. Los resultados muestran que, aunque no todas las herramientas cumplen con criterios de seguridad y evidencia científica, existen opciones bien establecidas, especialmente en Estados Unidos y Reino Unido, donde su implantación es más avanzada. Este estudio sugiere que la adopción de la IA en el ámbito terapéutico va en aumento y que puede ofrecer a las y los profesionales un complemento útil, ayudándoles a realizar tareas administrativas o repetitivas y permitiéndoles centrarse en aspectos más complejos de la terapia.
    """,
    "Beg, M. J. et al. (2025)": """
        **Resumen:** La psicoterapia es fundamental para abordar los problemas de salud mental, pero con frecuencia se ve limitada por la falta de accesibilidad y calidad. La inteligencia artificial (IA) ofrece soluciones innovadoras, tales como sistemas automatizados para aumentar la disponibilidad y tratamientos personalizados para optimizar la psicoterapia. No obstante, persisten las preocupaciones éticas sobre la integración de la IA en la atención a la salud mental. Esta revisión narrativa explora la literatura sobre las aplicaciones de la IA en psicoterapia, centrándose en sus mecanismos, eficacia e implicaciones éticas, particularmente en los trastornos depresivos y de ansiedad.
    """,
    "Gual-Montolio, P. et al. (2022)": """
        **Resumen:** Los trastornos emocionales son los trastornos mentales más comunes a nivel mundial. Se ha comprobado que los tratamientos psicológicos son útiles en un número significativo de casos; sin embargo, hasta el 40% de los pacientes no responde a la psicoterapia según lo esperado. Los métodos de inteligencia artificial (IA) podrían optimizar la psicoterapia al proporcionar a terapeutas y pacientes recomendaciones en tiempo real, o casi en tiempo real, basadas en la respuesta del paciente al tratamiento.
        El objetivo de esta investigación es revisar sistemáticamente la evidencia sobre el uso de métodos basados en IA para mejorar los resultados en las intervenciones psicológicas en tiempo real o casi en tiempo real.
    """,
    "Rony, M. K. K. et al. (2025)": """
        **Resumen:** La Inteligencia Artificial (IA) ha demostrado un potencial significativo para transformar la atención psiquiátrica mediante la mejora de la precisión diagnóstica y las intervenciones terapéuticas. La psiquiatría enfrenta desafíos como el solapamiento de síntomas, métodos diagnósticos subjetivos y la necesidad de tratamientos personalizados. La IA, con sus capacidades avanzadas de procesamiento de datos, ofrece soluciones innovadoras a estas complejidades.
        Este estudio consistió en una revisión sistemática y meta-análisis de la literatura existente para evaluar la precisión diagnóstica y la eficacia terapéutica de la IA en la atención psiquiátrica, centrándose en diversos trastornos y tecnologías de IA.
    """,
    "Rebelo, A. D. et al. (2023)": """
        **Resumen:** Los psicólogos clínicos han reportado que la IA parece poseer una capacidad prometedora para mejorar los procesos diagnósticos y los enfoques terapéuticos individualizados. El propósito de esta investigación es explorar la perspectiva de los profesionales de la salud mental sobre cómo la IA puede incrementar la precisión diagnóstica y las formas en que diversos pacientes podrían beneficiarse de sus aplicaciones.
        El objetivo de la investigación se centrará en desvelar lo siguiente: el nivel de conocimiento actual de los profesionales de la salud mental sobre la IA, el grado en que estos profesionales consideran que la IA es útil y los factores clave que podrían influir en su adopción por parte de este colectivo.
    """,
    "Cruz-Gonzalez, P. et al. (2025)": """
        **Resumen:** Recientemente, la inteligencia artificial (IA) se ha aplicado a diversos trastornos de salud mental y ámbitos sanitarios. Esta revisión sistemática presenta la aplicación de la IA en la salud mental en los dominios de diagnóstico, monitoreo e intervención.
        Las herramientas de IA demostraron ser precisas en la detección, clasificación y predicción del riesgo de afecciones de salud mental, así como en la predicción de la respuesta al tratamiento y el monitoreo del pronóstico continuo de los trastornos mentales.
    """,
    "Pacheco, C. R. & Scheeringa, M. S. (2022)": """
        **Resumen:** Los clínicos de salud mental realizan tareas complejas con los pacientes que, potencialmente, podrían mejorar gracias a la enorme capacidad de procesamiento disponible a través de las aplicaciones móviles. Este estudio tuvo como objetivo analizar las aplicaciones (apps) para móviles y ordenadores disponibles comercialmente y centradas en el tratamiento de trastornos psiquiátricos.
        Los resultados muestran que estos cuatro elementos clínicos pueden potenciarse significativamente; sin embargo, el pleno potencial del procesamiento informático parece aún no alcanzado en las aplicaciones relacionadas con la salud mental.
    """
}

# Selector de referencias
seleccion = st.selectbox("Selecciona un artículo para leer el resumen científico:", list(referencias.keys()))

if seleccion:
    st.info(referencias[seleccion])

# Footer
st.markdown("<br><p style='text-align: center; color: #9CA3AF;'>Dashboard de Divulgación Científica - 2026</p>", unsafe_allow_html=True)
