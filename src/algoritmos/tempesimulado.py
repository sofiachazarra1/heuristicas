from numpy import exp
from src.algoritmos.greedy import greedy_mochila
from src.algoritmos.busqueda_local import busqueda_local
import time
import random
def N(t):
    """Criterio de parada basado en el número de iteraciones que ha realizado el algoritmo."""
    iteraciones = random.choice(range(t))
    return iteraciones

def C(data):
    """Función de coste asociada al problema de la mochila."""

    return sum(data)

def temple_simulado(sort_data,peso_tot,data):
    start = time.time()
    solucion = greedy_mochila(sort_data, peso_tot, data, False)
    print(solucion)
    solucion_start = solucion
    t = 200
    u = 0
    while t > 0:
        n = 0
        while n <= N(t):
            solucion_bus, peso_busqueda_local = busqueda_local(data, peso_tot, False)
            delta = C(solucion_bus) - C(solucion_start)
            if delta < 0:
                solucion_start = solucion_bus
                if C(solucion) < C(solucion_start):
                    solucion_start = solucion
            else:
                if u < exp(-delta/t):
                    solucion = solucion_bus
            n = n + 1
        t = t - 1
    end = time.time()
    print("Usando un algoritmo de tempe simulado con el critero de parada establecido."
          " \n" + " Solución: " + str(solucion) + "\n Número de elementos: "
          + str(n) + " Tiempo de cómputo = " + str(1000 * (end - start)) + " ms")
    return solucion

