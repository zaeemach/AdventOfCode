# --- Day 15: Rambunctious Recitation ---
data = '0,5,4,1,10,14,7'
data = data.split(',')
data = [int(x) for x in data]

for i in range(2020-len(data)):
    init = data[-1]
    last = len(data)-1
    domain = data[0:last]
    if init not in domain:
        data.append(0)
    else:
        for i in range(last-1, -1, -1):
            if data[i] == init:
                diff = last - i
                data.append(diff)
                break

print(data[-1])


# Second Solution
# Runs faster
(data = '0,5,4,1,10,14,7'
data = data.split(',')
data = [int(x) for x in data]


for i in range(100020-len(data)):
    init = data[-1]
    last = len(data)-1
    domain = data[0:last]
    if init not in domain:
        data.append(0)
    else: 
        data.reverse()
        data.remove(init)
        diff = data.index(init) + 1
        data.reverse()
        data.extend([init, diff])

print(data[-1]))


# Third solution
# Most optimal, not iterations
data = '0,5,4,1,10,14,7'
data = data.split(',')
data = [int(x) for x in data]

# Initialize values for loop
index = len(data)-1
value = data[-1]
final = 2020

# Convert data list to set excluding the last value
data = {data[i]: i for i in range(index)}

# Run loop until required index is reached
while index < final-1:
    if value not in data:
        data[value] = index
        value = 0
    else: 
        diff = index - data[value]
        data[value] = index
        value = diff
    index += 1

print(value)


# --- Day 15: Part Two --- 
data = '0,5,4,1,10,14,7'
data = data.split(',')
data = [int(x) for x in data]

# Initialize values for loop
index = len(data)-1
value = data[-1]
final = 30000000

# Convert data list to dict excluding the last value
data = {data[i]: i for i in range(index)}

# Run loop until required index is reached
while index < final-1:
    if value not in data:
        data[value] = index
        value = 0
    else: 
        diff = index - data[value]
        data[value] = index
        value = diff
    index += 1

print(value)

# Note that this will not work unless the input string already contains
# a zero. If we use 1,2,3 then we'll have 1,2,3,0,0,1. The while loop
# does not account for the first time a zero occurs with a second zero
# as the first zero has already joined the dictionary. In this case, 
# during the initialization, maybe expand the string until the first 
# zero occurs and then initialize the dictionary with the new data set.
# Another option is to simply add a conditional statement but checking
# against it constantly seems useless? 