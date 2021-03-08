# --- Day 2: Password Philosophy ---
data = open("input.txt", "r").read().splitlines()

import re
for x in data:
    data[data.index(x)] = re.split(' |-|: ', x)

def counter(y):
    passwords = 0
    for x in y:
        if int(x[0]) <= x[3].count(x[2]) <= int(x[1]):
            passwords += 1
    print(passwords)
    
counter(data)


# --- Day 2: Part Two ---
data = open("input.txt", "r").read().splitlines()

import re
for x in data:
    data[data.index(x)] = re.split(' |-|: ', x)

def counter(y):
    passwords = 0
    for x in y:
        a = int(x[0])-1
        b = int(x[1])-1
        if (x[3][a] == x[2]) != (x[3][b] == x[2]):
            passwords += 1
    print(passwords)
    
counter(data)