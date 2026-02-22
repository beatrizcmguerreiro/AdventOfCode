# day 2 (part 1)

with open("2025/day2/input.txt", "r") as file:
    line = file.read()
    split_strings = line.split(",") # split the line into individual strings

    ranges = [] # created to separate the first and second ID in each range
    for id in split_strings:
        first_str, last_str = id.split("-") # split each range into first and last ID
        first_id = int(first_str)
        last_id = int(last_str)
        ranges.append([first_id, last_id]) # append the pair of IDs as a list

print(ranges)
def is_invalid(product_id): # check if the ID is repeated twice
    s = str(product_id) #convert ID to string since it's easier to compare "halves"
    length = len(s) # get length of the string because we need to know where to cut it

    if length % 2 != 0: # only IDs with even length can be repeated twice
        return False

    cut = length // 2 # get where to 'cut' the string
    # split the string into two halves
    first_half = s[:cut] 
    second_half = s[cut:]

    return first_half == second_half # return whether the two halves are equal

t_invalid = 0 # total of the invalid IDs
for first_id, last_id in ranges:
    for product_id in range(first_id, last_id + 1): # iterate through each ID in the range
        if is_invalid(product_id):
            t_invalid += product_id # add to the total if invalid

print(t_invalid)