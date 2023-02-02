# -*- coding: utf-8 -*-

# Voraz Mochila

import time

#  Sea el problema de la mochila max { z = c'x | a'x <= b; x binaria} cuyos datos se describen a continuacion.

n = 25 
peso_max = 471
valor = [53, 55, 52, 50, 52, 51, 53, 50, 52, 54, 51, 55, 51, 53, 53, 52, 53, 55, 55, 52, 52, 54, 55, 51, 55]
peso = [21, 27, 22, 23, 29, 24, 27, 29, 21, 25, 29, 21, 22, 23, 28, 25, 22, 24, 22, 28, 27, 28, 25, 28, 29]

###############################################################################################################################

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

def peso_maximo_superado(x):
    peso_total = 0
    for i in range(n):
        if x[i] == 1:
            peso_total += peso[i]
    return peso_total > peso_max


def encontrar_indice():
    indice = rentabilidad.index(max(rentabilidad))
    return indice

###############################################################################################################################

tic = time.process_time()

x = [0]*n

# Cuanto mayor sea el precio y menor sea el peso mejor
rentabilidad =[valor[i]/peso[i] for i in range(n)]

while (not peso_maximo_superado(x)):
    i = encontrar_indice()
    rentabilidad[i] = 0
    x[i] = 1
x[i] = 0 #Ponemos el último que hemos añadido a 0, pues es el que ha hecho que se supere el peso.

tac = time.process_time()

###############################################################################################################################

print("Usando un algoritmo: VORAZ (CONSTRUCTIVO) \n" + " Solución: " + str(x) + "\n Valor: " + str(calcular_valor(x)) + "\n Peso: " + str(calcular_peso(x)) + "\n Tiempo de cómputo = " + str(1000*(tac - tic)) + " ms")