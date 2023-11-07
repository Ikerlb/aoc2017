from sys import stdin
from collections import Counter

lines = [line[:-1] for line in stdin]

def part1(lines):
    s = 0
    for line in lines:
        split = line.split(" ")
        if len(set(split)) == len(split):
            s += 1
    return s

def part2(lines):
    s = 0
    for line in lines:
        split = line.split(" ")
        c = Counter("".join(sorted(w)) for w in split)
        if len(c) == len(split):
            s += 1
    return s

print(part1(lines))
print(part2(lines))
