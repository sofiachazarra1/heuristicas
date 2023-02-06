from numpy import exp
from src.algoritmos.greedy import greedy_mochila

import src.auxiliares.read_data as aux
from src.algoritmos.busquedalocal import busquedalocal
import time
import random
def N(t):
    """Criterio de parada basado en el número de iteraciones que ha realizado el algoritmo."""
    iteraciones = random.choice(range(t))
    print("Condicion de parada: "+str(iteraciones))
    return iteraciones

def C(data):
    """Función de coste asociada al problema de la mochila."""

    return sum(data)

def tempe_simulado(sort_data,peso_tot,data, num_obj):
    start = time.time()
    solucion, peso_mochila = greedy_mochila(sort_data, peso_tot, data, False)
    solucion_start = solucion
    t = 200
    u = 0
    while t > 0:
        n = 0
        while n <= N(t):
            solucion_bus = busquedalocal(sort_data, peso_tot, data, num_obj, False)
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
          + str(sum(solucion))  + "\n Peso: "
          + str(aux.calcular_peso(data["weight"], solucion, num_obj)) + "\n Tiempo de cómputo = " + str(1000 * (end - start)) + " ms")
    return solucion

