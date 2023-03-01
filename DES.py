'''
Programa de simulación DES (Discrete Event Simulation)
usando el módulo SimPy.

Autores: Diego Leiva
            Pablo Orellana

Referencia de ejemplos de Malonso-UVG
'''

import random as rnd
import simpy as smp

#Parametro de Simulacion
Random_Seed = 2912      #Semilla para la generacion de numeros al azar
Process_Qty = 25        #Cantidad de procesos a simular
Interval = 10           #Intervalo para la creacion de procesos
RAM_Capacity = 100      #Cantidad de Memoria RAM de la computadora
CPU_Cores = 1           #Cantidad de procesadores

#Informacion de simulacion
Time_of_Execution = 0   #Tiempo que tomo la ejecucion de un proceso
Time_List = []          #Listado con los tiempos de ejecucion de los procesos simulados


def ProcessBuilder():
    print("xd")

'''Instancia de metodo encargado de realizar los diferentes eventos para un proceso'''
def Process(env,id,cpu,ram):

    #Condiciones iniciales del proceso
    Start_Time = 0.0                        #Tiempo de la simulacion en que inicio el proceso
    Finish_Time = 0.0                       #Tiempo de la simulacion en que se termino el proceso
    Process_Completed = False               #Si el proceso ha terminado o no
    Memory_Qty = rnd.randint(1,10)          #Cantidad de memoria que el proceso requiere
    Intructions_Qty = rnd.randint(1,10)     #Cantidad de instrucciones a realizar

    #Evento NEW, cuando el proceso llega al sistema
    print("NEW")
    print(f'Proceso: {id}')
    print(f'Inicializado en: {env.now}')
    print(f'Cantidad de memoria utilizada: {Memory_Qty}\n')
    Start_Time = env.now

   


#Simulacion
rnd.seed(Random_Seed)
env = smp.Environment()
cpu = smp.Resource(env, capacity=CPU_Cores)
ram = smp.Container(env, init=RAM_Capacity,capacity=RAM_Capacity)