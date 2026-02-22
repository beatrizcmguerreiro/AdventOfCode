# day 9 (part 3)

points = []

with open("2025/day9/input.txt", "r") as file:
    for line in file:
        x, y = map(int, line.strip().split(","))
        points.append([x, y])

# build sorted unique coordinate lists
x_coords = []
y_coords = []

# add padding space around the grid to avoid edge cases during flood fill
for x, y in points:
    if x not in x_coords:
        x_coords.append(x)
    if y not in y_coords:
        y_coords.append(y)

x_coords = sorted(x_coords)
y_coords = sorted(y_coords)

# compressed grid coordinates (leave padding space)
x_indices = {}
y_indices = {}

for i, x in enumerate(x_coords):
    x_indices[x] = 2 * i + 2
for i, y in enumerate(y_coords):
    y_indices[y] = 2 * i + 2

# grid with padding
grid_size_x = 2 * len(x_coords) + 8
grid_size_y = 2 * len(y_coords) + 8

grid = [["?"] * grid_size_y for _ in range(grid_size_x)]

# draw straight line between adjacent red points
def fill_line(p1, p2):
    min_x, max_x = min(p1[0], p2[0]), max(p1[0], p2[0])
    min_y, max_y = min(p1[1], p2[1]), max(p1[1], p2[1])

    for xi in range(x_indices[min_x], x_indices[max_x] + 1):
        for yi in range(y_indices[min_y], y_indices[max_y] + 1):
            grid[xi][yi] = "#"

# connect points in input order
for i in range(len(points) - 1):
    fill_line(points[i], points[i + 1])
fill_line(points[-1], points[0])

# flood fill the outside starting at top-left corner
grid[0][0] = "."
outside_points = [[0, 0]]

def flood_neighbors(px, py):
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            x = px + dx
            y = py + dy
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                if grid[x][y] == "?":
                    grid[x][y] = "."
                    outside_points.append([x, y])

while outside_points:
    px, py = outside_points.pop(0)
    flood_neighbors(px, py)

# check whether rectangle is fully inside the region (# or interior)
def is_filled(p1, p2):
    min_x, max_x = min(p1[0], p2[0]), max(p1[0], p2[0])
    min_y, max_y = min(p1[1], p2[1]), max(p1[1], p2[1])

    for xi in range(x_indices[min_x], x_indices[max_x] + 1):
        for yi in range(y_indices[min_y], y_indices[max_y] + 1):
            if grid[xi][yi] == ".":
                return False
    return True

# search all red pairs for maximum valid rectangle
max_area = 0

for i in range(len(points) - 1):
    for j in range(i + 1, len(points)):
        p1, p2 = points[i], points[j]
        if is_filled(p1, p2):
            area = (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)
            if area > max_area:
                max_area = area

print(max_area)
