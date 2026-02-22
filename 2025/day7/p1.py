# day 7 (part 1)

def count_splits(rows: list[str]) -> int:
    # find starting column of S
    start_col = rows[0].index("S")

    # active beam positions (columns)
    beams = {start_col}

    total_splits = 0

    # process each row below S
    for row in rows[1:]:
        new_beams = set()

        for col in beams:
            # ignore beams that fall outside row width
            if col >= len(row):
                continue

            # if beam hits a splitter
            if row[col] == "^":
                total_splits += 1
                new_beams.add(col - 1)  # left beam
                new_beams.add(col + 1)  # right beam
            else:
                # beam continues straight down
                new_beams.add(col)

        beams = new_beams

    return total_splits

with open("2025/day7/input.txt", "r") as f:
    rows = [line.rstrip("\n") for line in f]

print(count_splits(rows))