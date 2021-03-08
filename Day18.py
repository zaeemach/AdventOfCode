# --- Day 18: Operation Order ---
import re
# Function to evalutae bracket-less strings, returns numerical string.
def newOrder(data):
    data = data.split()
    value = data[0]
    length = len(data)
    i = 1
    while i < length:
        value = value + ''.join(data[i:i+2])
        value = str(eval(value))
        i += 2
    return value

# Function to evaluate any string containing bracket, returns 
# numerical string.
def brackets(br):
    while '(' in br:
        oldVal = re.search(r'\([^\(^\)]+\)', br).group()
        newVal = newOrder(oldVal[1:-1])
        br = br.replace(oldVal, newVal)
    return newOrder(br)

# Calls functions depending on equation type. Converts numerical
# string to integer and adds to total count.
data = open("input.txt", "r").read().splitlines()
total = 0
for eq in data:
    if '(' in eq:
        total += int(brackets(eq))
    else:
        total += int(newOrder(eq))
print(total)



# --- Day 18: Part Two ---
import re
# Function to evaluate with new order. Returns numerical string.
# Note that it is important to note that replace() only replaces
# the FIRST occurrence and not all occurrences. This ensures that 
# oldVal and newVal are both applying to the SAME substring.
def newOrder(equ):
    while '+' in equ:
        oldVal = re.search(r'\d+\s\+\s\d+', equ).group()
        newVal = str(eval(oldVal))
        equ = equ.replace(oldVal, newVal, 1)
    return str(eval(equ))

# Function to evaluate any string containing bracket, returns 
# numerical string.
def brackets(br):
    while '(' in br:
        oldVal = re.search(r'\([^\(^\)]+\)', br).group()
        newVal = newOrder(oldVal[1:-1])
        br = br.replace(oldVal, newVal)
    return newOrder(br)

# Calls functions depending on equation type. Converts numerical
# string to integer and adds to total count.
data = open("input.txt", "r").read().splitlines()
total = 0
for eq in data:
    if '(' in eq:
        total += int(brackets(eq))
    else:
        total += int(newOrder(eq))
print(total)
