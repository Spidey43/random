''' a single-digit multiplication table practice program
    that repeatedly generates random problems
    and gives feedback about wrong solutions '''

import sys
import random

def main():
    print('type "exit" at anytime to exit the program')

    # multiplication table saved as problem:solution
    table = {}

    # fill the table
    fill(table)

    # repeatedly generate problems
    while True:
        generate_problem(table)

# fills the dictionary containing the multiplication table
def fill(table):

    # i is the multiplicand
    for i in range(1, 9):

        # j is the multiplier
        for j in range(1, 9):

            # get i*j values as text to get the problem, multiply them to get the solution
            problem = str(i)+'*'+str(j)
            solution = i*j

            # add the problem:solution pair to the dictionary
            table.update({problem:solution})

def generate_problem(table):
    # choose a random problem from the table
    problem = random.choice(list(table.keys()))

    # print the problem and save the solution
    print('\n'+problem)
    solution = input()

    # exit the program if the user wants to exit
    if solution == 'exit':
        sys.exit()
    
    # give feedback if the solution is wrong
    product = int(solution)
    if product != table[problem]:
        print('wrong.  '+problem+' = '+str(table[problem])+'\n')

main()
