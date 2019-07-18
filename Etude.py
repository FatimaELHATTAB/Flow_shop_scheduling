import solve_problem
import numpy as np
import csv

list_job = [200]
list_machine = [10,20]
list_probabilite = [0, 0.2, 0.4, 0.6, 0.9]
list_population = [25]
list_generation = [30]


def AG_study():
    # on parcours tous les tailles d'instanc10]
    test_AG(4,100,10)
    for j in list_machine:
        for k in list_job:
            # on parcours tous les problemes
            for i in range(1, 11):
                print("probleme ", i, j, k, "  : \n")
                makespan_list = []
                test_AG(i, k, j)
                # toutes les combinaisons possibles de probabilites et de taille population et taille generation
                """for p in list_probabilite:
                    for o in list_population:
                        for g in list_generation:
                            sequence, makespan = solve_problem.solve_benchmark_problem(i,k,j,o,g,p)
                            makespan_list.append(makespan)
                print(makespan_list)
                print(np.min(makespan_list))
                pd.Da
                """
    for m in range(1, 11):
        print("probleme ", m, 20, 500, "  : \n")
        makespan_list = []
        test_AG(m, 500, 20)



def test_AG(instance, job, machine):
    print("probleme ", instance, job, machine, "  : \n")
    makespan_list = []
    min = 10000000
    population = 0
    generation = 0
    proba = 0
    makespan_parameter = {}
    # toutes les combinaisons possibles de probabilites et de taille population et taille generation
    for p in list_probabilite:
        for o in list_population:
            for g in list_generation:
                sequence, makespan = solve_problem.solve_benchmark_problem(instance, job, machine, o, g, p)
                if makespan < min:
                    min = makespan
                    population = o
                    generation = g
                    proba = p
                    # makespan_parameter.append({makespan:[p,o,g]})
                    print("mutations probabilite: ", p, "generation", g, "population", o, "resultat", makespan)
    """print(makespan_list)
    minimum = np.min(makespan_list)
    print(makespan_parameter.fromkeys(minimum))
    """

    row = []
    row.append(str(instance) + str(machine) + str(job) + ".txt")
    row.append(sequence)
    row.append(min)
    row.append(proba)
    row.append(population)
    row.append(generation)
    print(row)
    with open('resultat5.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)
    csvFile.close()
