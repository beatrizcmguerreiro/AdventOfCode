# day 10 (part 2)

import numpy as np
from scipy.optimize import linprog
from collections import deque

with open("2025/day10/input.txt") as f:
    ls = f.read().strip().split("\n")

# part 1
def solve1(l):
    goal, *buttons, _ = l.split(" ")
    goal = set(i for i, x in enumerate(goal[1:-1]) if x == "#")

    moves = []
    for b in buttons:
        b = b[1:-1]
        b = {int(x) for x in b.split(",")}
        moves.append(b)

    # need to find the minimum number of moves to get from the empty set to the goal set, 
    # where each move is a symmetric difference with one of the moves
    q = deque()
    q.append((set(), 0))
    seen = set()
    while q:
        curr, steps = q.popleft()
        if curr == goal:
            return steps
        for m in moves:
            newset = curr ^ m
            if newset in seen:
                continue
            
            # add the new set to the queue
            seen.add(frozenset(newset))
            q.append((newset, steps + 1))

print(sum(solve1(l) for l in ls))


# part 2
def solve2(l):
    _, *buttons, counters = l.split(" ")

    # the goal is to find the minimum number of moves to get from the empty set to the goal set,
    # where each move is a symmetric difference with one of the moves, and we can use
    # each move any number of times, but we want to minimize the total number of moves used
    goal = tuple(map(int, counters[1:-1].split(",")))
    moves = []
    for b in buttons:
        b = b[1:-1]
        b = {int(x) for x in b.split(",")}
        moves.append(b)

    # represent the problem as a linear program, where we want to minimize the total number of moves used,
    # subject to the constraint that the final set is equal to the goal set, 
    # and each move can be used any number of times
    c = [1 for _ in moves]
    A_eq = []
    b_eq = []
    for i in range(len(goal)):
        A_eq.append([1 if i in move else 0 for move in moves])
        b_eq.append(goal[i])
    A_eq = np.array(A_eq)
    b_eq = np.array(b_eq)
    res = linprog(
        c, A_eq=A_eq, b_eq=b_eq, bounds=(0, None), method="highs", integrality=True
    )
    # print(res)
    return res.fun

# the answer is not an integer, so we need to round it up to the nearest integer
print(sum(solve2(l) for l in ls))