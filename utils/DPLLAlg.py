def seleccionar_literal(formula):
    """
    Selecciona una literal de la fórmula.
    En este caso seleccionamos la primera literal de la primera cláusula no vacía.
    """
    for clausula in formula:
        if clausula:
            return next(iter(clausula))
    return None

def simplificar_formula(formula, literal):
    """
    Simplifica la fórmula eliminando las cláusulas que contienen la literal,
    y eliminando la literal complementaria de las demás cláusulas.
    """
    nueva_formula = []
    for clausula in formula:
        if literal in clausula:
            continue  # Omitir cláusulas que se satisfacen
        nueva_clausula = clausula - {f"¬{literal}" if not literal.startswith("¬") else literal[1:]}
        nueva_formula.append(nueva_clausula)
    return nueva_formula

def dpll(formula, asignacion):
    """
    Implementa el algoritmo DPLL con detalles en los pasos.
    """
    print(f"Fórmula actual: {formula}")
    print(f"Asignación actual: {asignacion}")
    
    # Caso base: si la fórmula está vacía, es satisfacible
    if not formula:
        print(f"Fórmula vacía, satisfacible con asignación: {asignacion} ✅\n")
        return True, asignacion

    # Caso base: si alguna cláusula está vacía, es insatisfacible
    if any(not clausula for clausula in formula):
        print("Se encontró una cláusula vacía, fórmula insatisfacible. ❌")
        return False, {}

    # Selecciona una literal
    literal = seleccionar_literal(formula)
    print(f"Literal seleccionada: {literal}")

    # Asignar la literal como verdadera y simplificar la fórmula
    nueva_asignacion = asignacion.copy()
    nueva_asignacion[literal] = True
    nueva_formula = simplificar_formula(formula, literal)
    print(f"Probando asignación: {nueva_asignacion} con fórmula simplificada: {nueva_formula} 🔄\n")

    # Recursivamente aplicar DPLL
    resultado, resultado_asignacion = dpll(nueva_formula, nueva_asignacion)
    if resultado:
        return True, resultado_asignacion

    # Si no se satisfizo, asignar la literal complementaria como verdadera y simplificar
    literal_complementaria = f"¬{literal}" if not literal.startswith("¬") else literal[1:]
    nueva_asignacion = asignacion.copy()
    nueva_asignacion[literal_complementaria] = True
    nueva_formula = simplificar_formula(formula, literal_complementaria)
    print(f"Probando asignación complementaria: {nueva_asignacion} con fórmula simplificada: {nueva_formula} 🔄\n")

    return dpll(nueva_formula, nueva_asignacion)