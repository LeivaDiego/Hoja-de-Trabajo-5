'''
Programa de simulación DES (Discrete Event Simulation)
usando el módulo SimPy.

Autores:    Diego Leiva
            Pablo Orellana
'''

import random as rnd
import simpy as smp

#Parametro de Simulacion
Random_Seed = 2912
Process_Qty = 25
Interval = 5
RAM_Capacity = 100
CPU_Cores = 1

#Informacion de simulacion
Time_of_Execution = 0
Time_List = []

def ProcessBuilder():
    print("xd")

def Process(env,id,cpu,ram):
    Start_Time = 0.0
    Finish_Time = 0.0
    Process_Completed = False
    Memory_Qty = rnd.randint(1,10)
    Intructions_Qty = rnd.randint(1,10)




#Simulacion
rnd.seed(Random_Seed)
env = smp.Environment()
cpu = smp.Resource(env, capacity=CPU_Cores)
ram = smp.Container(env, init=RAM_Capacity,capacity=RAM_Capacity)