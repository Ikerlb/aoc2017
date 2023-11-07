NORMAL  = 0
GARBAGE = 1

def parse(s):
    res = [[]]
    mode = NORMAL
    garbage = 0
    i = 0
    while i < len(s):
        c = s[i]
        if mode == NORMAL and c == "{":
            res.append([])
            i += 1
        elif mode == NORMAL and c == "}":
            l = res.pop()
            res[-1].append(l)
            i += 1
        elif mode == NORMAL and c == "<":
            mode = GARBAGE
            i += 1
        elif mode == GARBAGE and c == "!":
            i += 2
        elif mode == GARBAGE and c == ">":
            i += 1
            mode = NORMAL
        elif mode == GARBAGE:
            garbage += 1
            i += 1
        else:
            i += 1
    res = res.pop()
    return res.pop() if res else None, garbage

def score(node, depth):
    s = depth
    for nn in node:
        r = score(nn, depth + 1)
        s += r
    return s
    
line = input()

parsed, garbage = parse(line)
if parsed is not None:
    print(score(parsed, 1))
print(garbage)
