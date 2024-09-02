from itertools import product

def evaluar_clausula(clausula, asignacion):
    """
    Evalúa si una cláusula es verdadera bajo una asignación dada.
    """
    for literal in clausula:
        if literal in asignacion and asignacion[literal]:
            return True
    return False

def evaluar_formula(formula, asignacion):
    """
    Evalúa si toda la fórmula es verdadera bajo una asignación dada.
    """
    return all(evaluar_clausula(clausula, asignacion) for clausula in formula)

def fuerza_bruta_sat(formula):
    """
    Implementa el algoritmo de fuerza bruta para el problema SAT.
    """

    variables = set(literal.strip('¬') for clausula in formula for literal in clausula)
    
    print(f"Variables a asignar: {variables} \n")
    
    for valores in product([True, False], repeat=len(variables)):
        asignacion = {}
        for variable, valor in zip(variables, valores):
            asignacion[variable] = valor
            asignacion[f"¬{variable}"] = not valor
        
        print(f"Probando asignación: {asignacion} 🔄")
        
        if evaluar_formula(formula, asignacion):
            print(f"Asignación {asignacion} Satisface ✅\n")
            return True, asignacion
    
    print("No se encontró una asignación que satisfaga la fórmula ❗️")
    return False, {}