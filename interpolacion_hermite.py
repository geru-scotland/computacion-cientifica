from sympy import symbols, diff, Eq, solve
"""
Autor: Aingeru García
Descripción:
Este script ha sido desarrollado para la construcción y evaluación de un polinomio interpolador, 
utilizando la biblioteca SymPy, como complemento a la documentación del Bloque III de la asignatura
de Computación Científica. 
El objetivo  es encontrar un polinomio que se ajuste a un conjunto dado de puntos y valores 
derivados en esos puntos, y luego evaluar ese polinomio en un punto concreto.
"""

# Defino las variables simbólicas, que serán los coeficinetes del px interpolador.
x, a, b, c, d, e = symbols('x a b c d e')

# Defino el px interpolador mencionado anteriormente
px = a + b*(x-1) + c*(x-1)**2 + d*(x-1)**2*(x-2) + e*(x-1)**2*(x-2)*(x-3)

# y obtengo su derivada, de cara a las condiciones.
px_derivada = diff(px, x)

# Establezco las condiciones
condiciones = [
    Eq(px.subs(x, 1), 1),          # P(1) = 1
    Eq(px_derivada.subs(x, 1), 1), # P'(1) = 1
    Eq(px.subs(x, 2), 5),          # P(2) = 5
    Eq(px.subs(x, 3), 8),          # P(3) = 8
    Eq(px_derivada.subs(x, 3), 2)  # P'(3) = 2
]

# Resuelvo para obtener los coeficiente
coeficientes = solve(condiciones, (a, b, c, d, e))

# Evalúo P(1.5) usando el polinomio interpolador px y
# los coeficientes obtenidos
px_evaluado = px.subs(coeficientes).subs(x, 1.5)
resultado = px_evaluado.evalf()
print("P(1.5) =", resultado)

