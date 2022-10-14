import random
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
import itertools
import pandas as pd
import multiprocessing

def run_simon(rho:float, t_steps: int = 10000):
    """
    rho:innovation rate
    t_steps: num_steps
    return : Counter(list of elements)
    """
    assert rho >= 0
    assert rho <= 1
    elements = []
    elements.append(1)
    set_of_groups = set(elements)
    for step in range(t_steps):
        if (step%1000 == 0):
            print("Step = ", step)
        dice = np.random.uniform()
        if dice < rho:
            # add a new element
            elements.append(max(set_of_groups)+1)
        else:
            # choose from population to make a choice
            elements.append(np.random.choice(list(set_of_groups)))
        set_of_groups = set(elements)
    return Counter(elements)     

if __name__ == "__main__":
    #  rho = 0.10, 0.01, and 0.001. 
    from multiprocessing import process
    p = Process(target=run_simon, args=(rho,))
    p.start()
    p.join()
    rhos = [0.10, 0.01, 0.001]
    groups = { r: [] for r in rhos}
    processes = []
    for rho in rhos:
    # run 10 experiments
        for i in range(10):
            print("experiment = ", i)
            groups[rho].append(run_simon(rho, t_steps = 10000))