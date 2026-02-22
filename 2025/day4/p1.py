# day 4 (part 1)

with open("2025/day4/input.txt") as f:
    grid = [list(line.strip()) for line in f]

rows = len(grid)
cols = len(grid[0])

# directions for adjacent cells (8 directions)
D = [(-1,-1), (-1,0), (-1,1),
     (0,-1),          (0,1),
     (1,-1), (1,0), (1,1)]

count_accessible = 0

# count "@" cells that are accessible aka not surrounded by 4 or more @
for r in range(rows):
    for c in range(cols):
        if grid[r][c] != "@":
            continue
        
        # count adjacent @
        adj = 0
        for dr, dc in D:
            rr, cc = r + dr, c + dc
            if 0 <= rr < rows and 0 <= cc < cols:
                if grid[rr][cc] == "@":
                    adj += 1
        
        if adj < 4:
            count_accessible += 1

print(count_accessible)
