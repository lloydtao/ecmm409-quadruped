from collections import Counter
from generation import Generation
from simulation import Simulation

import numpy as np
import pybullet as p
import random
import string


class Evolution:
    def __init__(self, pop_size=6, generations=6):
        self.pop_size = pop_size
        self.population = {}
        self.scores = {}

        self.generate_population()

        for i in range(generations):
            self.next()

        self.output()

    def generate_population(self):
        for n in range(self.pop_size):
            f_length = random.uniform(0.25, 2)
            f_width = random.uniform(0.25, 2)
            b_length = random.uniform(0.25, 2)
            b_width = random.uniform(0.25, 2)

            frontleg = [f_length, f_width, 1]
            backleg = [b_length, b_width, 1]
            legs = (frontleg, backleg)

            modelId = "".join(random.choice(string.digits) for i in range(8))
            self.population[modelId] = legs

    def fitness(self, modelId, legs):
        """Objective function to calculate score of a given member."""
        Generation.create_robot(legs=legs)

        s = Simulation(realtime=False)
        fitness = s.run()
        p.disconnect()

        return fitness

    def select(self, n=4):
        """Evaluate candidates in population and select fittest members."""
        k = Counter(self.scores)
        best_fit = k.most_common(n)
        return [i[0] for i in best_fit]

    def crossover(self, p1, p2):
        """Produce a child based on two parents."""
        p1_front_length = self.population[p1][0][0]
        p1_front_width = self.population[p1][0][1]
        p1_back_length = self.population[p1][1][0]
        p1_back_width = self.population[p1][1][1]

        p2_front_length = self.population[p2][0][0]
        p2_front_width = self.population[p2][0][1]
        p2_back_length = self.population[p2][1][0]
        p2_back_width = self.population[p2][1][1]

        new_front_length = random.uniform(p1_front_length, p2_front_length)
        new_front_width = random.uniform(p1_front_width, p2_front_width)
        new_back_length = random.uniform(p1_back_length, p2_back_length)
        new_back_width = random.uniform(p1_back_width, p2_back_width)

        # Perform mutation
        if random.uniform(0, 1) < 0.9:
            new_front_length += random.uniform(-0.1, 0.1)
        if random.uniform(0, 1) < 0.9:
            new_front_width += random.uniform(-0.1, 0.1)
        if random.uniform(0, 1) < 0.9:
            new_back_length += random.uniform(-0.1, 0.1)
        if random.uniform(0, 1) < 0.9:
            new_back_width += random.uniform(-0.1, 0.1)

        new_front = [new_front_length, new_front_width, 1]
        new_back = [new_back_length, new_back_width, 1]
        return (new_front, new_back)

    def next(self):
        self.scores = {}
        for modelId, legs in self.population.items():
            fitness = self.fitness(modelId, legs)
            self.scores[modelId] = fitness

        for key in self.population:
            print("Model", key, "scored", self.scores[key])

        fittest = self.select()
        print("Best models:", fittest)

        new_population = {}
        for i in range(0, len(fittest)):
            for j in range(i + 1, len(fittest)):
                modelId = "".join(random.choice(string.digits) for i in range(8))
                new_population[modelId] = self.crossover(fittest[i], fittest[j])
                print(new_population[modelId])

        self.population = new_population

    def output(self):
        self.scores = {}
        for modelId, legs in self.population.items():
            fitness = self.fitness(modelId, legs)
            self.scores[modelId] = fitness

        fittest = self.select(n=1)
        print(fittest[0])
        print(self.population)
        Generation.create_robot(legs=self.population[fittest[0]])

        s = Simulation(realtime=True)
        s.run()
        p.disconnect()


if __name__ == "__main__":
    e = Evolution()
