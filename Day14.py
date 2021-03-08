# --- Day 14: Docking Data ---
import re
program = open("input.txt", "r").read().splitlines()

# Function takes an integer, converts it to a 36-bit binary string and applies
# a mask. Returns resultant integer after mask is applied.
def applyMask(mask, num):
    num = '{:036b}'.format(num)
    for i in range(len(mask)):
        if mask[i] != 'X':
            num = num[:i] + mask[i] + num[i+1:]
    return int(num, 2)

# Initialize memory storage as dictionary
mem = {}

for x in program:
    if 'mask' in x:
        mask = x.split(' = ')[1]

    else:
        seg = x.split(' = ')        
        key = int(re.search(r'\d+', seg[0]).group())
        num = int(seg[1])        
        newmem = applyMask(mask, num)
        mem[key] = newmem

print(sum(mem.values()))


# --- Day 14: Part Two ---
import itertools, re
program = open("input.txt", "r").read().splitlines()

# Apply a mask that transforms memory address 
def applyMask(mask, num):
    num = '{:036b}'.format(num)
    for i in range(len(mask)):
        if mask[i] != '0':
            num = num[:i] + mask[i] + num[i+1:]
    return num

# Initialize memory storage as dictionary
mem = {}

# First find values of bit corresponding to X values
# For example: XVals for '00X0X' would be [1, 4]
# Second, generate list of all possibilities those X
# values would give us. In this example, we'd have:
# [], [1], [4], [1+4]

def combinations(newmem):
    XVals = [2**(35-i) for i, x in enumerate(newmem) if x == 'X']

    combos = []
    for i in range(len(XVals)+1):
        for combo in itertools.combinations(XVals, i):
            combos.append(sorted(combo))

    combos = [sum(x) for x in combos]
    minimum = newmem.replace('X', '0')
    minimum = int(minimum, 2)
    combos = [minimum+x for x in combos]

    return combos


# Go through the init program and apply the two functions above
for x in program:
    if 'mask' in x:
        mask = x.split(' = ')[1]
    else: 
        seg = x.split(' = ')
        key = int(re.search(r'\d+', seg[0]).group())
        val = int(seg[1])
        newmem = applyMask(mask, key)
        combos = combinations(newmem)
        for x in combos:
            mem[x] = val

print(sum(mem.values()))



# Theory: the combinations depend on the decimal values of X.
# If we have '1XX0X', then the X values are 1, 4, 8. These values
# can then be organized in many different ways to produce the
# remaining combinations. 
#
# The combinations function takes these values and finds all 
# possible combinations without accounting for order. Now
# let's generate combinations(x) where x = number of values:
# combinations(0): []
# combinations(1): [1], [4], [8]
# combinations(2): [1, 4], [1, 8], [4, 8]
# combinations(3): [1, 4, 8]
#
# So the total combinations are:
# [], [1], [4], [8], [1, 4], [1, 8], [4, 8], [1, 4, 8]
#
# These combinations correspond to binary as follows:
# []: 10000
# [1]: 10001
# [4]: 10100
# [8]: 11000
# [1, 4]: 10101
# [1, 8]: 11001
# [4, 8]: 11100
# [1, 4, 8]: 11101
#
# Note that right now, the combinations refer to the POSITIONS. To 
# convert them to an actual integer, we simply add them up:
# []: 0
# [1]: 1
# [4]: 4
# [8]: 8
# [1, 4]: 5
# [1, 8]: 9
# [4, 8]: 12
# [1, 4, 8]: 13
#
# Now note that we need to preserve all exisiting ones from before, 
# regardless of the Xs. In our example '1XX0X', if all the Xs are
# set at zero, the binary number is minimum of 16. All other 
# combinations are simply additions to this. So the final numbers
# after the mask is applied gives:
# 0 + 16 = 16
# 1 + 16 = 17
# 4 + 16 = 20
# 8 + 16 = 24
# 5 + 16 = 21
# 9 + 16 = 25
# 12 + 16 = 28
# 13 + 16 = 29