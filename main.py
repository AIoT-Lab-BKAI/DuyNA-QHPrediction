from GA import GA
import numpy as np
import random


def fitness(x):
    return sum(x.genes)+x.n

#sigma la sigma cua ssa khi da chuan hoa ve xac xuat
#ex:
sigma = [0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001 ,0.00001, 0.1,0.01]
pop = GA(sigma, fitness)
pop.run()
