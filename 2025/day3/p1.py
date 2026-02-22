# day 3 (part 1)

with open("2025/day3/input.txt", "r") as f:
    for line in f:
        line = line.strip()

def max_voltage(bank: list[int], number_digits: int) -> int:
    if number_digits == 1: # base case: if selecting 1 digit, return max
        return max(bank)

    if len(bank) == number_digits: # if exactly 'digits' digits, must take all
        value = 0
        for d in bank:
            value = value * 10 + d
        return value

    # choose best first digit from a prefix, leaving enough digits afterward
    limit = len(bank) - (number_digits - 1)
    prefix = bank[:limit]

    first = max(prefix)
    pindex = prefix.index(first)

    # recursive method for remaining digits
    rest = max_voltage(bank[pindex + 1:], number_digits - 1)

    return first * (10 ** (number_digits - 1)) + rest # combine first digit with rest

total = 0

digits = [int(c) for c in line]
total += max_voltage(number_digits, 2)

print(total)