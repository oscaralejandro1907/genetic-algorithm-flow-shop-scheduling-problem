import random
import numpy as np

from instance import Instance
from solution import Solution


class Solver:
    def __init__(self, i: Instance, n_pop, pc, pm, stop):
        self.instance = i
        self.n_population = n_pop  # Population size
        self.prob_crossover = pc  # Probability of crossover
        self.prob_mutation = pm  # Probability of mutation
        self.stop_generation = stop  # stopping condition

        # Initialization. Randomly generate an initial population (set of solutions)
        self.population = []

        # Create population. Each chromosome (solution) will be created as a random permutation of jobs, with its ids.
        # We will end with a list of chromosomes (population) which size will be the n_pop we defined.
        for i in range(self.n_population):
            p = list(np.random.permutation(self.instance.n_jobs))
            while p in self.population:  # if the population exists generate another, to avoid repetition
                p = list(np.random.permutation(self.instance.n_jobs))
            self.population.append(p)

        # Run algorithm until stopping condition
        for i in range(self.stop_generation):
            # Select the parents
            parents = self.selection()

            children = list()

            # Apply crossover. Get children
            for pair in parents:
                children.append(self.crossover([self.population[pair[0]], self.population[pair[1]]]))

            # Mutate children
            for child in children:
                child = self.mutation(child)

            # Update population
            self.population = self.elitist_strategy(self.population, children)

        # Result
        best_sequence_index, best_makespan = self.best_solution(self.population)

        print(self.population[best_sequence_index])
        print(best_makespan)

    def selection(self):
        """Selection operator"""
        # Calculate the makespans of all solutions (chromosomes) in the generated population
        pop_makespans = dict()
        for i in range(self.n_population):
            s = Solution(self.instance)
            pop_makespans[i] = s.calculate_makespan(self.population[i])

        # Sort decreasing makespan
        pop_makespans = {k: v for k, v in sorted(pop_makespans.items(), reverse=True, key=lambda item: item[1])}

        distr = []
        distr_indexes = []

        for i in range(self.n_population):
            distr_indexes.append(list(pop_makespans.keys())[i])
            prob = (2*(i+1)) / (len(self.population)*(len(self.population)+1))
            distr.append(prob)

        parents = []

        while len(parents) != self.n_population:
            pair = list(np.random.choice(distr_indexes, 2, p=distr))
            if pair[0] != pair[1] and pair not in parents:
                parents.append(pair)

        return parents

    def crossover(self, parents):
        """Crossover operator. Generates a child from two parents"""
        points = list(np.random.permutation(np.arange(self.instance.n_jobs - 1) + 1)[:2])

        if points[0] > points[1]:
            points[0], points[1] = points[1], points[0]

        child = list(parents[0])

        for i in range(points[0], points[1]):
            child[i] = -1

        p = -1
        for i in range(points[0], points[1]):
            while True:
                p += 1
                if parents[1][p] not in child:
                    child[i] = parents[1][p]
                    break

        return child

    def mutation(self, child):
        """ Mutation operator"""
        # Select the job to be shifted.
        # For that, generate a list between [0 - n_jobs], shuffle it, and select 2 elements
        points = list(np.random.permutation(np.arange(self.instance.n_jobs))[:2])

        # Reorder points
        if points[0] > points[1]:
            points[0], points[1] = points[1], points[0]

        # the job to be moved will be the one at index of the second point to the first one, and shift the sequence
        moved_job = child[points[1]]

        for i in range(points[1], points[0], -1):
            child[i] = child[i - 1]

        child[points[0]] = moved_job

        return child

    def elitist_strategy(self,old_pop, new_pop):
        best_sol_index = 0
        s = Solution(self.instance)
        best_solution_makespan = s.calculate_makespan(old_pop[0])

        for i in range(1, len(old_pop)):
            s = Solution(self.instance)
            current_makespan = s.calculate_makespan(old_pop[i])
            if current_makespan < best_solution_makespan:
                best_solution_makespan = current_makespan
                best_sol_index = i

        random_index = random.randint(0, len(new_pop)-1)

        new_pop[random_index] = old_pop[best_sol_index]

        return new_pop

    def best_solution(self, population):
        s = Solution(self.instance)
        best_makespan = s.calculate_makespan(population[0])
        best_solution_index = 0

        for i in range(1, len(population)):
            s = Solution(self.instance)
            current_makespan = s.calculate_makespan(population[i])
            if current_makespan < best_makespan:
                best_makespan = current_makespan
                best_solution_index = i

        return best_solution_index, best_makespan
