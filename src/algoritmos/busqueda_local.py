import time
import src.auxiliares.read_data as aux

def busqueda_local(data, M):
    start=time.time()
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
        end = time.time()

    print("Usando un algoritmo Greedy para el problema de la mochila"
         " \n" + " Solución: " + str(solucion) + "\n Número de elementos: "
         + str(sum(solucion)) + "\n Peso: " + str(peso_actual) + "\n"
        " Tiempo de cómputo = " + str(1000 * (end - start)) + " ms")
    return solucion, peso_m

    ###Para ejecutarlo directamente

path_data = "C:/Users/sofia.chazarra/OneDrive - Accenture/Documents/MasterUCM/OptimizacionII/DatosMochila/kplib-master/"
file="00Uncorrelated/n00050/R01000/s001.kp"
path_file=path_data+file

peso_tot,num_obj,data=aux.read_data(path_file)
data,sort_data=aux.prop_data(num_obj,data)
busqueda_local(sort_data,peso_tot)