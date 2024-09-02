import itertools

def es_satisfacible(formula):
    print("Evaluando la fórmula:", formula)
    variables = list(set(var for clause in formula for var in clause))
    print("Variables encontradas:", variables)
    
    for asignacion in itertools.product([True, False], repeat=len(variables)):
        interpretacion = dict(zip(variables, asignacion))
        print("Probando asignación:", interpretacion)
        
        if evalua_formula(formula, interpretacion):
            print("La fórmula es satisfacible con la asignación:", interpretacion)
            return True, interpretacion
    
    print("La fórmula no es satisfacible.")
    return False, None

def evalua_formula(formula, interpretacion):
    return all(any(interpretacion.get(literal, not literal.startswith('¬')) for literal in clause) for clause in formula)

def main():
    formula = [
        {'p', '¬q'},
        {'q', 'r'},
        {'¬p', 'r'}
    ]
    
    resultado, asignacion = es_satisfacible(formula)
    
    if resultado:
        print("La fórmula es satisfacible.")
    else:
        print("La fórmula no es satisfacible.")

if __name__ == "__main__":
    main()
