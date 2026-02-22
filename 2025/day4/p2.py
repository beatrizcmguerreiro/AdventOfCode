# day 4 (part 2)

with open("2025/day4/input.txt") as f:
    grid = [list(line.strip()) for line in f]

rows = len(grid)
cols = len(grid[0])

# direções para verificar os adjacentes (8 direções)
dirs = [(-1,-1),(-1,0),(-1,1),
        (0,-1),       (0,1),
        (1,-1),(1,0),(1,1)]

# conta quantos adjacentes existem para a posição (r, c)
def count_adj(r, c):
    cnt = 0
    for dr, dc in dirs:
        rr, cc = r+dr, c+dc
        if 0 <= rr < rows and 0 <= cc < cols and grid[rr][cc] == "@":
            cnt += 1
    return cnt

removed = 0

while True:
    to_remove = []

    # encontra todos os rolos removíveis nesta iteração
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "@":
                continue

            adj = count_adj(r, c)
            if adj < 4:
                to_remove.append((r, c))

    # se não há mais, termina
    if not to_remove:
        break

    # remove todos ao mesmo tempo
    for r, c in to_remove:
        grid[r][c] = "."

    removed += len(to_remove)

print("Part 2:", removed)