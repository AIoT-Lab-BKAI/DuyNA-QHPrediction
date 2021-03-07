from GA import GA
import numpy as np
import random
import yaml





def f1(x):
    return sum(x.genes)+x.n

pop = GA([0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001 ,0.00001, 0.1,0.01], 5 , f1)

pop.run()
