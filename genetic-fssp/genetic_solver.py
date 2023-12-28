from instance import Instance
from solution import Solution

import numpy as np


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

        for i in range(self.stop_generation):
            # Select the parents
            parents = self.selection()


    def selection(self):
        """Selection operator"""
        # Calculate the makespans of all solutions (chromosomes) in the generated population
        pop_makespans = dict()
        s = Solution(self.instance)
        solution_example = [2, 1, 0]
        s.calculate_makespan(solution_example)
        # for chrom in self.population:
        #     s = Solution(self.instance)
        #     c=chrom
        #     s.calculate_makespan(chrom)
        #     x=1


