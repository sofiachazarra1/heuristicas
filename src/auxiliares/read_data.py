import pandas as pd


#Funcion que te lee los ficheros que le indicas

def read_data(path_data, file):
    path_file = path_data + file
    data = pd.read_csv(path_file,delimiter=" ", names=["imp","weight"])
    print(f"Se ha leido el fichero:{path_file}")
    num_obj=data.iloc[0][0]
    peso_tot=int(data.iloc[1][0])
    print(f"El peso maximo será: {peso_tot}")
    return peso_tot,num_obj,data

def prop_data(num_obj,data):
    data["prop"]=data["weight"]/data["imp"]
    data=data.iloc[2:int(num_obj)][:]
    data_sort=data.sort_values("prop")
    return data, data_sort


