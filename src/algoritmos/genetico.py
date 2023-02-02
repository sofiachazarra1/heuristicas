import random
import src.auxiliares.read_data as aux



class Problema_Genetico(object):
    """ Clase para representar un problema para que sea abordado mediante un
    algoritmo genetico general. Consta de los siguientes atributos:
    - genes: lista de posibles genes en un cromosoma [0,1] Un gen por variable de decisión binaria
    - decodifica: lista inicial de genes
    - longitud_individuos: la longitud de los cromosomas
    - fitness: metodo de valoracion de los cromosomas. Es nuestra función objetivo"""

    def __init__(self, genes, decodifica, fitness):
        self.genes = genes
        self.decodifica = decodifica
        self.longitud_individuos = len(decodifica)
        self.fitness = fitness

    def mutacion(self, cromosoma, prob):
        """Los atributos son:
        - cromosoma: lista con valores 1 u 0.
        - prob: probablidad de mutacion en base a unas probabilidades random de cada gen """
        # if type(cromosoma)==float:
        #    cromosoma=[cromosoma]
        # print("mutacion")
        # print(cromosoma)
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


def cruza_padres(problema_genetico, padres):
    hijos = []
    padres_list = []
    for j in range(0, len(padres), 2):
        if type(padres[j:j + 1][0]) == list:
            print(padres[j:j + 1][0])
            if type(padres[j:j + 1][0][0]) == list:
                padres_list0 = padres[j:j + 1][0][0]
                padres_list1 = padres[j + 1:j + 2][0][0]
                print("hola")
            else:
                padres_list0 = padres[j:j + 1][0]
                padres_list1 = padres[j + 1:j + 2][0]
        else:
            padres_list0 = padres[j:j + 1]
            padres_list1 = padres[j + 1:j + 2]
        hijos.extend(problema_genetico.cruce(padres_list0, padres_list1))

    return hijos


def muta_individuos(problema_genetico, poblacion, prob):
    # print("poblacion")
    return list(map(lambda x: problema_genetico.mutacion(x, prob), poblacion))


def selecciona_uno_por_torneo(problema_genetico, poblacion, k, opt):
    p = 0
    participantes = random.sample(poblacion, k)

    try:
        p = opt(participantes, key=problema_genetico.fitness)
        return p
    except Exception as e:
        print(e)
        print("poblacion")
        print(poblacion)
        print("lenpoblacion")
        print(len(poblacion))
        print("participantes")
        print(participantes)


def seleccion_por_torneo(problema_genetico, poblacion, n, k, opt):
    sel_fam = []
    for i in range(n):
        gen_fam = selecciona_uno_por_torneo(problema_genetico, poblacion, k, opt)
        sel_fam.append(gen_fam)
    return sel_fam


def nueva_generacion_t(problema_genetico, k, opt, poblacion, n_padres, n_directos, prob_mutar):
    padres = seleccion_por_torneo(problema_genetico, poblacion, n_padres, k, opt)
    directos = seleccion_por_torneo(problema_genetico, poblacion, n_directos, k, opt)
    hijos = cruza_padres(problema_genetico, padres)
    mutacion = muta_individuos(problema_genetico, hijos + directos, prob_mutar)
    return mutacion


# Funcion principal
def algoritmo_genetico_t(problema_genetico, k, opt, ngen, tamano, prop_cruces, prob_mutar):
    """ - problema_genetico: clase instanciadas donde tenemos nuestros atributos
        - k: numero para la muestra sample
        - opt: funcion max o min
        - ngen: numero de iteraciones que vamos a hacer
        - tamano: tamaño del cromosoma
        - prop_cruces: probabilidad de que un cromosoma cruce con otro
        - prob_mutar: probabilidad de mutacion de un cromosoma """
    poblacion = problema_genetico.decodifica
    n_padres = round(tamano * prop_cruces)
    n_padres = (n_padres if n_padres % 2 == 0 else n_padres - 1)
    n_directos = tamano - n_padres
    for i in range(ngen):
        print("i_algoritmo_genetico:" + str(i))
        print("poblacion_Antes" + str(poblacion))
        poblacion = nueva_generacion_t(problema_genetico, k, opt, poblacion, n_padres, n_directos, prob_mutar)
    print(poblacion)
    mejor_cr = opt(poblacion, key=problema_genetico.fitness)
    print(mejor_cr)
    return (problema_genetico.fitness(mejor_cr))


# Definimos nuestra funcion objetivo que utilizamos para elegir los genes
def fun_obj(x):
    return sum(b*(2**i) for (i,b) in enumerate(x))



cuad_gen = Problema_Genetico([0,1],
                             100,
                             fun_obj,
                             lambda x: (fun_obj(x))**2)




print("El primer cromosoma será:"+ str(cuad_gen.decodifica))

res=algoritmo_genetico_t(cuad_gen,3,max,30,30,0.7,0.1)
print("mejor resultado será:" + str(res))
