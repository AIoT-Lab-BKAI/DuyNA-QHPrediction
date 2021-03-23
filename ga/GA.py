import random
import yaml
from ga.Population import Population


class GA:
    with open("settings/ga/setting.yaml", 'r') as stream:
        config =yaml.load(stream ,Loader=  yaml.FullLoader)
    SIZE_POPULATION = config['SIZE_POPULATION']
    CONDITION_STOP =  config['CONDITION_STOP'] 
    pc = config['pc']
    pm = config['pm']
    def __init__(self , sigma ,  fitness):
        f0 = open("log/ga/init.txt", 'w')
        f0.write("Hello")
        print("hello>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        self.pop = Population(size = GA.SIZE_POPULATION, sigma = sigma,f = fitness)
        for ind in self.pop.pop:
            f0.write(ind)
        f0.write("close file")
        f0.close()

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
        f1 = open("log/ga/run.txt", 'w+')
        i = 0
        while i < GA.CONDITION_STOP:
            child = []
            while len(child) < GA.SIZE_POPULATION:
                       child += self.crossover_mutation()
            self.pop.pop += child
            print(self.pop.get_best())
            self.pop.selection()
            f1.write("----------------"+ i+ "--------------")
            for i in range(GA.SIZE_POPULATION):
                f1.write(self.pop.pop[i])
            i +=1
        f1.close()
        return self.pop.get_best()    

