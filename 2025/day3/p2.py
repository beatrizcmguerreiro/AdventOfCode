# day 3 (part 2)

def max_joltage(bank: list[int], digits: int) -> int:
    if digits == 1: # base case: selecting 1 digit then return max
        return max(bank)

    if len(bank) == digits: # if exactly 'digits' digits, must takem all
        value = 0
        for d in bank:
            value = value * 10 + d
        return value

    limit = len(bank) - (digits - 1) # choose best first digit from a prefix, leaving enough digits afterward
    prefix = bank[:limit]

    first = max(prefix)
    idx = prefix.index(first)

    rest = max_joltage(bank[idx + 1:], digits - 1) # recursive (for remaining digits)

    return first * (10 ** (digits - 1)) + rest

total = 0

with open("2025/day3/input.txt", "r") as f:
    for line in f:
        digits = [int(c) for c in line.strip()]
        total += max_joltage(digits, 12)   

print(total)