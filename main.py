import utils.BruteForceAlg as BTa

if __name__ == "__main__":
    print("Algoritmo de Fuerza Bruta \n")
    formula = [ {"A"}, {"B"} ]
    resultado, asignacion = BTa.fuerza_bruta_sat(formula)
    if resultado:
        print(f"La fórmula es satisfacible con la asignación: \n{asignacion}")
    else:
        print("La fórmula es insatisfacible")