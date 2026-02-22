# day 8 (part 1)

import itertools as it, math

# each box is a circuit, and each circuit is a set of boxes
circuits = {b: {b} for b in map(eval, open('2025/day8/input.txt'))}

# sort all pairs of boxes by distance, and merge their circuits if they are different
pairs = sorted(it.combinations(circuits, 2),
               key=lambda x: math.dist(*x))

# for each pair of boxes, find their circuits and merge them if they are different
for i, (box1, box2) in enumerate(pairs):
    for c in circuits:
        if box1 in circuits[c]: cir1 = c
        if box2 in circuits[c]: cir2 = c
    
    if cir1 != cir2:
        circuits[cir1] |= circuits[cir2]
        del circuits[cir2]

    if i+1 == 1000:
        n = sorted(len(circuits[b]) for b in circuits)
        print(n[-3] * n[-2] * n[-1])

    if len(circuits) == 1:
        print(box1[0] * box2[0])
        break