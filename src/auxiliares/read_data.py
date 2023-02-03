import pandas as pd


#Funcion que te lee los ficheros que le indicas

def read_data(path_data, file):
    path_file = path_data + file
    data = pd.read_csv(path_file, delimiter=" ", names=["imp", "weight"])
    print(f"Se ha leido el fichero:{path_file}")
    num_obj=data.iloc[0][0]
    peso_tot=int(data.iloc[1][0])
    print(f"El peso maximo será: {peso_tot}")
    return peso_tot, int(num_obj), data.loc[2:]

def prop_data(data):
    data["prop"] = data["weight"]/data["imp"]
    data_sort = data.sort_values("prop")
    return data, data_sort

def calcular_peso(peso,x,n):
    peso_total = 0
    for i in range(n):
        if x[i] == 1:
            peso_total += peso[i+2]
    return peso_total

def calcular_valor(valor,x,n):
    valor_total = 0
    for i in range(n):
        if x[i] == 1:
            valor_total += valor[i+2]
    return valor_total



