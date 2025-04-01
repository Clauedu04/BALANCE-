def balance_combustion(hydrocarbon: str):
    import re
    
    # Expresión regular para extraer átomos de C y H
    match = re.match(r'C(\d*)H(\d*)', hydrocarbon)
    if not match:
        return "Formato inválido. Usa CxHy, donde x e y son números enteros."
    
    # Obtener números de átomos de C y H
    C = int(match.group(1)) if match.group(1) else 1  # Si no hay número, es 1
    H = int(match.group(2)) if match.group(2) else 1
    
    # Oxígeno en la ecuación
    O2 = (C * 2 + H // 2)  # Cantidad de O2 necesaria para balancear
    CO2 = C  # Cada C forma una molécula de CO2
    H2O = H // 2  # Cada dos H forman una molécula de H2O
    
    # Si H es impar, ajustar balance con coeficientes fraccionarios
    if H % 2 != 0:
        O2 = O2 / 2
        CO2 = CO2 / 2
        H2O = H2O / 2
    
    return f"{hydrocarbon} + {O2} O2 -> {CO2} CO2 + {H2O} H2O"

# Ejemplo de uso:
alcanos = ["CH4", "C2H6", "C3H8"]
alquenos = ["C2H4", "C3H6", "C4H8"]
alquinos = ["C2H2", "C3H4", "C4H6"]

for hc in alcanos + alquenos + alquinos:
    print(balance_combustion(hc))
