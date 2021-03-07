import random
import yaml
from Population import Population


class GA:
    with open("setting.yaml", 'r') as stream:
        config =yaml.load(stream ,Loader= yaml.FullLoader)
    SIZE_POPULATION = config['SIZE_POPULATION']
    CONDITION_STOP =  config['CONDITION_STOP'] 
    pc = config['pc']
    pm = config['pm']
    def __init__(self , sigma , n, f):
        self.pop = Population(size = GA.SIZE_POPULATION, sigma = sigma, n= n ,f = f)

    def crossover_mutation(self):
        a = random.randint(0, GA.SIZE_POPULATION -1 )
        b = random.randint(0, GA.SIZE_POPULATION -1 )
        while a == b:
            b = random.randint(0, GA.SIZE_POPULATION -1)
        ind1 = self.pop.pop[a]
        ind2 = self.pop.pop[b]
        p = random.random()
        if p < GA.pc:
            return self.pop.crossover(ind1,ind2)
        else:
            return self.pop.mutation(ind1) + self.pop.mutation(ind2)

    def run(self):
        i = 0
        while i < GA.CONDITION_STOP:
            child = []
            while len(child) < GA.SIZE_POPULATION:
                       child += self.crossover_mutation()
            self.pop.pop += child
            print(self.pop.get_best())
            self.pop.selection()
            i +=1    

