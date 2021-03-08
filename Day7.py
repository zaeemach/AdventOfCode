# --- Day 7: Handy Haversacks ---
import re 
data = open("input.txt", "r").read().splitlines()

# Because there are both 'bag' and 'bags', replacing them with one
# consistent term will help ensure all edge cases are met. The string
# 'no other bag' is also replaced to properly match regex later in 
# the code.
data = [x.replace('bags', 'bag') for x in data]
data = [x.replace('no other bag', 'none') for x in data]

# Create dictionary of the bags
bags = {}
for x in data:
    x = x.split(' contain ')
    bags[x[0]] = x[1]

# Run a loop where all bags containing or eventually containing
# a shiny gold bag are added to check.
check = ['shiny gold bag']
for x in check:
    for y in bags.keys():
        if x in bags[y] and y not in check:
            check.append(y)

# Print the total number of bags in check minus 'shiny gold bag' as
# it should not be included in total count.
print(len(check)-1)

# --- Day 7: Part Two ---
# Print out all bags contained within or eventually contained within
# shiny gold bags.
totals = ['shiny gold bag']
for x in totals:
    if x in bags.keys():
        v = bags[x]
        v = re.findall(r'[a-z]+\s[a-z]+\sbag', v)
        totals.extend(v)

# Remove any duplicates as they are irrelevant.
totals = list(set(totals))


# Initialize a tracker which will help map out the order in which each
# value in totals should be visited. 
tracker = []
for x in totals:
    if 'none' in bags[x]:
        tracker.append(x)
        bags[x] = '0'


# Define a function that takes a key value and finds the total number of
# bags within it. Will, of course, only work if all contained bags already
# have been counted.
def totalBags(x):
    val = 0
    v = bags[x]
    v = v.split(', ')
    for bag in v:
        bag = re.findall(r'\d+|[a-z]+\s[a-z]+\sbag', bag)
        val += int(bag[0]) + int(bag[0]) * int(bags[bag[1]])
        bags[x] = str(val)


# Tracker will contain the correct order in which to visit the keys by 
# going through totals and figuring out which keys have already been 
# visited. Once the key is found, the totalBags function will be invoked
# to calculate the number of bags within the particular keys. This will 
# continue looping until the final shiny gold bag has been found.
while set(tracker) != set(totals):
    for key in totals:
        v = bags[key]
        v = re.findall(r'[a-z]+\s[a-z]+\sbag', v)
        if set(v) <= set(tracker) and key not in tracker:
            tracker.append(key)
            totalBags(key)
print(bags['shiny gold bag'])