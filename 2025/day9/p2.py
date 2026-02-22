# day 9 (part 2)

# read points
points = []
with open("2025/day9/input.txt") as f:
    for line in f:
        x, y = map(int, line.strip().split(","))
        points.append((x, y))

# determine grid bounds
xs = [p[0] for p in points]
ys = [p[1] for p in points]
max_x = max(xs) + 2
max_y = max(ys) + 2

# grid: 0 = empty, 1 = red, 2 = green
grid = [[0] * (max_y + 1) for _ in range(max_x + 1)]

# mark red tiles
for x, y in points:
    grid[x][y] = 1

# draw a straight green line between red points a to b
def draw_line(a, b):
    (x1, y1), (x2, y2) = a, b
    if x1 == x2:
        step = 1 if y2 > y1 else -1
        for y in range(y1, y2 + step, step):
            if grid[x1][y] == 0:
                grid[x1][y] = 2
    else:
        step = 1 if x2 > x1 else -1
        for x in range(x1, x2 + step, step):
            if grid[x][y1] == 0:
                grid[x][y1] = 2

# connect each red to next red (loop)
for i in range(len(points)):
    a = points[i]
    b = points[(i + 1) % len(points)]
    draw_line(a, b)

# flood-fill from outside using a simple list queue (no collections)
visited = [[False] * (max_y + 1) for _ in range(max_x + 1)]

queue = [(0, 0)]
visited[0][0] = True

# directions for flood-fill
dirs = [(1,0), (-1,0), (0,1), (0,-1)]

while queue:
    # pop from front of queue
    x, y = queue.pop(0)

    for dx, dy in dirs:
        nx = x + dx
        ny = y + dy

        # only visit valid, unvisited, empty tiles
        if 0 <= nx <= max_x and 0 <= ny <= max_y:
            if not visited[nx][ny] and grid[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append((nx, ny))

# mark all unvisited empty tiles as green (2)
for x in range(max_x + 1):
    for y in range(max_y + 1):
        if grid[x][y] == 0 and not visited[x][y]:
            grid[x][y] = 2

# build prefix sum of invalid tiles (cells where grid == 0)
prefix = [[0] * (max_y + 2) for _ in range(max_x + 2)]

for i in range(1, max_x + 2):
    for j in range(1, max_y + 2):
        prefix[i][j] = (prefix[i-1][j]
                        + prefix[i][j-1]
                        - prefix[i-1][j-1]
                        + (1 if grid[i-1][j-1] == 0 else 0))

# check if rectangle from (x1, y1) to (x2, y2) contains any invalid tiles
def rect_invalid(x1, y1, x2, y2):
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)
    return (prefix[x2+1][y2+1]
            - prefix[x1][y2+1]
            - prefix[x2+1][y1]
            + prefix[x1][y1])

max_area = 0

# test all red pairs
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        x1, y1 = points[i]
        x2, y2 = points[j]

        # must contain only green or red
        if rect_invalid(x1, y1, x2, y2) == 0:
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            max_area = max(max_area, area)

print(max_area)
