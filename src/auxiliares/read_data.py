import pandas as pd
import csv
import random
path_data = "C:/Users/sofia.chazarra/OneDrive - Accenture/Documents/MasterUCM/OptimizacionII/DatosMochila/kplib-master/"
file="00Uncorrelated/n00050/R01000/s001.kp"
path_file=path_data+file

#Funcion que te lee los ficheros que le indicas
def read_data(path_file):
    data = pd.read_csv(path_file,delimiter=" ", names=["imp","weight"])
    print(f"Se ha leido el fichero:{path_file}")
    num_obj=data.iloc[0][0]
    peso_tot=int(data.iloc[1][0])
    print(f"El peso maximo será: {peso_tot}")
    return peso_tot,num_obj,data

def prop_data(peso_tot,num_obj,data):
    data["prop"]=data["weight"]/data["imp"]
    data=data.iloc[2:int(num_obj)][:]
    data_sort=data.sort_values("prop")
    return peso_tot, num_obj, data, data_sort


