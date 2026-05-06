import numpy as np
def parcial_x(X: list, f: callable, h: float) -> float:
    """Esta función calcula la derivada parcial respecto a x usando diferencia centrada"""
    return (f([X[0] + h, X[1]]) - f([X[0] - h, X[1]])) / (2 * h)

def parcial_y(X: list, f: callable, h: float) -> float:
    """Esta función calcula la derivada parcial respecto a y usando diferencia centrada"""
    return (f([X[0], X[1] + h]) - f([X[0], X[1] - h])) / (2 * h)

def gradf(X: list, f: callable, h: float = 0.000001) -> list:
    """Esta función retorna el vector gradiente en el punto X"""
    df_dx = parcial_x(X, f, h)
    df_dy = parcial_y(X, f, h)
    return [df_dx, df_dy]

def f1(X: list) -> float:
    x, y = X[0], X[1]
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2

def f2(X: list) -> float:
    x = X[0]
    y = X[1]
    return -(y + 47) * np.sin(np.sqrt(abs(y + x/2 + 47))) - x * np.sin(np.sqrt(abs(x - (y + 47))))
