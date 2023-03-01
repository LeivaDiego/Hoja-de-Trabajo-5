"""
Programa de simulación DES (Discrete Event Simulation)
usando el módulo SimPy.

Autores: Diego Leiva
            Pablo Orellana

Referencia de ejemplos de Malonso-UVG
"""

import random as rnd
import simpy as smp

# Parámetro de Simulación
Random_Seed = 2912  # Semilla para la generación de números al azar
Process_Qty = 25  # Cantidad de procesos a simular
Interval = 10  # Intervalo para la creación de procesos
RAM_Capacity = 100  # Cantidad de Memoria RAM de la computadora
CPU_Cores = 1  # Cantidad de procesadores

# Información de simulación
Time_of_Execution = 0  # Tiempo que tomo la ejecución de un proceso
Time_List = []  # Listado con los tiempos de ejecución de los procesos simulados


def process_builder():
    print("xd")


'''Instancia de método encargado de realizar los diferentes eventos para un proceso'''


def process_sim(env, id, cpu, ram):
    # Condiciones iniciales del proceso
    start_time = 0.0  # Tiempo de la simulación en que inicio el proceso
    finish_time = 0.0  # Tiempo de la simulación en que se terminó el proceso
    process_completed = False  # Si el proceso ha terminado o no
    memory_qty = rnd.randint(1, 10)  # Cantidad de memoria que el proceso requiere
    instructions_qty = rnd.randint(1, 10)  # Cantidad de instrucciones a realizar

    # Evento NEW, cuando el proceso llega al sistema
    print("NEW")
    print(f'Proceso: {id}')
    print(f'Inicializado en: {env.now}')
    print(f'Cantidad de memoria utilizada: {memory_qty}\n')
    start_time = env.now

    # Ciclo que permite realizar las instrucciones del proceso hasta que este termine
    while not process_completed:
        with cpu.request() as req:
            yield req
            yield env.timeout(1)
            yield ram.get(memory_qty)

            # Evento READY, cuando el proceso está listo para correr
            print("READY")
            print(f'Proceso: {id}')
            print(f'Listo para ejecutarse en: {env.now}')
            print(f'Cantidad de Instrucciones: {instructions_qty}\n')


# Simulación
rnd.seed(Random_Seed)
environment = smp.Environment()
CPU = smp.Resource(environment, capacity=CPU_Cores)
RAM = smp.Container(environment, init=RAM_Capacity, capacity=RAM_Capacity)
