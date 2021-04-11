import random
import yaml
from ga.Individual import Individual
import datetime
import pytz

class Population:
    with open("settings/ga/setting.yaml", 'r') as stream:
        config =yaml.load(stream ,Loader= yaml.FullLoader)
    pc1p = config['pc1p']
    pc2p = config['pc2p']
    pBLX = config['pBLX']
    pAMOX = config['pAMOX']
    sm =config['sigma']
    pmx = config['pmx']
    pmi2 = config['pmi2']
    file_name = config['populationInit']
    pselection = config['selection']
    pwar = config['war']
    prulet = config['rulet']

    def __init__(self, size, sigma,f):
        self.sigma = sigma
        self.size = size
        self.pop = []
        self.fitness = f
        self.k = 0
        if Population.file_name != 'None':
            file = open(Population.file_name,'r')
            preline = file.readline()
            self.k = int(preline)
            while preline:
                print(preline)
                preline = file.readline()
                if len(preline)<1:
                    break
                s = preline.split()
                l = len(s)
                ssa = [int(x) for x in s[0:l-2]]
                n = int(s[l-2])
                fitness = float(s[l-1])
                ind = Individual(sigma)
                ind.set_genes(ssa)
                ind.set_n(n)
                ind.value_fitness = fitness
                self.pop.append(ind)

            f2 = open("log/ga/runtime.txt","a+")
            f2.seek(0,2)
            f2.write("Load population ... \n")
            f2.close()

        else:    
            for i in range(self.size):
                ind = Individual(sigma)

                print('----------khoi tao con thu i: ',i,">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                print("-->")           
                f2 = open("log/ga/runtime.txt","a+")
                f2.seek(0,2)
                f2.write("bat dau khoi tao: \n")
                f2.write(ind.__str__())
                f2.close()
                print(ind)
                print("-->")
                print("-->")
            
                ind.value_fitness = self.fitness(ind)
                ind.time = datetime.datetime.now(pytz.timezone('Asia/Ho_Chi_Minh'))
                self.pop.append(ind)
                
                f2 = open("log/ga/runtime.txt","a+")
                f2.seek(0,2)
                f2.write("khoi tao xong: \n")
                f2.write(ind.__str__())
                f2.write("\n")
                f2.close()
                f0 = open("log/ga/init.txt","a+")
                f0.seek(0,2)
                f0.write(ind.__str__())
                f0.write("\n")
                f0.close()
                print("----------------<<>><><<<<<<<<<<<<<<<<<<<<<<<>..................>>>>>>>-----------------------------------")            
                print(ind)
                print("--")

            self.pop = sorted(self.pop, key= lambda x : x.value_fitness)   
            

            file_name="log/ga/population0.txt"
            fi = open(file_name,'w+')
            fi.write("0")
            fi.write('\n')
            fi.close()

            for x in self.pop:
                x.write_file(file_name,'a+')
        self.get_best(self.k)  
        
      
    
    def  crossover_one_point(self, parent1, parent2):
        n1 = random.randint(1,len(parent1)-1)
        child1 = [0]*len(parent1)
        child2 = [0]*len(parent1)
        for i in range(0, n1):
            child1[i] = parent1[i]
            child2[i] = parent2[i]
        for i in range(n1, len(parent1)):
            child1[i] = parent2[i]
            child2[i] = parent1[i]
        return [child1, child2]
    
    
    def crossover_two_point(self, parent1, parent2):
        n1 = random.randint(0,len(parent1) -1)
        n2 = random.randint(0,len(parent1) -1)
        while n1 == n2:
            n2 = random.randint(0,len(parent1) -1)

        if n1 > n2:
            n1, n2 = n2, n1
        child1 = [0]*len(parent1)
        child2 = [0]*len(parent1)
        for i in range(0, n1):
            child1[i] = parent1[i]
            child2[i] = parent2[i]
        for i in range(n1, n2+1):
            child1[i] = parent2[i]
            child2[i] = parent1[i]
        for i in range(n2+1, len(parent1)):
            child1[i] = parent1[i]
            child2[i] = parent2[i]
        return [child1, child2]

    def BLX(self, parent1, parent2):
        n1 = parent1
        n2 = parent2
        if n1 > n2:
            n1, n2 = n2, n1
        alpha = int((n2 - n1)/2)
        n2 += alpha
        n1 -= alpha
        if n1 < 2 :
            n1 = 2
        return random.randint(n1, n2)

    def AMOX(self, parent1, parent2):
        alpha = random.random()
        return int( alpha*parent1 + (1- alpha)*parent2 ) 
    

    def crossover(self, parent1, parent2):
        f2 = open("log/ga/runtime.txt","a+")
        f2.seek(0,2)
        f2.write("lai ghep: \n")
        f2.close()
        child1 = Individual(self.sigma)
        child2 = Individual(self.sigma) 
        r = random.random()
        if r < Population.pc1p:
            a = self.crossover_one_point(parent1.genes, parent2.genes)
            child1.set_genes(a[0])
            child2.set_genes(a[1])
        else:
            a = self.crossover_two_point(parent1.genes, parent2.genes)
            child1.set_genes(a[0])
            child2.set_genes(a[1])
        
        if r < Population.pAMOX:
            child1.set_n(self.AMOX(parent1.n, parent2.n))
            child2.set_n(self.AMOX(parent1.n, parent2.n))
        else:
            child1.set_n(self.BLX(parent1.n, parent2.n))
            child2.set_n(self.BLX(parent1.n, parent2.n))
        
        child1.value_fitness = self.fitness(child1)
        child1.time = datetime.datetime.now(pytz.timezone('Asia/Ho_Chi_Minh'))
        child2.value_fitness = self.fitness(child2)
        child2.time = datetime.datetime.now(pytz.timezone('Asia/Ho_Chi_Minh'))
        
        
        f2 = open("log/ga/runtime.txt","a+")
        f2.seek(0,2)
        f2.write(parent1.__str__())
        f2.write("\n")
        f2.write(parent2.__str__())
        f2.write("\n----------------\n")
        f2.write(child1.__str__())
        f2.write("\n")
        f2.write(child2.__str__())
        f2.write("\n----------------\n")
        f2.close()

        return [child1, child2]

    def mutation(self, ind):
        f2 = open("log/ga/runtime.txt","a+")
        f2.seek(0,2)
        f2.write("Dot bien: \n")
        f2.close()


        parent1 = ind.genes
        child1 = [ i for i in parent1]
        pmm = random.random()
        if pmm < Population.pmx:
            s = 0
            for i in range(len(parent1)):
                s += (1-self.sigma[i], self.sigma[i])[parent1[i] == 0] 
            k = random.random()*s
            a =0
            for i in range(len(parent1)):
                if a <= k <= a + (1-self.sigma[i], self.sigma[i])[parent1[i] == 0]:
                    child1[i] = 1 - child1[i]
                    break
                a += (1-self.sigma[i], self.sigma[i])[parent1[i] == 0]
        elif pmm < Population.pmi2 + Population.pmx:
            n1 = random.randint(0, len(parent1) -1 )
            n2 = random.randint(0, len(parent1) -1 )
            while n1 == n2:
                n2 = random.randint(0, len(parent1) -1)
            if n1 > n2:
                n1, n2 = n2, n1
            for j in range(n1, n2+1):
                child1[j] = 1- parent1[j]

        else :
            k = random.randint(0 ,len(parent1)-1)
            child1[k] = 1 - child1[k]
        
        
        child = Individual(self.sigma)
        child.set_genes(child1)
        child.set_n(int(random.gauss(ind.n, Population.sm)))
        child.value_fitness = self.fitness(child)
        child.time = datetime.datetime.now(pytz.timezone('Asia/Ho_Chi_Minh'))

        f2 = open("log/ga/runtime.txt","a+")
        f2.seek(0,2)
        f2.write(ind.__str__())
        f2.write("\n----------------\n")
        f2.write(child.__str__())
        f2.write("\n----------------\n")
        f2.close()


        return [child]
    
    
    def get_best(self,i):
        best = open("log/ga/best.txt","a+")
        best.write(str(i)+" :: ")
        best.write(self.pop[0].__str__())
        best.write('\n')
        best.close()

    def inverse_fitness(self,fitness):
        return 100000000 - fitness

    def selection(self):

        n_selection = self.size*Population.pselection
        n_war = self.size*Population.pwar
        n_rulet = self.size*Population.prulet

        pop_sorted = sorted(self.pop, key= lambda x : x.value_fitness)
        pop_child  = pop_sorted[0:n_selection]
        pop_war = pop_sorted[n_selection:]
        pop_rulet = pop_sorted[n_selection:]

        k = 0;
        while k < n_war :
            a = random.randint(0, self.size*2-n_war - 1 )
            b = random.randint(0, self.size*2-n_war - 1 )
            while a == b:
                b = random.randint(0, self.size*2-n_war - 1 )
            c = min(a,b)
            pop_child.append(pop_war[c])
            k+=1
        
        
        list_f = []
        sum_fitness =0
        for ind in pop_rulet:
            sum_fitness += self.inverse_fitness(ind.value_fitness)
        for ind in pop_rulet:
            list_f.append(float(self.inverse_fitness(ind.value_fitness)/sum_fitness))
        k=0
        while k< n_rulet:
            a = random.random()
            s = 0
            for i in range(len(list_f)):
                if a < s+ list_f[i]:
                    pop_child.append( pop_rulet[i] )
                    break
                s+=list_f[i]
            k+=1
        self.pop = sorted(pop_child, key= lambda x : x.value_fitness)
