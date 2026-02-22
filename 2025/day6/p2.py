# day 6 (part 2)

worksheet = []

with open("2025/day6/input.txt") as f:
    worksheet = [line.rstrip("\n") for line in f]

# normalize row widths
width = max(len(row) for row in worksheet)
worksheet = [row.ljust(width) for row in worksheet]

problems = []
current_columns = []

# column of all spaces is a separator between problems
def is_blank_col(col):
    return all(row[col] == " " for row in worksheet)

# identify problem column groups
col = 0
while col < width:
    if is_blank_col(col):
        if current_columns:
            problems.append(current_columns)
            current_columns = []
        col += 1
        continue

    current_columns.append(col)
    col += 1

if current_columns:
    problems.append(current_columns)

grand_total = 0

# process each problem according to cephalopod rules
for cols in problems:
    numbers = []

    # find the operator in the bottom row (first non-space)
    for c in cols:
        if worksheet[4][c] != " ":
            operator = worksheet[4][c]
            break

    # each column = one number, top to bottom
    for c in cols:
        digits = "".join(worksheet[row][c] for row in range(4)).strip()
        if digits:
            numbers.append(int(digits))

    # cephalopod math is right-to-left
    numbers = numbers[::-1]

    # compute result
    if operator == "+":
        result = sum(numbers)
    else:  # operator == "*"
        result = 1
        for n in numbers:
            result *= n
    
    # add to grand total
    grand_total += result

print(grand_total)
