# day 8 (part 2)

import itertools as it, math

# each box is a circuit, and each circuit is a set of boxes
circuits = {b: {b} for b in map(eval, open("2025/day8/input.txt"))}

# sort all pairs of boxes by distance, and merge their circuits if they are different
pairs = sorted(it.combinations(circuits, 2),
               key=lambda x: math.dist(*x))

last_merge = None

# for each pair of boxes, find their circuits and merge them if they are different
for i, (box1, box2) in enumerate(pairs):

    # find circuits for box1 and box2
    for c in circuits:
        if box1 in circuits[c]: cir1 = c
        if box2 in circuits[c]: cir2 = c

    # merge only if different
    if cir1 != cir2:
        circuits[cir1] |= circuits[cir2]
        del circuits[cir2]
        last_merge = (box1, box2)

      
        if i + 1 == 1000:
            sizes = sorted(len(circuits[b]) for b in circuits)
            print("Part 1:", sizes[-1] * sizes[-2] * sizes[-3])


    if len(circuits) == 1:
        a, b = last_merge
        print("Part 2:", a[0] * b[0])
        break
