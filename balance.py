import streamlit as st

def balance_combustion(formula):
    """Balancea la ecuación de combustión para hidrocarburos"""
    import re
    match = re.match(r'C(\d*)H(\d*)', formula)
    if not match:
        return "Fórmula no válida"
    
    C = int(match.group(1)) if match.group(1) else 1
    H = int(match.group(2)) if match.group(2) else 1
    O2 = (C * 1 + H / 4)
    CO2 = C
    H2O = H / 2
    
    return f"{formula} + {O2} O₂ → {CO2} CO₂ + {H2O} H₂O"

st.title("Balanceador de Reacciones de Combustión")

formula = st.text_input("Ingrese la fórmula del hidrocarburo (Ej: C2H6)")
if formula:
    resultado = balance_combustion(formula)
    st.write("Ecuación balanceada:")
    st.latex(resultado)
