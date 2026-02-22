# day 6 (part 1)

worksheet = []

with open("2025/day6/input.txt") as f:
    worksheet = [line.rstrip("\n") for line in f]

# determine width of the grid
width = max(len(row) for row in worksheet)

# normalize all rows to equal width
worksheet = [row.ljust(width) for row in worksheet]

problems = []
current_columns = []

# check if a column is blank to help
def is_blank_col(col):
    return all(row[col] == " " for row in worksheet)

# scan columns left to right
col = 0
while col < width:
    if is_blank_col(col):
        if current_columns:
            problems.append(current_columns)
            current_columns = []
        col += 1
        continue

    # if non-blank column it's part of a problem
    current_columns.append(col)
    col += 1

# append the last problem if needed
if current_columns:
    problems.append(current_columns)

grand_total = 0

# process each problem
for cols in problems:
    numbers = []
    operator = None

    for row in range(4):  # the first 4 rows contain numbers
        value_str = "".join(worksheet[row][c] for c in cols).strip()
        if value_str:
            numbers.append(int(value_str))

    # operator is on the last row
    operator_str = "".join(worksheet[4][c] for c in cols).strip()
    operator = operator_str  # either '+' or '*'

    # compute the result of this problem
    if operator == "+":
        result = sum(numbers)
    else:  # operator == "*"
        result = 1
        for n in numbers:
            result *= n

    grand_total += result

print(grand_total)