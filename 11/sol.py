from collections import deque

# this is a fantastic resource to make sense of it all!
# https://www.redblobgames.com/grids/hexagons/#distances
# use odd q vertical layout
def neighbors(r, c):
    yield r + (c % 2) - 1, c + 1    # ne
    yield r - 1, c                  # n
    yield r + (c % 2) - 1, c - 1    # nw
    yield r + (c % 2), c + 1        # se
    yield r + 1, c                  # s
    yield r + (c % 2), c - 1        # sw

def step(r, c, instruction):
    match instruction:
        case "ne":
            dr, dc = (c % 2) - 1, 1
        case "n":
            dr, dc = -1, 0
        case "nw":
            dr, dc = (c % 2) - 1, -1
        case "se":
            dr, dc = (c % 2), 1
        case "s":
            dr, dc = 1, 0
        case "sw":
            dr, dc = (c % 2), -1
    return r + dr, c + dc

#def distance(sr, sc, tr, tc):
#    q = deque([(sr, sc)])
#    steps = 0
#    used = {(sr, sc)}
#    while q:
#        for i in range(len(q)):
#            r, c = q.popleft()
#            if (r, c) == (tr, tc):
#                return steps
#            for nr, nc in neighbors(r, c):
#                if (nr, nc) not in used:
#                    used.add((nr, nc))
#                    q.append((nr, nc))
#        steps += 1
#    return -1

def oddq_to_axial(row, col):
    q = col
    r = row - (col - (col&1)) // 2
    return q, r

def axial_subtract(ar, ac, br, bc):
    return ar - br, ac - bc

def axial_distance(ar, ac, br, bc):
    vecr, vecc = axial_subtract(ar, ac, br, bc)
    return (abs(vecr) + abs(vecr + vecc) + abs(vecc)) // 2

def distance(sr, sc, tr, tc):
    ar, ac = oddq_to_axial(sr, sc)
    br, bc = oddq_to_axial(tr, tc)
    return axial_distance(ar, ac, br, bc)

def steps(r, c, instructions):
    mdist = 0
    for instruction in instructions:
        mdist = max(mdist, distance(0, 0, r, c))
        r, c = step(r, c, instruction)
    return r, c, mdist

instructions = input().split(",")
tr, tc, mdist = steps(0, 0, instructions)

# p1
print(distance(0, 0, tr, tc))

# p2
print(mdist)
