# This is a Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from sys import argv
from instance import Instance
from genetic_solver import Solver

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        filename = argv[1]
    except:
        filename = 'VFR10_3_1_Gap.txt'

    data = Instance(filename)
    fssp = Solver(data, n_pop=5, pc=1.0, pm=1.0, stop=50)
    x=3

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
