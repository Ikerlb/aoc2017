from heapq import heappush, heappop

blocks = [int(n) for n in input().split()]

# mutates blocks
def step(blocks):
    i = max(range(len(blocks)), key = lambda i: (blocks[i], -i))
    j = (i + 1) % len(blocks)
    redis = blocks[i]
    blocks[i] = 0
    for _ in range(redis):
        blocks[j] += 1
        j = (j + 1) % len(blocks)

def steps(blocks):
    visited = {}
    i = 0
    while (tup := tuple(blocks)) not in visited:
        visited[tup] = i
        step(blocks)
        i += 1
    return i, i - visited[tup]

i, cl = steps(blocks)

# p1
print(i)

# p2
print(cl)
