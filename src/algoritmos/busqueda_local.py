import time
import src.auxiliares.read_data as aux

def busqueda_local(data, M):
    start=time.time()
    peso = data["weight"].tolist()
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

    print("Usando un algoritmo de busqueda local para el problema de la mochila"
         " \n" + " Solución: " + str(solucion) + "\n Número de elementos: "
         + str(sum(solucion)) + "\n Peso: " + str(peso_m) + "\n"
        " Tiempo de cómputo = " + str(1000 * (end - start)) + " ms")
    return solucion, peso_m
