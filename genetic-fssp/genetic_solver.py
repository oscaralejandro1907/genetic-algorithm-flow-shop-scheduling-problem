from instance import Instance
import numpy as np


class Solver:
    def __init__(self, i: Instance, n_pop, pc, pm, stop):
        self.instance = i
        self.n_population = n_pop  # Population size
        self.prob_crossover = pc  # Probability of crossover
        self.prob_mutation = pm  # Probability of mutation
        self.stop_generation = stop  # stopping condition

        self.populations = []

        # Create populations. Each population will be created as a random permutation of jobs, with its ids.
        # We will end with a list of populations which size will be the n_pop we defined.
        for i in range(self.n_population):
            p = list(np.random.permutation(self.instance.n_jobs))
            while p in self.populations:  # if the population exists generate another, to avoid repetition
                p = list(np.random.permutation(self.instance.n_jobs))
            self.populations.append(p)

        for i in range(self.stop_generation):
            # Select the parents
            parents = self.selection()


    def selection(self):
        """Selection operator"""
        # Calculate the makespans of all generated populations
        pop_makespans = dict()
        for pop in self.populations:
            print(pop)

