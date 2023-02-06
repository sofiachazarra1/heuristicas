import time
import src.auxiliares.read_data as aux
from src.algoritmos.greedy import greedy_mochila
import random

def busquedalocal(sort_data, pesomax, data, M, showprint=True, entorno=0):
    start = time.time()
    if entorno==0:
        entorno = int(random.choice([0, 1, 2]))
    sacar = 0
    meter = 0
    solucion, peso_solucion = greedy_mochila(sort_data, pesomax, data, False)

    valor_solucion = aux.calcular_valor(data["imp"], solucion, M)
    if entorno == 0:
        while sacar + meter < 3:
            parada = int(random.choice(range(0, M)))
            if solucion[parada]==1:
                solucion[parada]=0.0
                peso_solucion = peso_solucion-data["weight"].tolist()[parada]
                valor_solucion = valor_solucion-data["imp"].tolist()[parada]
                sacar = sacar + 1
            # Metemos  un elemento de la mochila
            if sacar == 2:
                parada = int(random.choice(range(0, M)))
                if int(peso_solucion + data["weight"].tolist()[parada]) < int(pesomax):
                    if solucion[parada] == 0:
                        solucion[parada] = 1.0
                        peso_solucion = peso_solucion + data["weight"].tolist()[parada]
                        valor_solucion = valor_solucion + data["imp"].tolist()[parada]
                        meter = meter + 1
    #sacar un elemento y meter uno
    if entorno == 1:
        while sacar + meter < 2:
            parada = int(random.choice(range(0, M)))
            if solucion[parada] == 1:  # sacar un elemento
                solucion[parada] = 0.0
                peso_solucion = peso_solucion - data["weight"].tolist()[parada]
                valor_solucion = valor_solucion - data["imp"].tolist()[parada]
                sacar = sacar + 1
            if sacar == 1:
                parada = int(random.choice(range(0, M)))
                if peso_solucion + data["weight"].tolist()[parada] < pesomax:
                    if solucion[parada] == 0:
                        solucion[parada] = 1.0
                        peso_solucion = peso_solucion + data["weight"].tolist()[parada]
                        valor_solucion = valor_solucion + data["imp"].tolist()[parada]
                        meter = meter + 1

    #meter uno
    if entorno == 2:
        for k in range(M):
            parada = int(random.choice(range(0, M)))
            if peso_solucion + data["weight"].tolist()[parada] < pesomax:
                if solucion[parada] == 0:  # sacar un elemento
                    solucion[parada] = 1.0
                    peso_solucion = peso_solucion + data["weight"].tolist()[parada]
                    valor_solucion = valor_solucion + data["imp"].tolist()[parada]

    end = time.time()
    if showprint==True:
        print("Usando un algoritmo de busqueda local para el problema de la mochila"
             " \n" + " Solución: " + str(solucion) + "\n Número de elementos: "
             + str(sum(solucion)) + "\n Peso: " + str(peso_solucion) + "\n"
            " Tiempo de cómputo = " + str(1000 * (end - start)) + " ms")
    return solucion
