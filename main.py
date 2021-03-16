from ga.GA import GA

def fitness(x):
    return sum(x.genes)+x.n

if __name__ == "__main__":
    training_result = run_script(sigma_lst=[1,2,3,4,5,6], num_model=3)
    #sigma la sigma cua ssa khi da chuan hoa ve xac xuat
    