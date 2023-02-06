import src.auxiliares.read_data as aux
from src.algoritmos.busquedalocal import busquedalocal
from src.algoritmos.tempesimulado import temple_simulado
from src.algoritmos.greedy import greedy_mochila
from src.algoritmos.genetico_alg import genetico

path_data = "C:/Users/sofia.chazarra/OneDrive - Accenture/Documents/MasterUCM/OptimizacionII/DatosMochila/kplib-master/"
file = "00Uncorrelated/n00050/R01000/s001.kp"

peso_tot, num_obj, data = aux.read_data(path_data, file)
data, sort_data = aux.prop_data(data)

def main():
    print("¿Que tipo de algoritmo quiere ejecutar de la siguiente lista: tempe_simulado, greedy, vns, genetico o busquedalocal? ")
    tipo_algoritmo = input()
    if tipo_algoritmo == "tempe_simulado":
        temple_simulado(sort_data, peso_tot, data)
    elif tipo_algoritmo == "greedy":
        greedy_mochila(sort_data, peso_tot, data)
    elif tipo_algoritmo == "vns":
        temple_simulado(sort_data, peso_tot, data)
    elif tipo_algoritmo == "busquedalocal":
        busquedalocal(sort_data, peso_tot, data, num_obj)
    elif tipo_algoritmo == "genetico":
        print("Para el algortimo genetico necesitamos la probabilidad de mutacion, numero de hijos, las iteraciones y la longitud de la poblacion. ")
        print("Escriba la pobrobailidad de mutar (num del 0 al 1)")
        prob_mutar = float(input())
        print("Escriba el numero de hijos")
        sol_rep = int(input())
        print("Escriba el num de iteraciones")
        iteraciones = int(input())
        print("Escriba el num de cromosomas")
        poblacion_size = int(input())
        genetico(data, peso_tot, num_obj, prob_mutar, sol_rep, iteraciones, poblacion_size)
    else:
        print("El algoritmo indicado no se corresponde con ninguno de los listados.")

if __name__ =="__main__":
    main()

