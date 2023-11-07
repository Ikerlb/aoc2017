from sys import stdin
import re
from itertools import groupby
from collections import Counter

def parse(line):
    regex = r'(.+) \((\d+)\)( -> .+)?'
    res = re.match(regex, line)
    name = res.group(1)
    size = int(res.group(2))
    children = res.group(3)
    ch = children[4:].split(", ") if children else []
    return name, size, ch

programs = [parse(line[:-1]) for line in stdin]

def parent(programs):
    parents = {}
    for name, size, children in programs:
        for ch in children:
            parents[ch] = name

    name = programs[0][0]
    while name in parents:
        name = parents[name]
    return name

def dfs(g, node):
    size, children = g[node]
    total = size
    odd = off = None
    sizes = {}
    for nn in children:
        s, sodd, soff = dfs(g, nn)
        sizes[nn] = s
        if sodd is not None:
            odd = sodd
            off = soff
        total += s

    if odd is not None or not sizes:
        return total, odd, off

    c, _ = Counter(sizes.values()).most_common(1).pop()
    odds = [nn for nn in sizes if sizes[nn] != c]
    if odds:
        odd = odds.pop()
        off = c - sizes[odd]
    return total, odd, off

def part2(programs, parent):
    d = {name: (size, children) for name, size, children in programs}
    total, odd, off = dfs(d, parent)
    return d[odd][0] + off

# p1
p = parent(programs)
print(p)

#p2
print(part2(programs, p))
