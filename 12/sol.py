import re
from sys import stdin
from collections import defaultdict

class UFS:
    def __init__(self, n):
        self.n = n
        self.parents = list(range(n))

    def _root(self, a):
        if self.parents[a] == a:
            return a
        ra = self._root(self.parents[a])
        self.parents[a] = ra
        return ra

    def union(self, a, b):
        ra = self._root(a)
        rb = self._root(b)

        if ra == rb:
            return False

        self.parents[ra] = rb
        return True

    def size(self, a):
        ra = self._root(a)
        return sum(1 for i in range(self.n) if self._root(i) == ra)

    def groups(self):
        d = defaultdict(int)
        for i in range(self.n):
            d[self._root(i)] += 1
        return d

def parse(s):
    regex = r'(\d+) <-> (.+)\n'
    fst, snd = re.match(regex, s).groups()
    return int(fst), [int(sn) for sn in snd.split(", ")]

def part1(ufs):
    return ufs.size(0)

def part2(ufs):
    groups = ufs.groups()
    return len(groups)

def build_ufs(groups):
    n = max(i for i, _ in groups) + 1
    ufs = UFS(n)
    for i, l in groups:
        for j in l:
            ufs.union(i, j)
    return ufs

groups = [parse(line) for line in stdin]
ufs = build_ufs(groups)

# p1
print(part1(ufs))

# p2
print(part2(ufs))
