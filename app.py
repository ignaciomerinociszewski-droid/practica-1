import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Salud 3º ESO", page_icon="🏥")

# Título y Descripción
st.title(" 🤑🤑🤑🤑Calculadora de rebajas🤑🤑🤑🤑")
st.markdown("Q pasa, aqui puedes calcular tus aura rebajas.")
st.write("---") # Línea separadora5

# 2. Entrada de Datos (Barra Lateral)
st.sidebar.header("Tus Datos")
precio = st.sidebar.number_input("precio (€)", min_value=0, max_value=10000000000, value=60)
porcentaje = st.sidebar.slider("Porcentaje de rebajas (%)", 0.00, 100.00, 50.00)

# 3. Botón de Cálculo y Lógica
if st.button("Calcular ahora"):
    
    # Fórmula Matemática: Peso entre altura al cuadrado
    PF = precio -(precio * porcentaje/100)
    
    # 4. Mostrar Resultado con Diseño
    col1, col2 = st.columns(2)
    
    with col1:
        # Usamos metric para que el número se vea grande
        st.metric(label="Tu precio final es:", value=f"{PF:.2f}")
        
    with col2:
        # Usamos condicionales (if/elif/else) para el diagnóstico
        if porcentaje < 25:
            st.warning("👍 ahorro minimo")
            st.write("No esta mal bro.")
        elif porcentaje == 67:
            st.warning("👍 ahorro minimo")
            st.success("67auraskibidi")
        elif 25 <= porcentaje < 50:
            st.success("✅ ahorro mediano")
            st.balloons() # ¡Premio!
        elif 50 <= porcentaje < 75:
            st.warning(" gran ahorro😎")
            st.write("Que buena jugada.")
      
        else:
            st.error("AURA")
            st.write("Es importante cuidar tu salud.")
    
    
    # Extra: Mostrar la fórmula usada (LaTeX)
    st.write("---")
    st.info("Fórmula matemática utilizada:")
    st.latex(r''' precio final = Precio - precio * porcentaje ''')

