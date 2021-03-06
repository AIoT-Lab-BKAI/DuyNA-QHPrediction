import random

class Individual:
    def __init__(self, sigma, n):
        self.size = len(sigma)
        self.genes = [0] * self.size
        for i in range(self.size):
            if random.random() < sigma[i] :
                self.genes[i] = 1
        self.n = random.randint(2, n) 
        self.value_fitness = 0

    def __str__(self):
        s ="ssa ="
        for i in self.genes:
            s += str(i) + ' '
        s +="  n =" + str(self.n) + "  fitness = " + str(self.value_fitness)
        return s

    def get_genes(self):
        return self.genes
    def get_n(self):
        return self.n
    
    def set_genes(self, genes):
        for i in range(self.size):
            self.genes[i] = genes[i]
    def set_n(self, n):
        self.n = n