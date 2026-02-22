# day 5 (part 2)

fresh_ranges = []

with open("2025/day5/input.txt") as f:
    lines = [line.strip() for line in f]

# parse only the fresh ID ranges, the ones before the blank line
blank_index = lines.index("")
range_lines = lines[:blank_index]

for line in range_lines:
    fresh_ranges.append(list(map(int, line.split("-"))))

# sort by start value
fresh_ranges.sort()

# start with the first range
merged_start, merged_end = fresh_ranges[0]
total_fresh_ids = merged_end - merged_start + 1

# sweep through remaining ranges
for i in range(1, len(fresh_ranges)):
    start, end = fresh_ranges[i]

    # if the new range is entirely inside the merged interval, skip it
    if end <= merged_end:
        continue

    # if overlapping, then adjust start to the next uncovered ID
    if start <= merged_end:
        start = merged_end + 1

    # count newly uncovered section
    total_fresh_ids += end - start + 1

    # expand merged interval
    merged_end = end

print(total_fresh_ids)
