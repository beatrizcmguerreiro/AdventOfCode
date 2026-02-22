# day 9 (part 1)

points = []

file = open("2025/day9/input.txt", "r")

# read in the points
for line in file:
  line = line.replace("\n", "")
  point_str = line.split(",")
  point = [int(point_str[0]), int(point_str[1])]
  points.append(point)

# calculate the area of the rectangle formed by each pair of points and keep track of the maximum area
max_area = 0
for index in range(0, len(points) - 1):
  for index2 in range(index + 1, len(points)):
    point, point2 = points[index], points[index2]
    area = (abs(point[0] - point2[0]) + 1) * (abs(point[1] - point2[1]) + 1)
    max_area = max(max_area, area)

print(max_area)
