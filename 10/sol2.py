N = 256 

def build(n):
    return list(range(n))

def reverse(arr, s, l):
    for i in range((l // 2) + 1):
        si = (s + i) % len(arr)
        ei = (s + l - i) % len(arr)
        #print(si, ei)
        arr[si], arr[ei] = arr[ei], arr[si]

def format(arr, i):
    return " ".join(str(n) if j!=i else f"[{n}]" for j, n in enumerate(arr))

def part1(arr, lengths):
    ss = cur = 0
    for l in lengths:
        reverse(arr, cur, l - 1)
        cur = (cur + l + ss) % len(arr)
        ss += 1
    return arr[0] * arr[1]
        
def chunks(arr, size):
    for i in range(0, len(arr), size):
        yield arr[i:i + size]

def xor(l):
    res = 0
    for n in l:
        res ^= n
    return res

def part2(arr, lengths):
    lengths.extend([17, 31, 73, 47, 23])
    ss = cur = 0
    for _ in range(64):
        for l in lengths:
            reverse(arr, cur, l - 1)
            cur = (cur + l + ss) % len(arr)
            ss += 1
    sparse = [xor(chunk) for chunk in chunks(arr, 16)]
    return "".join(f"{n:02x}" for n in sparse)

txt = input()
arr = build(N)

# p1
# print(part1(arr, [int(n) for n in txt.split(",")]))

# p2
print(part2(arr, [ord(c) for c in txt]))
