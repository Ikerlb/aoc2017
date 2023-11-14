
def reverse(arr, s, l):
    for i in range((l // 2) + 1):
        si = (s + i) % len(arr)
        ei = (s + l - i) % len(arr)
        #print(si, ei)
        arr[si], arr[ei] = arr[ei], arr[si]

def chunks(arr, size):
    for i in range(0, len(arr), size):
        yield arr[i:i + size]

def xor(l):
    res = 0
    for n in l:
        res ^= n
    return res

def knot_hash(txt):
    lengths = [ord(c) for c in txt] + [17, 31, 73, 47, 23]
    arr = list(range(256))
    
    ss = cur = 0
    for _ in range(64):
        for l in lengths:
            reverse(arr, cur, l - 1)
            cur = (cur + l + ss) % len(arr)
            ss += 1
    sparse = [xor(chunk) for chunk in chunks(arr, 16)]
    return hexadecimal(sparse)

def binary(h):
    res = []
    for n in h:
        num = int(n, base = 16)
        bnum = [(num >> i) & 1 for i in range(4)]
        bnum.reverse()
        res.extend(bnum)
    return res
    
def hexadecimal(h):
    return "".join(f"{n:02x}" for n in h)

if __name__ == "__main__":
    txt = input()
    print(knot_hash([ord(c) for c in txt]))
