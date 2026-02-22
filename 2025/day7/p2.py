# day 7 (part 2)

def count_timelines(rows: list[str]):
    
    # beams[col] = number of timelines at that column
    beams = {rows[0].index("S"): 1}

    for row in rows[1:]:
        new = {}

        for col, n in beams.items():
            if 0 <= col < len(row):
                if row[col] == "^":
                    
                    # split left
                    new[col - 1] = new.get(col - 1, 0) + n
                    
                    # split right
                    new[col + 1] = new.get(col + 1, 0) + n
                else:
                    # continue downward
                    new[col] = new.get(col, 0) + n
        
        # update beams
        beams = new

    return sum(beams.values())

with open("2025/day7/input.txt", "r") as f:
    rows = [line.rstrip("\n") for line in f]

print(count_timelines(rows))