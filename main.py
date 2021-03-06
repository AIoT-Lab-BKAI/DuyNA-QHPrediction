from GA import GA
import numpy as np
import random


def f1(x):
    return sum(x.genes)+x.n

pop = GA([0.1, 0.1, 0.1, 0.1, 0.1], 2 , f1)

pop.run()