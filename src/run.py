import src.auxiliares.read_data as aux
from src.algoritmos.busqueda_local import busqueda_local
from src.algoritmos.tempesimulado import temple_simulado

path_data = "C:/Users/sofia.chazarra/OneDrive - Accenture/Documents/MasterUCM/OptimizacionII/DatosMochila/kplib-master/"
file="00Uncorrelated/n00050/R01000/s001.kp"

peso_tot, num_obj, data = aux.read_data(path_data, file)
data, sort_data = aux.prop_data(num_obj, data)

alg = temple_simulado(sort_data, peso_tot, data)