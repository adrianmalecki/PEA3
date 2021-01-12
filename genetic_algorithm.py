import copy
import random
from read_data import Read_data
from sys import maxsize

class GeneticAlgorithm:
    def __init__(self, nodes, max_time):
        self.mutation_rate = 0.1
        self.crossing_rate = 0.8
        self.nodes = nodes
        self.population_size = 10
        self.size = len(nodes)
        self.population = []
        self.best_cost = maxsize

    def find_solution(self, nodes):
        self.population = self.generate_population()
        for P1 in self.population:
            for P2 in self.population:
                if P1 is not P2:
                    rand = random.random()
                    if rand < self.crossing_rate:
                        child = self.PMX(P1,P2)
                        child_cost = self.calculate_cost(child)
                        if child_cost < self.best_cost:
                            self.best_cost = child_cost
                            self.best_path = child
                            self.best_time = self.current_time
                        #jeśli lepszy niz najgorszy


    def generate_population(self):
        help_list = []
        #for i in range(self.population_size):
        #    first_node = random.randint(0, self.size-1)
        #    if first_node not in help_list:
        #        help_list.append(first_node)
        #print("helplist: ",help_list)
        #for node in help_list:
        #    path = self.generate_solution(node)
        #    self.population.append(path)
        for i in range(self.population_size):
            path = self.generate_solution()
            help_list.append(path)
        return help_list

    def calculate_cost(self, path):
        cost = 0
        for i in range(1, len(path)):
            cost += self.nodes[path[i - 1]][path[i]]
        cost += self.nodes[path[len(self.nodes) - 1]][path[0]]
        return cost

    # bardziej ranodowo zrobić
    def generate_solution(self):
        help_list = []  # pusta lista do przeszukiwania drogi
        while len(help_list) != self.size:  # poki lista nie wypełniona
            rand = random.randint(0, self.size - 1)  # wylosowanie wierzchołka
            if rand not in help_list:  # jeżeli wylosowany wierzchołek nie znajduje sie w liście
                help_list.append(rand)  # dodanie tego wierzchołka
        return help_list  # zwrócenie losowej drogi



    def PMX(self, P1, P2):
        point1 = random.randint(0, self.size-2)
        child = []
        # zamineinc na labde
        for i in range(0, self.size):
            child.append(-1)
        print(point1)
        point2 = random.randint(point1 + 1, self.size-1)
        print(point2)
        for i in range(self.size):
            if i >= point1 and i <= point2:
                child[i] = P1[i]

        for k in range(point1, point2+1):
            if P2[k] not in child:
                j = P1[k]
                index = P2.index(j)
                if child[index] == -1:
                    child[index] = P2[k]
                else:
                    element = P1[index]
                    index2 = P2.index(element)
                    child[index2] = P2[k]

        for i in range(self.size):
            if child[i] == -1:
                child[i] = P2[i]
        print(child)
        return child

    def mutation_by_inversion(self, P):
        point1 = random.randint(0, self.size-2)
        point2 = random.randint(point1 + 1, self.size-1)
        slice = P[point1:point2+1]
        slice = slice[::-1]
        child = copy.deepcopy(P)
        child[point1:point2+1] = slice


rd = Read_data()
#file_name = input("Podaj nazwe pliku: ")
file_name = 'ftv47.atsp'
try:
    open(format(file_name), "r")
    nodes = rd.read_file(file_name)
#    print(nodes)
except IOError:
    print("Error!")

P1 = [1,2,3,4,5,6,7,8,9]
P2 = [9,3,7,8,2,6,5,1,4]
gn = GeneticAlgorithm(nodes,100)
#gn.PMX(P1, P2)
gn.find_solution(nodes)