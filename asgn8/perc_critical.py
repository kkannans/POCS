# https://codereview.stackexchange.com/questions/210641/size-of-the-largest-connected-component-in-a-grid-in-python
# https://leetcode.com/problems/max-area-of-island/solution/
import numpy as np
import random
import pickle
from pprint import pprint

def distAreaOfIsland(grid):
    seen = set()
    count_size = {}
    for r0, row in enumerate(grid):
        for c0, val in enumerate(row):
            if val and (r0, c0) not in seen:
                shape = 0
                stack = [(r0, c0)]
                seen.add((r0, c0))
                while stack:
                    r, c = stack.pop()
                    shape += 1
                    for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                        if (0 <= nr < len(grid) and 0 <= nc < len(grid[0])
                                and grid[nr][nc] and (nr, nc) not in seen):
                            stack.append((nr, nc))
                            seen.add((nr, nc))
                if shape in count_size.keys():
                    count_size[shape] += 1
                else:
                    count_size[shape] = 1
    return count_size

def generate_grid(grid_size:int, prob:float):
    lattice_rand = np.random.rand(grid_size,grid_size)
    lattice = (lattice_rand < prob).astype(int)
    return lattice

L = 500
p_c = 0.6
p = [p_c, p_c/2.0,  p_c + (1 - p_c)/2.0]
num_experiments = 100
lcc_pc = {k: [] for k in p}
for prob in p:
    print("prob = ", prob)
    for i in range(num_experiments):
        if (i%10) == 0:
            print("experiment = ", i)
        count_sizes = distAreaOfIsland(generate_grid(L, prob))
        lcc_pc[prob].append(count_sizes)
exp_file = open('percolation_critical_analysis_L'+str(L)+'.pickle', 'wb')
pickle.dump(lcc_pc, exp_file)
exp_file.close()
