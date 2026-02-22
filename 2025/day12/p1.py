# day 12 (part 1)

class Day12:
    def __init__(self):
        with open("2025/day12/input.txt") as f:
            self.data = [line.rstrip('\n') for line in f]
        # parse regions and sizes
        self.regions = [[x for x in line.split(' ')] for line in self.data if len(line) > 6]
        self.sizes = {}
        self.fill_sizes()

    # part 1
    def part_one(self):
        total = 0
        for region in self.regions:
            size = int(region[0][:2]) * int(region[0][3:5])
            presents = 0
            for i in range(1, len(region)):
                presents += int(region[i]) * self.sizes[i - 1]
            if size >= presents:
                total += 1
        return total
    
    def part_two(self):
        return "Merry Christmas"

    # helper to fill self.sizes with the number of '#' in each region
    def fill_sizes(self):
        num, count = 0, 0
        for line in self.data:
            if line == "":
                self.sizes[num] = count
                count = 0
            elif line[-1] == ':':
                num = int(line[0])
            elif '#' in line or '.' in line:
                for x in line:
                    if x == '#':
                        count += 1
            else:
                return

    def print_solution(self):
        print("Day 12:")
        print(f"Part 1: {self.part_one()}")
        print(f"Part 2: {self.part_two()}")