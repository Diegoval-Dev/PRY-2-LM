
# SAT | DPLL y Fuerza Bruta 

Este proyecto contiene la implementación en Python de dos algoritmos fundamentales para resolver problemas de satisfacibilidad booleana (SAT): el algoritmo de Fuerza Bruta y el algoritmo DPLL (Davis-Putnam-Logemann-Loveland). Ambos algoritmos están diseñados para determinar si una fórmula booleana en forma normal conjuntiva (CNF) es satisfacible, y si es así, proporcionan una asignación de valores de verdad que satisface la fórmula.


## Librerías

- itertools


## Uso/Ejemplos

```python
# Esta variable define qué algoritmo utilizar
use_dpll = True || False

# Casos de prueba para verificar los algoritmos
f_case = [  
        [{"P"}, {"¬P"}],
        [{"Q", "P", "¬P"}],
        [{"¬P", "¬R", "¬S"}, {"¬Q", "¬P", "¬S"}],
        [{"¬P", "¬Q"}, {"Q", "S"}, {"¬P", "S"}, {"¬Q", "S"}],
        [{"¬P", "¬Q", "¬R"}, {"Q", "¬R", "P"}, {"¬P", "Q", "R"}],
        [{"R"}, {"¬Q", "¬R"}, {"¬P", "Q", "¬R"}, {"Q"}]
    ]
```

## Capturas de ejecución


### Algoritmo de Fuerza Bruta

<img width="1070" alt="image" src="https://github.com/user-attachments/assets/c6086066-3a9a-4e87-ab4b-baa6919a30bd">

### Alogritmo DPLL 

<img width="898" alt="image" src="https://github.com/user-attachments/assets/ed6e882f-1665-49e9-a5ed-80d4d1f7514c">

