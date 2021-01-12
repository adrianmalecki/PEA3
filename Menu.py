from read_data import Read_data
from genetic_algorithm import GeneticAlgorithm

class Menu:
    def __init__(self):
        self.read_data = Read_data()
        self.nodes = []
        self.choice = 0
        self.max_time = 100
        self.a = 0
        self.temperature = 0

    def main_menu(self):
        while self.choice != 6:
            print('_________MENU_________')
            print('1. Wczytaj dane')
            print('2. Kryterium stopu(Czas w sekundach) ')
            print('3. Ustaw wielkość populacji początkowej')
            print('4. Ustaw współczynnik mutacji')
            print('5. Ustaw współczynnik krzyżowania')
            print('6. Uruchom algorytm')
            print('7. Wyjście')

            self.choice = input('Wybór: ')

            if self.choice == '1':
                self.read_data.show_avaiable_files()
                file_name = input("Podaj nazwe pliku: ")
                #file_name = 'ftv170.atsp'
                try:
                    open(format(file_name), "r")
                    self.nodes = self.read_data.read_file(file_name)
                    print(self.nodes)
                except IOError:
                    print("Error!")

            elif self.choice == '2':
                self.max_time = int(input("Podaj czas: "))

            elif self.choice == '3':
                pass

            elif self.choice == '4':
                pass

            elif self.choice == '5':
                pass

            elif self.choice == '6':
                self.genetic_alg = GeneticAlgorithm(self.nodes, self.max_time)
                # best_path, best_sol, find_time = self.tabu_search.find_solution()
                print('Ścieżka: ')
                print('Koszt: ')
                print('Czas: ')

            elif self.choice == '7':
                exit()

            else:
                print("Wprowadz poprawną liczbę")


M = Menu()
M.main_menu()