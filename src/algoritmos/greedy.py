import time
import src.auxiliares.read_data as aux
from src.algoritmos.busqueda_local import busqueda_local
def greedy_mochila(sort_data,data,peso_tot):
    start=time.time()
    agg_weight=0
    i=1
    while (agg_weight+sort_data.iloc[i][1])<= peso_tot:
        agg_weight=agg_weight+sort_data.iloc[i][1]
        i=i+1
    sel_data=sort_data.iloc[0:i+1][:].sort_index()
    sel_data["selected"]=1
    sel_data=sel_data.merge(data, how="right")
    vect_ind=sel_data["selected"].fillna(0).tolist()
    end=time.time()
    print("Usando un algoritmo Greedy para el problema de la mochila"
          " \n" + " Solución: " + str(vect_ind) + "\n Número de elementos: "
          + str(sum(vect_ind)) + "\n Peso: " + str(agg_weight) + "\n"
        " Tiempo de cómputo = " + str(1000 * (end - start)) + " ms")
    return vect_ind


###Para ejecutarlo directamente
"""
path_data = "C:/Users/sofia.chazarra/OneDrive - Accenture/Documents/MasterUCM/OptimizacionII/DatosMochila/kplib-master/"
file="00Uncorrelated/n00050/R01000/s001.kp"
path_file=path_data+file

peso_tot,num_obj,data=aux.read_data(path_file)
data,sort_data=aux.prop_data(num_obj,data)
greedy_mochila(sort_data,data,peso_tot)
"""