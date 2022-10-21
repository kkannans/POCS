# https://codereview.stackexchange.com/questions/210641/size-of-the-largest-connected-component-in-a-grid-in-python
from collections import deque
import numpy as np
import random
from collections import OrderedDict
import pickle

def largest_connected_component(grid):
    EMPTY = 0
    FILLED = 1
    VISITED = 2

    def is_valid(x, y):
        return (0 <= x < len(grid) and 0 <= y < len(grid[0]) and
                grid[x][y] != VISITED)

    def traverse_component(x, y):
        grid[x][y] = VISITED
        result = 1
        for adjacent in ((x + 1, y),
                         (x - 1, y),
                         (x, y + 1),
                         (x, y - 1)):
            if (is_valid(*adjacent)):
                if (grid[adjacent[0]][adjacent[1]] == EMPTY):
                    q.append(adjacent)
                    grid[adjacent[0]][adjacent[1]] = VISITED
                else:
                    result += traverse_component(*adjacent)

        return result

    max_filled_size = 0
    q = deque()
    if (grid[0][0] == EMPTY):
        q.append((0, 0))
        grid[0][0] = VISITED
    else:
        max_filled_size = max(max_filled_size, traverse_component(0, 0))

    while q:
        x, y = q.popleft()

        for adjacent in ((x + 1, y),
                         (x - 1, y),
                         (x, y + 1),
                         (x, y - 1)):
            if (is_valid(*adjacent)):
                if (grid[adjacent[0]][adjacent[1]] == EMPTY):
                    q.append(adjacent)
                    grid[adjacent[0]][adjacent[1]] = VISITED
                else:  # FILLED
                    max_filled_size = max(max_filled_size, traverse_component(*adjacent))

    return max_filled_size

L = [20, 50, 100, 200, 500, 1000]
p_vals = [round(i*0.01,4) for i in range(0,100)]
# for each L run 100 experiments corresponding to different p_vals
lcc_L = {round(k,2): {v: 0} for k in L for v in p_vals}
for grid_size in L:
    print("gridsize = ", grid_size)
    for p in p_vals:
        lcc_L[grid_size][p] = largest_connected_component(generate_grid(grid_size, p))
        lcc_L[grid_size] = {k:v for k,v in sorted(lcc_L[grid_size].items(), key=lambda t: t[0])}

exp_file = open('percolation_experiment.pickle', 'wb')
pickle.dump(lcc_L, exp_file)
exp_file.close()
