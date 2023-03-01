'''
Programa de simulación DES (Discrete Event Simulation)
usando el módulo SimPy.

Autores:    Diego Leiva
            Pablo Orellana
'''

import random as rnd
import simpy as smp

#Parametro de Simulacion
processQty = 25
randomSeed = 2912
interval = 5
capacity = 1
processors = 1


#Informacion de simulacion
executionTime = 0
timesList = []

