def metodo_gradiente(n: int, x0: list, a: float, f: callable) -> list:
    
    x = np.array(x0, dtype=float)
    generados = [x.copy()]

    for _ in range(n):
        gradiente = np.array(gradf(x.tolist(), f))
        x = x - a * gradiente
        generados.append(x.copy())

    return generados
