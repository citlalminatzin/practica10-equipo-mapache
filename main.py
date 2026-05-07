def metodo_gradiente(n: int, x0: list, a: float, f: callable) -> list:
    
    x = np.array(x0, dtype=float)
    trayectoria = [x.copy()]

    for _ in range(n):
        gradiente = np.array(gradf(x.tolist(), f))
        x = x - alpha * gradiente
        trayectoria.append(x.copy())

    return trayectoria
