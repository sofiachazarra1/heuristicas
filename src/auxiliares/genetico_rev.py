# -*- coding: utf-8 -*-


# Genético

import time
import random

#  Sea el problema de la mochila max { z = c'x | a'x <= b; x binaria} cuyos datos se describen a continuacion.

n = 25 
peso_max = 471
valor = [53, 55, 52, 50, 52, 51, 53, 50, 52, 54, 51, 55, 51, 53, 53, 52, 53, 55, 55, 52, 52, 54, 55, 51, 55]
peso = [21, 27, 22, 23, 29, 24, 27, 29, 21, 25, 29, 21, 22, 23, 28, 25, 22, 24, 22, 28, 27, 28, 25, 28, 29]

###############################################################################################################################

poblacion_size = 200
n_sol_para_reproducir = 10*2 #Numero de hijos que queremos * 2
probabilidad_de_mutar = 20 #Frecuencia de mutación del 0 al 100
max_genes_mutan = 3 # Al mutar cuantos elementos queremos cambiar como máximo
iteraciones = 200

###############################################################################################################################

ruleta = []
for k in range(0,poblacion_size):
    ruleta += [k]*(poblacion_size-k)

###calculos de peso y valor
def calcular_peso(x):
    peso_total = 0
    for i in range(n):
        if x[i] == 1:
            peso_total += peso[i]
    return peso_total

def calcular_valor(x):
    valor_total = 0
    for i in range(n):
        if x[i] == 1:
            valor_total += valor[i]
    return valor_total
###calculos de peso y valor

def peso_maximo_superado(x):
    peso_total = 0
    for i in range(n):
        if x[i] == 1:
            peso_total += peso[i]
    return peso_total > peso_max

def solucion_random():
    sol = []
    for j in range(n):
        sol.append(random.randint(0, 1))
    return sol

def crear_poblacion_inicial():
    poblacion = []
    for i in range(poblacion_size): 
        sol = solucion_random()
        poblacion.append(sol)
    print(poblacion)
    return poblacion


def funcion_aptitud(poblacion):
    aptitud = []
    for sol in poblacion: #Atraviesa todas las soluciones de la poblacion
        if peso_maximo_superado(sol): # Si supera el peso maximo entonces su valor será -(cantidad peso por encima del maximo)
            valor = peso_max - calcular_peso(sol)
        else:
            valor = calcular_valor(sol)
            print(valor)
        aptitud.append([valor, sol])
    
    aptitud.sort(reverse=True) #para que me lo ordene de menor coste a mayor con su cromosoma asociado
    poblacion_ordenada = [fila[1] for fila in aptitud]
    return poblacion_ordenada

def cruce(sol1, sol2): # Cruce uniforme
    sol_nuevo = []
    for i in range(n):
        sol_nuevo.append(random.choice([sol1[i], sol2[i]]))
    print("sol_nuevo")
    print(sol_nuevo)
    return sol_nuevo

def seleccion_y_reproduccion(poblacion): #Seleccion de ruleta + elitismo
    mejor_anterior=poblacion[0][:] # Para el elitismo

    #SELECCION
    orden = []  
    for _ in range(n_sol_para_reproducir): #cuantos cromosomas queremos seleccionar
        orden.append(random.choice(ruleta))

      
    #REPRODUCCION
    sol_nuevos= []        
    for j in range(n_sol_para_reproducir//2): #creamos los hijos de las parejas formadas en la parte anterior
        sol_nuevo = cruce(poblacion[orden[2*j]], poblacion[orden[2*j+1]])
        sol_nuevos.append(sol_nuevo)


    for _ in range(n_sol_para_reproducir//2):
        poblacion.pop() #Eliminamos el ultimo (el que menos valor posee)
    poblacion += sol_nuevos #Añadimos los hijos

    poblacion = funcion_aptitud(poblacion) #Evaluamos y ordenamos
    
    return poblacion, mejor_anterior

def mutacion(poblacion, mejor_anterior):
    for j in range(poblacion_size): 
        if random.randint(1, 100) <= probabilidad_de_mutar:
            for _ in range(1, random.randint(1, max_genes_mutan)): 
                numero = random.randint(0, n-1)
                poblacion[j][numero] = 1 - poblacion[j][numero]
    print("mutacion")
    print(poblacion)
    print("adios")
    poblacion = funcion_aptitud(poblacion)
    if calcular_valor(poblacion[0]) < calcular_valor(mejor_anterior): #Si no se ha superado el de la mejor iteracion le volvemos a incluir
        poblacion.pop()
        poblacion = [mejor_anterior] + poblacion
    return poblacion

###############################################################################################################################
tic = time.process_time()

poblacion = crear_poblacion_inicial()
poblacion = funcion_aptitud(poblacion)
#print(poblacion[0])
    
for i in range(iteraciones):
    poblacion, mejor_anterior = seleccion_y_reproduccion(poblacion)
    print("poblacion")
    print(poblacion)
    print(len(poblacion))
    print("mejor_anterior")
    print(len(mejor_anterior))
    poblacion = mutacion(poblacion, mejor_anterior)

tac = time.process_time()

###############################################################################################################################

print("Usando un algoritmo: GENETICO \n" + " Solución: " + str(poblacion[0]) + "\n Valor: " + str(calcular_valor(poblacion[0])) + "\n Peso: " + str(calcular_peso(poblacion[0])) + "\n Tiempo de cómputo = " + str(1000*(tac - tic)) + " ms")
