import fileinput

l = [chr(i + ord('a')) for i in range(16)]

def step(l, s):
    match s[0]:
        case "s":
            n = int(s[1:])
            l[:] = l[-n:] + l[:-n]
        case "x":
            a, b = map(int, s[1:].split("/"))
            l[a], l[b] = l[b], l[a]
        case "p":
            a, b = map(lambda x: l.index(x), s[1:].split("/"))
            l[a], l[b] = l[b], l[a]

def steps(l, instructions):
    for instr in instructions:
        step(l, instr)
    return "".join(l)

def part1(l, instructions):
    return steps(l, instructions)

def part2(start, instructions):
    l = start[:]
    s = {}
    i = 0
    while True:
        res = steps(l, instructions)
        if res in s:
            break
        s[res] = i
        i += 1

    # cycles of i - s[res]
    k = 1000000000
    l = start[:]

    for _ in range(s[res]):
        steps(l, instructions)
        k -= 1

    # k steps remaining
    k = k % (i - s[res])
    for _ in range(k):
       steps(l, instructions)
    return "".join(l)
    
instructions = next(fileinput.input(encoding="utf-8")).split(",")

# p1
print(part1(l[:], instructions))

# p2
print(part2(l[:], instructions))
