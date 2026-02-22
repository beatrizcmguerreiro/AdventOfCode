# day 5 (part 1)

fresh_ranges = []
ingredient_ids = []

with open("2025/day5/input.txt") as f:
    lines = [line.strip() for line in f]

# determine where the blank line is to separate ranges from ingredient IDs
blank_index = lines.index("")

range_lines = lines[:blank_index]
id_lines = lines[blank_index + 1:]

# parse fresh ingredient ID ranges
for line in range_lines:
    start, end = map(int, line.split("-"))
    fresh_ranges.append((start, end))

# count how many ingredient IDs are fresh
fresh_count = 0
for line in id_lines:
    ingredient_id = int(line)
    for start, end in fresh_ranges:
        if start <= ingredient_id <= end:
            fresh_count += 1
            break

print(fresh_count)