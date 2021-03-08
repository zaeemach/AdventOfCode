# --- Day 16: Ticket Translation ---
import re
data = open("input.txt", "r").read().split('\n\n')

ranges = data[0].split()
ranges = [x for x in ranges if re.search(r'\d', x)] 
ranges = [x.split('-') for x in ranges]
for i in range(len(ranges)):
    ranges[i][0] = int(ranges[i][0])
    ranges[i][1] = int(ranges[i][1])
ranges = [tuple(x) for x in ranges]

others = data[2].split()
others = [x for x in others if re.search(r'\d', x)] 
others = [x.split(',') for x in others]
for x in others:
    for i in range(len(x)):
        x[i] = int(x[i])

error = 0
for x in others:
    for i in range(len(x)):
        num = x[i]
        if not any(l <= num <= u for (l, u) in ranges):
            error += num

print(error)





# --- Day 16: Part Two --- 
import re
data = open("input.txt", "r").read().split('\n\n')

# Create tuples containing allowed ranges
ranges = data[0].split()
ranges = [x for x in ranges if re.search(r'\d', x)] 
ranges = [x.split('-') for x in ranges]
for i in range(len(ranges)):
    ranges[i][0] = int(ranges[i][0])
    ranges[i][1] = int(ranges[i][1])
ranges = [tuple(x) for x in ranges]


# Separate nearby tickets into list
others = data[2].split()
others = [x for x in others if re.search(r'\d', x)] 
others = [x.split(',') for x in others]
for x in others:
    for i in range(len(x)):
        x[i] = int(x[i])


# Create new list with only valid tickets
valid = []
for x in others:
    counter = 0
    for i in range(len(x)):
        num = x[i]
        if not any(l <= num <= u for (l, u) in ranges):
            break
        counter += 1
        if counter == len(x):
            valid.append(x)


# Rearrange valid tickets so that each element represents one category
cats = len(valid[0])
revalid = []
for i in range(cats):
    new = []
    for x in valid:
        new.append(x[i])
    revalid.append(new)


# Re-organize tuples into sets of two ranges each
newranges = []
for i in range(0, len(ranges)-1, 2):
    check = [ranges[i], ranges[i+1]]
    newranges.append(check)


# Create new list containing ranges of each category and the positions
# of ALL tickets that meet these ranges
categories = []
for validset in newranges:
    match = []
    for x in revalid:
        counter = 0
        for i in range(len(x)):
            num = x[i]
            if not any(l <= num <= u for (l, u) in validset):
                break
            counter += 1
            if counter == len(x):
                match.append(revalid.index(x))
    categories.append(match)


# Loop until each category correlates with only one possible position. The 
# key is that you need to begin by finding one ticket that only corresponds
# to one possible set of ranges. Use process of elimination until each array
# has only one possible position
final = []
for i in range(cats):
    for x in categories:
        num = x[0]
        if len(x) == 1 and num not in final:
            final.append(num)
            break
    for y in categories:
        if num in y and len(y) != 1:
            y.remove(num)


# Flatten out categories so that each value corresponds to index, which
# in turn corresponds to the category value
categories = [x[0] for x in categories]


# List of all possible categories 
classes = data[0].split('\n')
for i in range(len(classes)):
    string = classes[i].split(':')
    classes[i] = string[0]


# List out values of your ticket
mytick = data[1].split('\n')
mytick = mytick[1].split(',')
mytick = [int(x) for x in mytick]


# Calculate index of any value with 'departure', then point to position of
# this value on ticket and finally use your ticket to multiply the values
multiplier = 1
for i in range(len(classes)):
    if 'departure' in classes[i]:
        index = categories[i]
        multiplier *= mytick[index]
print(multiplier)