from itertools import product

index = int(input()) 

def spiral_coord(index):
    i = 0
    step = 1
    dr, dc = 0, 1
    r = c = 0

    while index:
        s = min(index, step)
        rs, cs = dr * s, dc * s
        r, c = r + rs, c + cs
        index -= s
        dr, dc = -dc, dr

        if i & 1 == 1:
            step += 1
        i += 1
    return r, c

def part1(index):
    r, c = spiral_coord(index - 1)
    return abs(r) + abs(c)

def neighbors(grid, r, c):
    g = product([0, -1, 1], repeat = 2)

    # burn 
    next(g)

    for dr, dc in g:
        if (tup := (r + dr, c + dc)) in grid:
            yield tup

def simulate():
    r = c = 0
    weight = 1
    grid = {(r, c): weight}
    yield r, c, weight
    step = 1
    sinc = 0
    dr, dc = 0, 1
    ur, uc = r + (dr * step), c + (dc * step)
    while True:
        r, c = r + dr, c + dc
        weight = sum(grid[tup] for tup in neighbors(grid, r, c))
        yield r, c, weight
        grid[(r, c)] = weight
        if r == ur and c == uc:
            step += sinc
            sinc = 1 - sinc
            dr, dc = -dc, dr
            ur, uc = r + (dr * step), c + (dc * step)

def part2(index):
    g = simulate()
    while (res := next(g)[2]) <= index:
        pass
    return res

# p1
print(part1(index))

# p2
print(part2(index))
