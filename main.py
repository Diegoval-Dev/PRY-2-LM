import utils.BruteForceAlg as BTa

if __name__ == "__main__":
    print("Algoritmo de Fuerza Bruta \n")

    f_case1 = [ {"¬A"}, {"B", "C"} ]
    f_case2 = [ {"A"}, {"¬A", "B"}, {"¬B"} ]

    resultado, asignacion = BTa.fuerza_bruta_sat(f_case1)
    if resultado:
        print(f"La fórmula es satisfacible con la asignación: \n{asignacion}")
    else:
        print("La fórmula es insatisfacible")