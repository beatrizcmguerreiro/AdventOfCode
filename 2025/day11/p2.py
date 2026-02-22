# day 11 (part 2)

from functools import cache
from collections import defaultdict

# part 1
def parse_device(line):
    name, outs = line.strip().split(": ")
    return name, outs.split()

with open("2025/day11/input.txt") as f:
    devices = defaultdict(list, map(parse_device, f))

# part 2
FFT = "fft"
DAC = "dac"

@cache
def dfs(node, state):
    # state is a bitmask of seen devices (FFT=1, DAC=2)
    if node == FFT:
        state |= 1
    if node == DAC:
        state |= 2

    # if we reach the exit, check if we've seen both devices
    if node == "out":
        return 1 if state == 3 else 0  # valid only if seen both

    return sum(dfs(child, state) for child in devices[node])

answer = dfs("svr", 0)
print(answer)
