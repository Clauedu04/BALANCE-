from sympy import symbols, Eq, solve

def balance_combustion(formula):
    # Extraer cantidad de C, H y asumir O en el compuesto
    import re
    match = re.match(r'C(\d*)H(\d*)', formula)
    if not match:
        raise ValueError("Fórmula inválida. Debe ser CxHy")
    
    C = int(match.group(1)) if match.group(1) else 1
    H = int(match.group(2)) if match.group(2) else 1
    O = 2  # Oxígeno molecular (O2)
    
    # Definir incógnitas
    a, b, c, d = symbols('a b c d')
    
    # Reacción: CxHy + O2 -> CO2 + H2O
    eq1 = Eq(a, 1)  # Reactivo hidrocarburo
    eq2 = Eq(b * 2, C * c)  # Balance de Carbono
    eq3 = Eq(d * 2, H * a)  # Balance de Hidrógeno
    eq4 = Eq(b * 2, c + d / 2)  # Balance de Oxígeno
    
    # Resolver sistema
    solution = solve((eq1, eq2, eq3, eq4), (a, b, c, d))
    
    # Convertir a coeficientes enteros mínimos
    factor = max(solution.values())
    balanced = {k: int(v * factor) for k, v in solution.items()}
    
    return f"{balanced[a]} {formula} + {balanced[b]} O2 -> {balanced[c]} CO2 + {balanced[d]} H2O"

# Ejemplo de uso:
hydrocarbons = ['CH4', 'C2H4', 'C2H2']  # Metano (alcano), eteno (alqueno), etino (alquino)
for hc in hydrocarbons:
    print(balance_combustion(hc))
