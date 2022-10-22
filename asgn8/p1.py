import numpy as np
import random
import pickle

def get_k_max(N:int, gamma:float):
    """
    z = [1 − F (z)]^(−1/(gamma - 1))
    return max
    """
    assert N > 0
    assert gamma > 1
    exponent = -1/(gamma-1)
    samples = [(1 - np.random.uniform())**exponent for _ in range(N)]
    return np.max(samples)

Ns = [10**i for i in range(1,7)]
n = 1000
gamma = 3/2

k_maxes = {}
for N in Ns:
    print("N = ", N)
    k_maxes[N] = [get_k_max(N, gamma) for _ in range(1000)]

# write dict
exp_file = open('experiment', 'wb')
pickle.dump(k_maxes, exp_file)
exp_file.close()