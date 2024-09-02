
# SAT | DPLL y Fuerza Bruta 

Este proyecto contiene la implementación en Python de dos algoritmos fundamentales para resolver problemas de satisfacibilidad booleana (SAT): el algoritmo de Fuerza Bruta y el algoritmo DPLL (Davis-Putnam-Logemann-Loveland). Ambos algoritmos están diseñados para determinar si una fórmula booleana en forma normal conjuntiva (CNF) es satisfacible, y si es así, proporcionan una asignación de valores de verdad que satisface la fórmula.


## Librerías

- itertools


## Uso/Ejemplos

```python
# Esta variable define qué algoritmo utilizar
use_dpll = True || False

# Casos de ejemplo uno éxito (1) y otro de fracaso (2)
f_case1 = [ {"¬A"}, {"B", "C"} ]
f_case2 = [ {"A"}, {"¬A", "B"}, {"¬B"} ]
```

## Capturas de ejecución

