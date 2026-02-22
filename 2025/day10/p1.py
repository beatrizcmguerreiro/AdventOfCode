# day 10 (part 1)

def parse_line(line):
    # extract [pattern]
    i1 = line.index('[') + 1
    i2 = line.index(']', i1)
    pat = line[i1:i2]

    # goal mask
    goal = 0
    for i, ch in enumerate(pat):
        if ch == "#":
            goal |= (1 << i)

    # extract button groups
    buttons = []
    idx = i2 + 1
    while True:
        # find next group of buttons
        try:
            a = line.index('(', idx) + 1
        except ValueError:
            break
        b = line.index(')', a)
        group = line[a:b]
        idx = b + 1

        # convert group to mask
        if group.strip():
            mask = 0
            for x in group.split(','):
                mask |= (1 << int(x))
            buttons.append(mask)

    return goal, buttons, len(pat)

# find the minimum number of button presses to reach the goal pattern
def min_presses(goal, buttons, n):
    start = 0
    if start == goal:
        return 0
    
    queue = [(start, 0)]
    head = 0
    seen = {start}
    
    while head < len(queue):
        state, dist = queue[head]
        head += 1

        # try pressing each button
        for b in buttons:
            nxt = state ^ b
            if nxt == goal:
                return dist + 1
            if nxt not in seen:
                seen.add(nxt)
                queue.append((nxt, dist + 1))

    return None

# solve the problem for all lines in the input file and sum the results
def solve(path):
    total = 0
    for line in open(path):
        line = line.strip()
        if not line:
            continue
        goal, buttons, n = parse_line(line)
        total += min_presses(goal, buttons, n)
    return total

print(solve("2025/day10/input.txt"))
