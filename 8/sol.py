from sys import stdin
from collections import defaultdict
import re

def parse(line):
    regex = r'([a-zA-Z]+) (inc|dec) (-?\d+) if (.+)'
    var, binop, val, cond = re.match(regex, line).groups()
    if binop == "inc": 
        op = lambda x: x + int(val)
    else:
        op = lambda x: x - int(val)
    return (var, op, cond)
    

instructions = [parse(line[:-1]) for line in stdin]

# we'll take advantage of eval's param
def execute(instructions):
    context = defaultdict(int)
    mx = 0
    for var, op, cond in instructions:
        if eval(cond, None, context):
            context[var] = op(context[var]) 
            mx = max(mx, context[var])
    return context, mx

context, mx = execute(instructions)
# p1
print(max(context.values()))

# p2
print(mx)
