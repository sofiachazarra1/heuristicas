import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
list_mutar = [0.1]*5+ [0.4]*5
hijos = [5]*5 + [1, 5, 10, 20, 28]
cromosomas= [20]*2+ [30]+[200]*2+[20]*5
iteraciones = [60]+[100]+[60]+[100]+ [200]+[60]*5 + [0]
valores=[14453, 15072, 13098, 14620, 14888, 13816, 14804, 13769, 13631, 13030] #1º 0.1,5,20,60 2º 0.1,5,20,100 3º 0.1,5,30,60 4º 0.1,5,200,100
peso=[13238, 13519, 13588, 12821, 13350, 13003, 13349, 12986, 13219, 12919] #5º 0,1,5,200,200 6º0.4,1,20,60 7º0.4,5,20,60 8º 0.4,10,20,60

# se creara otra variable que se representara con colores
plt.figure()
df = pd.DataFrame({"x":peso,
                   "y":valores,
                   "colors":cromosomas})

size=81
sc = plt.scatter(df['x'], df['y'], s=size, c=df['colors'], edgecolors='none')

labels_mutar=["0.1","0.4"]
labels_hijos=["1","5", "10", "20", "28"]
labels_cromosomas=["60","100","200"]
labels_iteraciones=["20","30", "200"]
lp = lambda i: plt.plot([],color=sc.cmap(sc.norm(i)), ms=np.sqrt(size), mec="none",
                        label="Iteraciones {:g}".format(i), ls="", marker="o")[0]
print(lp)
#"Feature {:g}".format(i)
handles = [lp(i) for i in np.unique(df["colors"])]
print(handles)
plt.legend(handles=handles)
plt.ylabel("Valor del objeto")
plt.xlabel("Peso del objeto")
plt.show()


breakpoint()


#axes[1, 0].scatter(valores, peso, c=hijos, alpha=1)
#axes[0, 1].scatter(valores, peso, c=iteraciones, alpha=1)
#axes[1, 1].scatter(valores, peso, c=cromosomas, alpha=1)


plt.show()