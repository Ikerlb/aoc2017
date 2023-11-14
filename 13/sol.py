import re
from sys import stdin

def parse(line):
    regex = r'(\d+): (\d+)\n'
    rng, depth = re.match(regex, line).groups()
    return int(rng), int(depth)

def build(lines):
    d = {rng: depth for rng, depth in lines}
    return d

def severity(d, delay):
    l = [k * v for k, v in d.items() if ((k+delay) % (v + v - 2)) == 0]
    return l

def part1(d):
    l = severity(d, 0)
    return sum(l)

def part2(d):
    i = 0
    while len(l := severity(d, i)) != 0:
        #print(s)
        i += 1
    return i

lines = [parse(line) for line in stdin]

d = build(lines)
#print(d)

# p1
print(part1(d))

# p2
print(part2(d))
