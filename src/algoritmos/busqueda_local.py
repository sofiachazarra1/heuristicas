def busqueda_local(data, M):
    peso = data["weight"].tolist()

    beneficio = data["imp"].tolist()

    def mejor_objeto_restante(data):
        mejor_obj = data.index[0]
        return mejor_obj - 2, data.drop(mejor_obj)

    n = len(peso)
    solucion = [0 for i in range(n)]  # creamos una solucion inicial con un vector de 0's
    peso_actual = 0
    while peso_actual < M:
        i, data = mejor_objeto_restante(data)
        if peso[i] + peso_actual <= M:
            solucion[i] = 1
            peso_m = peso_actual + peso[i]
            peso_actual = peso_actual + peso[i]
        else:
            solucion[i] = round((M - peso_actual) / peso[i])
            peso_actual = M
    return solucion, peso_m