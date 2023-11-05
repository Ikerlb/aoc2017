from sys import stdin

grid = [[int(n) for n in line[:-1].split()] for line in stdin]

def part1(grid):
    return sum(abs(min(row) - max(row)) for row in grid)

def div_or_mult(a, b):
    return a % b == 0 or b % a == 0

def find_div_or_mult(row):
    n = len(row)
    for i in range(n):
        for j in range(i + 1, n):
            if div_or_mult(row[i], row[j]):
                return max(row[i] // row[j], row[j] // row[i])

def part2(grid):
    return sum(find_div_or_mult(row) for row in grid) 

print(part1(grid))
print(part2(grid))

