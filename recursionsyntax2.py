"""
Testing the performance of difference loop structures.
Different loop structures are used to generate a list of lists
from an initial list called "DUMMY".

Each loop is then iterated many times and the time it takes
to execute each operation is measured using time.time().

Also testing out lexical scoping in Python by calling
functions defined in the global environment within other functions.

by MAS 10/2018
"""

###
#Import libraries

import time
import numpy as np
import seaborn as sns
import pylab as plt

#Set seaborn plotting defaults for data visualization
sns.set()

###
#Define constants

#Dummy list to do operations on
#Use as list, not range object
DUMMY = list(range(1,100))

#Number of tests
RUNS = 50

###
#Define different loop structures

#'Clunky' loop structure
def clunky(test_list):
    """This is a 'clunky' loop. The way I was taught
    in academic biophysics research.

    7 Lines Total.
    """
    temp = []
    final = []
    for x in range(len(test_list)):
        temp.append(test_list[x]+1)
        temp.append(test_list[x]+2)
        final.append(temp)
        temp = []
    return final

#'Less Clunky' loop structure
def less_clunky(test_list):
    """This loop is similar to clunky but does not use
    a temp list to store data.

    3 Lines Total.
    """
    final = []
    for x in range(len(test_list)):
        final.append([test_list[x]+1, test_list[x]+2])
    return final

#Pythonic loop structure
def pythonic(test_list):
    """This is a pythonic loop.

    1 Line Total.
    """
    final = [[entry+1, entry+2] for entry in test_list]
    return final

###
#Functions to time different loops structures

def time_test(test_list, test_function, trials=1000):
    """Repeat function to get measurable time.

    Keyword arguments:
    test_list -- list to perform operation on
    test_function -- function that carries out operation on test_list
    trials -- number of times to carry out operation (default 1000)
    """
    start = time.time()
    for trial in range(trials):
        new_test_list = test_function(test_list)
    total_time = time.time() - start
    return total_time

def time_group(test_list, test_function, tests=50):
    """Repeat time_test to get stats about performance.

    test_list -- list to perform operation on
    test_function -- function that carries out operation on test_list
    trials -- number of times to perform time_test (default 50)
    """
    times = [time_test(test_list, test_function) for test in range(tests)]
    return times

def plot(x_vars, y_vars):
    """Plot results.

    Box+Whisker Plot to show mean and stdv
    Beeswarm on top to show raw data
    """
    ax = sns.boxplot(x_vars, y_vars, linewidth=2.5)
    ax = sns.swarmplot(x_vars, y_vars, color='.25', size=8)
    ax.set_xticklabels(['Clunky', 'Less Clunky', 'Pythonic'])
    plt.tick_params(axis='both', which='major', labelsize=18)
    plt.ylabel('Elapsed Time (s)', fontsize=22)
    plt.show()
    return 0
        
#Main
def main(dummy_list, runs):
    """Main function to execute everything."""
    #List functions to test (functions are defined in global environment)
    all_functions = [clunky, less_clunky, pythonic]
    #Do the timing test
    out = [time_group(dummy_list,function,runs) for function in all_functions]
    #Flatten all_output for visualization (y-axis values)
    y_vars = [entry for sublist in out for entry in sublist]
    #Generate arbitrary indices (x-axis values) for visualization
    x_vars = [1]*runs + [2]*runs + [3]*runs
    #Visualize results (plot function defined in global environment)
    plot(x_vars, y_vars)
    return 0

if __name__ == '__main__':
    main(DUMMY, RUNS)
