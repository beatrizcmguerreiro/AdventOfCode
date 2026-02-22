# day 11 (part 1)

from functools import cache
from collections import defaultdict

# load and parse input
def parse_device(line):
    name, outs = line.strip().split(": ")
    return name, outs.split()

with open("2025/day11/input.txt") as f:
    devices = defaultdict(list, map(parse_device, f))

# count all paths from source to destiny
@cache
def paths(src, dst):
    if src == dst:
        return 1
    return sum(paths(child, dst) for child in devices[src])

print(paths("you", "out"))
