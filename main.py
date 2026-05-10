import numpy as np
from funciones import f1, f2, gradf

#EJERCICIO1
# Paso 1
print("Paso 1: verificación de f1 y f2")
punto_prueba = [1.0, 2.0]
print(f"f1({punto_prueba}) = {f1(punto_prueba)}")
print(f"f2({punto_prueba}) = {f2(punto_prueba):.6f}")

# Paso 2
print("\n Paso 2: gradiente numérico")

puntos_pruebaS = [
    [0.0, 0.0],
    [1.0, 1.0],
    [3.0, 2.0],   # mínimo conocido de f1
]

print("\nGradiente de f1:")
for p in puntos_pruebaS:
    g = gradf(p, f1)
    print(f"  ∇f1({p}) ≈ [{g[0]:.6f}, {g[1]:.6f}]")

print("\nGradiente de f2:")
for p in puntos_pruebaS:
    g = gradf(p, f2)
    print(f"  ∇f2({p}) ≈ [{g[0]:.6f}, {g[1]:.6f}]")

#verificamos mínimos con gradiente cercano a cero
minimos_f1 = [[3.0, 2.0], [-2.805118, 3.131312],
              [-3.779310, -3.283186], [3.584428, -1.848126]]

print("\nVerificación en mínimos conocidos de f1 (gradiente ≈ 0):")
for m in minimos_f1:
    g = gradf(m, f1)
    norma = np.linalg.norm(g)
    print(f"  ∇f1({[round(c,4) for c in m]}) ≈ {norma:.2e}  {'✓' if norma < 1e-3 else '✗'}")