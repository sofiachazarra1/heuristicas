import random
import time
import src.auxiliares.read_data as aux

class Problema_Genetico(object):
    """ Clase para representar un problema para que sea abordado mediante un
    algoritmo genetico general. Consta de los siguientes atributos:
    - genes: lista de posibles genes en un cromosoma [0,1] Un gen por variable de decisión binaria
    - decodifica: lista inicial de cromosomas
    - longitud_individuos: nº de cromosomas
    - fitness: metodo de valoracion de los cromosomas. Es nuestra función objetivo
    - iteraciones: nº de iteraciones que se hacen sobre los cromosomas"""

    def __init__(self, genes, decodifica, poblacion_size, fitness, iteraciones):
        self.genes = genes
        self.decodifica = decodifica
        self.longitud_individuos = poblacion_size
        self.fitness = fitness
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

    def cruce(self, cromosoma1, cromosoma2):
        """Los atributos son:
        - cromosoma1: lista con valores 1 u 0 para el primer cromosoma.
        - cromosoma2: lista con valores 1 u 0 para el segundo cromosoma. """
        pos = random.randrange(1, self.longitud_individuos - 1)
        cr1 = cromosoma1[:pos] + cromosoma2[pos:]
        cr2 = cromosoma1[:pos] + cromosoma2[pos:]
        return [cr1, cr2]



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
    print("poblacion inicial es:" + str(poblacion))
    return poblacion


def cruza_padres(problema_genetico, padres):
    hijos = []
    for j in range(0, len(padres), 2):
        if type(padres[j:j + 1][0]) == list:
            if type(padres[j:j + 1][0][0]) == list:
                padres_list0 = padres[j:j + 1][0][0]
                padres_list1 = padres[j + 1:j + 2][0][0]
            else:
                padres_list0 = padres[j:j + 1][0]
                padres_list1 = padres[j + 1:j + 2][0]
        else:
            padres_list0 = padres[j:j + 1]
            padres_list1 = padres[j + 1:j + 2]
        hijos.extend(problema_genetico.cruce(padres_list0, padres_list1))

    return hijos


def muta_individuos(problema_genetico, poblacion, prob):
    return list(map(lambda x: problema_genetico.mutacion(x, prob), poblacion))


def selecciona_uno_por_torneo(problema_genetico, poblacion, num_obj, data, peso_tot):
    #participantes = random.sample(poblacion, num_obj)

    #try:
    #nos quedamos con uno de nuestra muetra
    solucion_torneo = problema_genetico.fitness(poblacion, peso_tot, num_obj, data)
    return solucion_torneo
    #except Exception as e:
    #    print(e)


def seleccion_por_torneo(problema_genetico, poblacion, num_obj, data, peso_tot, n_padres_directos):
    sel_fam = []
    print(n_padres_directos)
    for i in range(n_padres_directos):
        print(i)
        gen_fam = selecciona_uno_por_torneo(problema_genetico, poblacion, num_obj, data, peso_tot)
        sel_fam.append(gen_fam)
    #print(sel_fam)
    return sel_fam

def nueva_generacion_t(problema_genetico, num_obj, data, peso_tot, poblacion, n_padres, n_directos, prob_mutar):
    print("seleciona por torneo padre")
    padres = seleccion_por_torneo(problema_genetico, poblacion, num_obj, data, peso_tot, n_padres)
    print("seleciona por torneo directo")
    directos = seleccion_por_torneo(problema_genetico, poblacion, num_obj, data, peso_tot, n_directos)
    print("seleciona por torneo hijo")
    hijos = cruza_padres(problema_genetico, padres)
    print("mutacion")
    mutacion = muta_individuos(problema_genetico, hijos + directos, prob_mutar)
    return mutacion


# Funcion principal
def algoritmo_genetico_t(problema_genetico, num_obj, data, peso_tot, tamano, prop_cruces, prob_mutar):
    """ - problema_genetico: clase instanciadas donde tenemos nuestros atributos
        - k: numero para la muestra sample
        - opt: funcion max o min
        - poblacion_size: numero de iteraciones que vamos a hacer
        - tamano: tamaño del cromosoma
        - prop_cruces: probabilidad de que un cromosoma cruce con otro
        - prob_mutar: probabilidad de mutacion de un cromosoma """
    poblacion = problema_genetico.decodifica
    #poblacion_size = problema_genetico.longitud_individuos
    iteraciones = problema_genetico.iteraciones
    n_padres = round(tamano * prop_cruces)
    n_padres = (n_padres if n_padres % 2 == 0 else n_padres - 1)
    n_directos = tamano - n_padres
    for i in range(iteraciones):
        print("i_algoritmo_genetico:" + str(i))
        poblacion = nueva_generacion_t(problema_genetico, num_obj, data, peso_tot, poblacion, n_padres, n_directos, prob_mutar)
    mejor_cr = max(poblacion, key=problema_genetico.fitness)
    return (problema_genetico.fitness(mejor_cr))





# Definimos nuestra funcion objetivo que utilizamos para elegir los genes
def fun_obj(poblacion, peso_max, n, data):
    sol_objetivo = []
    for sol in poblacion:
        valor = aux.calcular_valor(data["imp"], sol, n)
        peso = aux.calcular_peso(data["weight"], sol, n)
        if peso > peso_max:
            valor = peso_max - peso
        sol_objetivo.append([valor, sol])
    print("solreverse"+str(sol_objetivo))
    sol_objetivo.sort(reverse=True)
    poblacion_ordenada = [fila[1] for fila in sol_objetivo]
    return poblacion_ordenada


"""


res=algoritmo_genetico_t(cuad_gen,3,max,30,30,0.7,0.1)
"""

###############################################################################################################################
start = time.time()
poblacion_size = 30
n_sol_para_reproducir = 10*2 #Numero de hijos que queremos * 2
probabilidad_de_mutar = 20 #Frecuencia de mutación del 0 al 100
max_genes_mutan = 3 # Al mutar cuantos elementos queremos cambiar como máximo
iteraciones = 20
n=30 #poblacion inicial

####LECTURA DATA
path_data = "C:/Users/sofia.chazarra/OneDrive - Accenture/Documents/MasterUCM/OptimizacionII/DatosMochila/kplib-master/"
file="00Uncorrelated/n00050/R01000/s001.kp"

#num objeto tiene el tamaño de la muestra
peso_tot, num_obj, data = aux.read_data(path_data, file)
num_obj=30
#Crea una lista con nº: poblacion_size de poblaciones iniciales. Cada poblacion inicial tiene una longitud de num_obj
poblacion = crear_poblacion_inicial(poblacion_size, num_obj)


#A la poblacion inicial le aplicamos nuestra funcion objetivo
poblacion = fun_obj(poblacion, peso_tot, num_obj, data)



# Otra cosa mariposa
cuad_gen = Problema_Genetico([0, 1], poblacion, poblacion_size, fun_obj, iteraciones)


res = algoritmo_genetico_t(cuad_gen, num_obj, data, peso_tot, 50, 0.7, 0.1)
breakpoint()
end = time.process_time()
###############################################################################################################################

print("Usando un algoritmo: GENETICO \n" + " Solución: " + str(poblacion[0]) + "\n Valor: " + str(
    aux.calcular_valor(poblacion[0]))+ "\n Peso: " + str(aux.calcular_peso(poblacion[0])) + "\n Tiempo de cómputo = " + str(
    1000 * (end - start)) + " ms")
