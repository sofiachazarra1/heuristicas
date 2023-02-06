import time
from src.algoritmos.greedy import greedy_mochila
from src.algoritmos.busquedalocal import busquedalocal
import src.auxiliares.read_data as aux
import random

n_max = 1000


def C(data):
    """Función de coste asociada al problema de la mochila."""
    suma_sol=0
    for s in data:
        suma_sol += int(s)
    return -(suma_sol)


def VND(sort_data, peso_tot, data, num_obj):
    """Búsqueda Descendente"""

    S, agg_weight = greedy_mochila(sort_data, peso_tot, data, False)
    j=0
    while (j <= 2):
        S_prima = busquedalocal(sort_data, peso_tot, data, num_obj, False, j)
        if C(S_prima) < C(S):
            S = S_prima
            j = 0
        else:
            j = j + 1
    return S


def GVNS(sort_data, peso_tot, data, num_obj):
    """Búsqueda en Entorno Variable General"""

    start=time.time()

    S = greedy_mochila(sort_data, peso_tot, data, False)
    n = 1

    entorno = int(random.choice([0, 1, 2]))
    S_prima = busquedalocal(sort_data, peso_tot, data, num_obj, False, entorno)

    S_segunda = VND(sort_data, peso_tot, data, num_obj)
    if type(S[0])==list:
        T=S[0]
    else:
        T=S
    while (n < n_max and C(S_segunda) < C(T)):
        j = 1
        while (j <= 2):
            S = S_segunda
            entorno = int(random.choice([0, 1, 2]))
            S_prima = busquedalocal(sort_data, peso_tot, data, num_obj, False, entorno)
            S_segunda = VND(sort_data, peso_tot, data, num_obj)
            j = j + 1
        n = n + 1
    end = time.time()
    print("Usando un algoritmo vns para el problema de la mochila"
          " \n" + " Solución: " + str(S) + "\n Número de elementos: "
          + str(sum(S)) + "\n Peso: " + str(aux.calcular_peso(data["weight"], S, num_obj)) + "\n"
        " Tiempo de cómputo = " + str(1000 * (end - start)) + " ms")

    return S