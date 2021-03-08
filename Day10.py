# --- Day 10: Adapter Array ---
data = open("input.txt", "r").read().splitlines()
data = [int(x) for x in data]
data.extend([0, max(data)+3])
data = sorted(data)

one = 0
three = 0

for i in range(len(data)-1):
    difference = data[i+1]-data[i]
    if difference == 1:
        one += 1
    if difference == 3:
        three += 1

multiplier = one*three
print(multiplier)

# --- Day 10: Part Two ---
data = open("input.txt", "r").read().splitlines()
data = [int(x) for x in data]
data.extend([0, max(data)+3])
data = sorted(data)

# notes explaining this below
fib = [0,1,2,4,7,13,24]
comb = []
ones = []

for i in range(len(data)-1):
    difference = data[i+1]-data[i]
    if difference == 1:
        ones.append(difference)
    else:
        comb.append(ones)
        ones = []

combinations = 1
for x in comb:
    if len(x) != 0:
        combinations *= fib[len(x)]

print(data)

# Let's look at [0, 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, 22]
# There are two pairs of ones that correspond to valid differences:
# Between 4,5,6,7 and between 10,11,12: [1,1,1] and [1,1]
# There are 4 ways of organizing [1,1,1] into sums of 1,2 or 3: 
# [1,2], [1,1,1], [2,1] and [3]. Note that we don't want sums greater
# than 3 as that would correspond to differences larger than 3.
# For [1,1]: [1,1] and [2]. 
# So the first pair is organized in 4 ways and second is in 2 ways.
# This is a total of 4*2 = 8 ways for the adapters to be organized.

# There is an interesting pattern. For [1,1,1,1]:
# If we keep the first 1, the last three can be organized in 4
# different ways as found above. 
# If we now combine the second one, we have 2 and [1,1] left. This 
# can be organized in 2 ways.
# Combining the third one gives us 3 and [1], which can be organized
# in just on way. 
# In total, there are: 4+2+1 = 7 ways.
# This is the same as adding the preceding three numbers in the
# pattern: [1], [1,1], [1,1,1], [1,1,1,1] is 1,2,4,7 combinations.

# Continuing forward, let's look at [1,1,1,1,1]:
# Keeping the first one leaves [1,1,1,1], this is 7 combinations.
# Combining into 2 leaves [1,1,1], this is 4 combiations.
# Combining into 3 leaves [1,1], this is 2 combiations.
# Same again! We have added the preceeding three numbers!

# Therefore, 1,2,4,7,13... corresponds to the total combinations 
# any set of ones that can be combined into 1,2 or 3! 