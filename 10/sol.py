lengths = [int(n) for n in input().split(",")]

N = 5

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

    
    # insert after
    def insert_after(self, other):
        last = other
        while last.next:
            last = last.next

        nxt = self.next
        self.next = other
        other.prev = self
        last.next = nxt
        if nxt:
            nxt.prev = last

    def __repr__(self):
        node = self
        s = set()
        res = []
        while node and node.val not in s:
            res.append(str(node.val))
            s.add(node.val)
            node = node.next
        return "->".join(res) + "|"

    # 3->2->1->0->3
    # removes from self to n
    def trim(self, n):
        node = self
        for _ in range(n - 1):
            node = node.next
        prv = self.prev
        node.next.prev = self.prev
        self.prev.next = node.next
        nxt = node.next
        node.next = self.prev = None
        return prv, nxt

    def __iter__(self):
        s = set()
        node = self
        while node and node not in s:
            yield node
            s.add(node)
            node = node.next

    def reverse(self):
        l = list(self)
        for node in l:
            node.next, node.prev = node.prev, node.next
        return node

    def advance(self, n):
        node = self
        for _ in range(n):
            node = node.next
        return node

    def __repr__(self):
        res = []
        for node in self:
            prv = node.prev.val if node.prev else "_"
            res.append(f"{node.val}({prv})")
        return "->".join(res) + "|"

def build(n):
    d = [Node(0)]
    for i in range(1, n):
        node = Node(i)
        d[i - 1].insert_after(node)
        d.append(node)
    d[-1].next = d[0]
    d[0].prev = d[-1]
    return d

def part1(nodes, lengths):
    ss = 0
    node = nodes[0]
    for i, l in enumerate(lengths):
        if l == N:
            node = node.reverse()
        else:
            prv, nxt = node.trim(l)
            node = node.reverse()
            prv.insert_after(node)
        node = node.advance((l + ss) % N)
        ss += 1
    print(node)
    return node.val * node.next.val
    

nodes = build(N)
print(part1(nodes, lengths))
