import copy
import random
import time

from read_data import Read_data
from sys import maxsize


class GeneticAlgorithm:
    def __init__(self, nodes, max_time):
        self.mutation_rate = 0
        self.crossing_rate = 0
        self.nodes = nodes
        self.population_size = 20
        self.size = len(nodes)
        self.population = []
        self.best_cost = maxsize
        self.deadline = max_time
        self.nodes = nodes
        self.size = len(nodes)

    def check_data_init(self):
        if self.deadline == 0:
            self.deadline = 100
        if self.mutation_rate == 0:
            self.mutation_rate = 0.1
        if self.crossing_rate == 0:
            self.crossing_rate = 0.8

    def find_solution(self):
        self.check_data_init()
        total_time = 0
        find_time = 0
        duration = 0
        self.population = self.generate_population()
        while (duration < self.deadline):
            duration = time.process_time()
            for i in range(0, self.population_size):
                for j in range(0, self.population_size):
                    P1 = self.population[i][0]
                    P2 = self.population[j][0]
                    if P1 is not P2:
                        rand = random.random()
                        if rand < self.crossing_rate:
                            child = self.PMX(P1, P2)
                            child_cost = self.calculate_cost(child)
                            # jeśli najlepszy
                            if child_cost < self.best_cost:
                                self.best_cost = child_cost
                                self.best_path = child

                            self.population.append([child, child_cost])

            self.population.sort(key=self.myFunc)
            help_list = []
            for k in range(0, self.population_size):
                help_list.append(self.population[k])
            self.population = help_list

            #rand = random.random()
            #if rand < self.mutation_rate:
            #    self.population[i][0] = self.mutation_by_inversion(self.population[i][0])
            #    self.population[i][1] = self.calculate_cost()

        return self.best_path, self.best_cost

    def myFunc(self, e):
        return e[1]

    def generate_population(self):
        help_list = []
        for i in range(self.population_size):
            path = random.sample(range(self.size), self.size)
            cost = self.calculate_cost(path)
            help_list.append([path, cost])
        help_list.sort(key=self.myFunc)
        return help_list

    def calculate_cost(self, path):
        cost = 0
        for i in range(1, len(path)):
            cost += self.nodes[path[i - 1]][path[i]]
        cost += self.nodes[path[len(self.nodes) - 1]][path[0]]
        return cost

    def PMX(self, P1, P2):

        point1 = random.randint(0, self.size - 2)
        child = []
        for i in range(0, self.size):
            child.append(-1)

        point2 = random.randint(point1 + 1, self.size - 1)

        for i in range(self.size):
            if i >= point1 and i < point2:
                child[i] = P1[i]

        for k in range(point1, point2):
            if P2[k] not in child:
                a = P2[k]
                b = P2[k]
                while True:
                    j = P1[k]
                    index = P2.index(j)
                    if child[index] == -1:
                        child[index] = b
                        break
                    else:
                        a = j
                        k = P2.index(a)
        for i in range(self.size):
            if child[i] == -1:
                child[i] = P2[i]
        return child

    def mutation_by_inversion(self, P):
        point1 = random.randint(0, self.size - 2)
        point2 = random.randint(point1 + 1, self.size - 1)
        slice = P[point1:point2 + 1]
        slice = slice[::-1]
        child = copy.deepcopy(P)
        child[point1:point2 + 1] = slice


rd = Read_data()
# file_name = input("Podaj nazwe pliku: ")
file_name = 'ftv47.atsp'
try:
    open(format(file_name), "r")
    nodes = rd.read_file(file_name)
#    print(nodes)
except IOError:
    print("Error!")

gn = GeneticAlgorithm(nodes, 120)
# P1 = [5,9,6,3,2,1,0,8,4,7]
# P2 = [5,8,0,1,4,9,2,6,3,7]
# P1 = [4, 9, 2, 8, 3, 6, 5, 7, 0, 1]
# P2 = [0, 9, 5, 7, 1, 8, 3, 4, 2, 6]
# print(gn.PMX(P1, P2))
a, b = gn.find_solution()
print(a)
print(b)
