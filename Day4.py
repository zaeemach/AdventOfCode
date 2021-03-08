# --- Day 4: Passport Processing ---
import re
data = open("input.txt", "r").read().split('\n\n')
data = [re.split('\s|:', x) for x in data]

key = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
key_op = [x for x in key if x != "cid"]

counter = 0
for x in data:
    if (set(x)&set(key) == set(key)) or (set(x)&set(key) == set(key_op)):
        counter += 1

print(counter)

# --- Day 4: Part Two ---
import re
data = open("input.txt", "r").read().split('\n\n')
data = [re.split('\s|:', x) for x in data]

key = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
key_op = [x for x in key if x != "cid"]

valid = []
for x in data:
    intersect = set(x)&set(key)
    if (intersect == set(key)) or (intersect == set(key_op)):
        valid.append(x)
print(valid[1])

tracker = 0
for x in valid: 
    counter = 0
    for i in range(0, len(x)-1, 2):
        if x[i] == 'byr' and int(x[i+1]) in range(1920,2003):
            counter += 1
        elif x[i] == 'iyr' and int(x[i+1]) in range(2010,2021):
            counter += 1
        elif x[i] == 'eyr' and int(x[i+1]) in range(2020, 2031):
            counter += 1
        elif x[i] == 'hgt':
            if 'cm' in x[i+1] and int(x[i+1].replace('cm', '')) in range(150, 194):
                counter += 1
            if 'in' in x[i+1] and int(x[i+1].replace('in', '')) in range(59, 77):
                counter += 1
        elif x[i] == 'hcl' and re.match(r"#[0-9a-f]{6}$", x[i+1]):
            counter += 1
        elif x[i] == 'ecl' and re.match(r"amb$|blu$|brn$|gry$|grn$|hzl$|oth$", x[i+1]):
            counter += 1
        elif x[i] == 'pid' and re.match(r"[0-9]{9}$", x[i+1]):
            counter += 1
        elif x[i] == 'cid':
            counter += 0
        else: 
            break
    if counter == 7:
        tracker += 1

print(tracker)