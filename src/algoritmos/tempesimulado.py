def N(T):
    """Criterio de parada basado en el número de iteraciones que ha realizado el algoritmo."""
    return T

def C(data):
    """Función de coste asociada al problema de la mochila."""
    peso=data["weight"].tolist()
    return sum(peso)

def temple_simulado(sort_data,peso_tot,data):
    x,elem = greedy_mochila(sort_data,peso_tot,data)
    x_star = x
    T = 12345
    while(T > 0):
        n = 0
        while(n <= N(T)):
            y,peso_m = busqueda_local(x,peso_tot)
            delta = C(y) - C(x)
            if delta < 0:
                x = y
                if C(x) < C(x_star):
                    x_star = x
            else:
                if u < exp(-delta/T):
                    x = y
            n = n + 1
        T = T - 1
    return x