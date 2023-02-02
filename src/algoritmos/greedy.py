def greedy_mochila(sort_data,data,peso_tot=None):
    agg_weight=0
    i=1
    while (agg_weight+sort_data.iloc[i][1])<=peso_tot:
        agg_weight=agg_weight+sort_data.iloc[i][1]
        i=i+1
    sel_data=sort_data.iloc[0:i+1][:].sort_index()
    sel_data["selected"]=1
    sel_data=sel_data.merge(data, how="right")
    print(f"El valor inicial de la mochila es {agg_weight}")
    print(f"Se han añadido {i} elementos")
    vect_ind=sel_data["selected"].fillna(0)
    return vect_ind
