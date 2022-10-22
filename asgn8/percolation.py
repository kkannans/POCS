# https://codereview.stackexchange.com/questions/210641/size-of-the-largest-connected-component-in-a-grid-in-python
# https://leetcode.com/problems/max-area-of-island/solution/
import numpy as np
import random
import pickle
from pprint import pprint

def maxAreaOfIsland(grid):
    seen = set()
    ans = 0
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
                ans = max(ans, shape)
    return ans

def largest_connected_component(grid):
    """Find largest connected component of 1s on a grid."""

    def traverse_component(pos):
        """Returns no. of unseen elements connected to (i,j)."""
        i, j = pos
        result = 1

        # Check all four neighbours
        for new_pos in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if new_pos in elements:
                elements.remove(new_pos)
                result += traverse_component(new_pos)
        return result

    # Tracks size of largest connected component found
    elements = set((i, j) for i, line in enumerate(grid) for j, cell in enumerate(line) if cell)
    largest = 0
    while elements:
        pos = elements.pop()
        largest = max(largest, traverse_component(pos))
    return largest

def generate_grid(grid_size:int, prob:float):
    lattice_rand = np.random.rand(grid_size,grid_size)
    lattice = (lattice_rand < prob).astype(int)
    return lattice

if __name__ == "__main__":
    # test
    # grid = generate_grid(10, 0.1)
    # pprint(grid)
    # lcc = maxAreaOfIsland(grid)
    # print(lcc)
    L = [20, 50, 100, 200, 500, 1000]
    p_vals = [round(i*0.01,4) for i in range(0,100)]
    num_experiments = 100
    # for each L run 100 experiments corresponding to p in p_vals
    for grid_size in L:
        print("Running 100 experiments for gridsize = ", grid_size)
        lcc_L = { k:[] for k in p_vals}
        for p in p_vals:
            # perform 100 experiments and compute the fractional component size ~ lcc/grid_size^2
            for _ in range(num_experiments):
                lcc = maxAreaOfIsland(generate_grid(grid_size, p))
                fractional_size = lcc/(grid_size*grid_size)
                lcc_L[p].append(fractional_size)
            lcc_L = {k:v for k,v in sorted(lcc_L.items(), key=lambda t: t[0])}
            exp_file = open('percolation_experiment_' + str(grid_size)+'.pickle', 'wb')
            pickle.dump(lcc_L, exp_file)
            exp_file.close()
