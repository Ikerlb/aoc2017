import sys
sys.path.append('../knot-hash')
from knot_hash import knot_hash, reverse, binary
from itertools import product

key = input()

grid = [binary(knot_hash(f"{key}-{i}")) for i in range(128)]

def neighbors(grid, r, c):
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]: 
        nr, nc = r + dr, c + dc
        if not 0 <= nr < len(grid):
            continue
        if not 0 <= nc < len(grid[0]):
            continue
        yield nr, nc

def dfs(grid, r, c):
    for nr, nc in neighbors(grid, r, c):
        if grid[nr][nc] == 1:
            grid[nr][nc] = -1
            dfs(grid, nr, nc)

def part2(grid):
    i = 0
    for r, c in product(range(128), repeat = 2):
        if grid[r][c] == 1:
            dfs(grid, r, c)
            i += 1
    return i

# p1
print(sum(sum(row) for row in grid))

# p2
print(part2(grid))
