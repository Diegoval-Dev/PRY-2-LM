from utils.BruteForceAlg import fuerza_bruta_sat
from utils.DPLLAlg import dpll

if __name__ == "__main__":
    # ¬

    f_case = [  
        [{"P"}, {"¬P"}],
        [{"Q", "P", "¬P"}],
        [{"¬P", "¬R", "¬S"}, {"¬Q", "¬P", "¬S"}],
        [{"¬P", "¬Q"}, {"Q", "S"}, {"¬P", "S"}, {"¬Q", "S"}],
        [{"¬P", "¬Q", "¬R"}, {"Q", "¬R", "P"}, {"¬P", "Q", "R"}],
        [{"R"}, {"¬Q", "¬R"}, {"¬P", "Q", "¬R"}, {"Q"}]
    ]

    for formula in f_case:
        print(f"Fórmula: {formula}")

        use_dpll = False  # Si el valor es False se usará el alogoritmo de fuerza bruta

        print("Algoritmo de Fuerza Bruta \n" if not use_dpll else "Algoritmo DPLL \n")

        if use_dpll:
            resultado, asignacion = dpll(formula, {})
        else:
            resultado, asignacion = fuerza_bruta_sat(formula)

        if resultado:
            print(f"La fórmula es satisfacible con la asignación: \n{asignacion}\n")
        else:
            print("\nLa fórmula es insatisfacible")