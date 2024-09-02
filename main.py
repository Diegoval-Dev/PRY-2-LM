from utils.BruteForceAlg import fuerza_bruta_sat
from utils.DPLLAlg import dpll

if __name__ == "__main__":
    f_case1 = [ {"¬A"}, {"B", "C"} ]
    f_case2 = [ {"A"}, {"¬A", "B"}, {"¬B"} ]

    use_dpll = False  # Si el valor es False se usará el alogoritmo de fuerza bruta

    print("Algoritmo de Fuerza Bruta \n" if not use_dpll else "Algoritmo DPLL \n")

    if use_dpll:
        resultado, asignacion = dpll(f_case1, {})
    else:
        resultado, asignacion = fuerza_bruta_sat(f_case1)

    if resultado:
        print(f"La fórmula es satisfacible con la asignación: \n{asignacion}\n")
    else:
        print("\nLa fórmula es insatisfacible")