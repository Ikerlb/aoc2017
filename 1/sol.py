from sys import stdin

def match(arr, i, k = 1):
    n = len(arr)
    return arr[i] == arr[(i + k) % n]

line = input()

arr = [int(ch) for ch in line]


# p1
print(sum(arr[i] for i in range(len(arr)) if match(arr, i)))

# p2
half = len(arr) // 2
print(sum(arr[i] for i in range(len(arr)) if match(arr, i, half)))
