from sys import stdin

instructions = [int(line[:-1]) for line in stdin]

def part1(instructions):
    steps = i = 0
    while 0 <= i < len(instructions):
        jump = instructions[i]
        instructions[i] += 1
        i += jump
        steps += 1
    return steps


def part2(instructions):
    steps = i = 0
    while 0 <= i < len(instructions):
        jump = instructions[i]
        inc = -1 if jump >= 3 else 1
        instructions[i] += inc
        i += jump
        steps += 1
    return steps

# p1
print(part1(instructions[:]))

# p2
print(part2(instructions[:]))
