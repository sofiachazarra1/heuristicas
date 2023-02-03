import random
import time
import src.auxiliares.read_data as aux
import csv

class Problema_Genetico(object):
    """ Clase para representar un problema para que sea abordado mediante un
    algoritmo genetico general. Consta de los siguientes atributos:
    - genes: lista de posibles genes en un cromosoma [0,1] Un gen por variable de decisión binaria
    - decodifica: lista inicial de cromosomas
    - longitud_individuos: nº de cromosomas
    - iteraciones: nº de iteraciones que se hacen sobre los cromosomas"""

    def __init__(self, genes, decodifica, poblacion_size, iteraciones):
        self.genes = genes
        self.decodifica = decodifica
        self.longitud_individuos = poblacion_size
        self.iteraciones = iteraciones

    def mutacion(self, cromosoma, prob):
        """Los atributos son:
        - cromosoma: lista con valores 1 u 0.
        - prob: probablidad de mutacion en base a unas probabilidades random de cada gen """
        resultado = []
        if type(cromosoma) != list:
            cromosoma = [cromosoma]
        for g in cromosoma:
            if random.random() < prob:
                resultado.append(random.choice(self.genes))
            else:
                resultado.append(g)

        return resultado

    # añadir lo de quitar elementos duplicados en el curce

    def cruce(self, cromosoma1, cromosoma2,n):
        """Los atributos son:
        - cromosoma1: lista con valores 1 u 0 para el primer cromosoma.
        - cromosoma2: lista con valores 1 u 0 para el segundo cromosoma. """
        hijos = []
        for i in range(n):
            hijos.append(random.choice([cromosoma1[i], cromosoma2[i]]))
        return hijos


# Definimos nuestra funcion objetivo que utilizamos para elegir los genes
def fun_obj(poblacion, peso_max, n, data):
    sol_objetivo = []
    for sol in poblacion:

        peso = aux.calcular_peso(data["weight"], sol, n)
        if peso > peso_max:
            valor = peso_max - peso
        else:
            valor = aux.calcular_valor(data["imp"], sol, n)
        sol_objetivo.append([valor, sol])
    sol_objetivo.sort(reverse=True)
    poblacion_ordenada = [fila[1] for fila in sol_objetivo]
    return poblacion_ordenada

#Vamos a crear poblacion_size numero de vectores de n longitud cada uno
def crear_poblacion_inicial(poblacion_size, n):
    def solucion_random(n):
        solucion = []
        for j in range(n):
            solucion.append(random.randint(0, 1))
        return solucion

    poblacion = []
    for i in range(poblacion_size):
        poblacion.append(solucion_random(n))
    return poblacion




def muta_individuos(problema_genetico, poblacion, mejor_anterior, prob, peso_max, data, num_obj):
    mutacion = list(map(lambda x: problema_genetico.mutacion(x, prob), poblacion))
    mutacion = fun_obj(mutacion, peso_max, num_obj, data)
    if aux.calcular_valor(data["imp"], mutacion, num_obj) < aux.calcular_valor(data["imp"], mejor_anterior, num_obj):
        mutacion.pop()
        mutacion = [mejor_anterior] + mutacion
    return mutacion



def competicion(problema_genetico, poblacion, num_obj, peso_max, data):
    mejor_anterior = poblacion[0][:] #cogemos la primera solucion de la poblacion
    participantes = problema_genetico.longitud_individuos
    sol_participantes = []
    ruleta=[]

    #participantes a elegir
    for k in range(0, participantes):
        ruleta += [k] * (participantes - k)
    for _ in range(participantes):
        sol_participantes.append(random.choice(ruleta))

    # REPRODUCCION
    sol_nuevos = []
    #los hijos

    for j in range(participantes // 2):
        sol_nuevo = problema_genetico.cruce(poblacion[sol_participantes[2 * j]], poblacion[sol_participantes[2 * j + 1]], num_obj)
        sol_nuevos.append(sol_nuevo)


    for _ in range(participantes  // 2):
        poblacion.pop()

    poblacion = poblacion + sol_nuevos
    poblacion = fun_obj(poblacion, peso_max, num_obj, data)
    return poblacion, mejor_anterior



####LECTURA DATA
path_data = "C:/Users/sofia.chazarra/OneDrive - Accenture/Documents/MasterUCM/OptimizacionII/DatosMochila/kplib-master/"
file="00Uncorrelated/n00050/R01000/s001.kp"
poblacion_size = 51
iteraciones = 20
prob_mutar=0.2

#num objeto tiene el tamaño de la muestra
peso_max, num_obj, data = aux.read_data(path_data, file)

#Crea una lista con nº: poblacion_size de poblaciones iniciales. Cada poblacion inicial tiene una longitud de num_obj
poblacion = crear_poblacion_inicial(poblacion_size, num_obj)


#A la poblacion inicial le aplicamos nuestra funcion objetivo
poblacion = fun_obj(poblacion, peso_max, num_obj, data)

# Instanciamos nuestro problema genetico
cuad_gen = Problema_Genetico([0, 1], poblacion, poblacion_size, iteraciones)

start=time.time()
for i in range(cuad_gen.iteraciones):
    poblacion, mejor_anterior = competicion(cuad_gen, poblacion, num_obj, peso_max, data)
    mutacion = muta_individuos(cuad_gen, poblacion, mejor_anterior, prob_mutar, peso_max, data, num_obj)

end=time.time()

print("Usando un algoritmo: GENETICO \n" + " Solución: " + str(poblacion[0]) + "\n Valor: " + str(
    aux.calcular_valor(data["imp"], poblacion[0], num_obj))+ "\n Peso: " + str(aux.calcular_peso(data["weight"], poblacion[0], num_obj)) + "\n Tiempo de cómputo = " + str(
    1000 * (end - start)) + " ms")