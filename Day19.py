# --- Day 19: Monster Messages ---
import re

# Create dictionary for rules and list for received messages
data = open("input.txt", "r").read().split('\n\n')
data1 = data[0].split('\n')
data1 = [x.split(': ') for x in data1]
rules = {}
for x in data1: 
    rules[x[0]] = x[1]
messages = data[1].split('\n')


# Initialize tracker by finding numbers the correspond to letters; use of 
# init will be displayed below
init = []
tracker = []
for k, v in rules.iteritems():
    if 'a' in v or 'b' in v:
        tracker.append(k)
        init.append(k)


# Add ordered sequence of numbers to loop through when assigning possibilities
while '0' not in tracker:
    for k, v in rules.iteritems():
        check = re.findall(r'\d+', v)
        if k not in tracker and set(check) <= set(tracker):
            tracker.append(k)


# Finalizes the rules dictionary. Removes keys corresponding to letters 
# from tracker and converts alphabetical values into lists. This will ensure smooth 
# flow in the next step.
for x in init:
    if x in rules.keys():
        tracker.remove(x)
        change = re.findall(r'\w+', rules[x])
        rules[x] = change


# Function prepares values to generate combinations. It draws on pre-existing 
# combinations and plugs them in. They will then be combined into the next 
# function. Returns list.
def splitter(num):
    num = num.split(' | ')
    num = [x.split() for x in num]
    for i, x in enumerate(num):
        num[i] = [rules[j] for j in x]
    return num


# Function takes given rule and returns list of all possible combinations.
# Takes argument in the form of lists. If rules are separated by space, they
# are in the same list. If separated by commas, they are in different lists.
def combines(rule):
    combos = []
    i = 0
    while len(rule) != 1:
        add = rule[0][i]
        def combine(x):
            return add + x
        new = map(combine, rule[1])
        combos.extend(list(new))        
        i += 1
        if i == len(rule[0]):
            i = 0
            del rule[0:2]
            rule.insert(0, combos)
            combos = []
    return rule[0]


# Loop through tracker and update each key's value with the new combinations.
for k in tracker:
    value = rules[k]
    value = splitter(value)
    combos = []
    for x in value:
        combos.extend(combines(x))
    rules[k] = combos


# Find intersection between combinations is zeroth rule and in messages. Display how
# how many matches are found.
matches = set(rules['0'])&set(messages)
matches = list(matches)
print(len(matches))



# --- Day 19: Part Two ---
# Find how long each string is in rules '31' and '42'. Note all strings will be equally long in 
# each key.
t = len(rules['31'][0])
f = len(rules['42'][0])


# See below for complete theory.
# Code reads each string from end to start (could have done it the other way around too). Once 
# the loop for subgroups in '31' is exited, the remaining subgroups are checked in rule '42'. 
# The code then checks if certain requirements are met. This prevents counting invalid combinations
# such as 42 31 42 or 42 42 42 or 42 31 31. Each valid combination will ALWAYS have 31 at the end,
# more 42s than 31s and 42 at the beginning. The last condition is met by checking if i == 0. This
# can only be true if we stay inside the rule '42' while loop till the zeroth index is reached. This in 
# turn implies all remaining subgroups after rule '31' were in '42'. This would invalidate, for example,
# 31 42 42 42 42 31. While the combinatination after '31' is valid, the entire combination is not, as 
# it does not begin with '42'.

total = 0 
for a in messages:
    i = len(a)
    begloops = 0
    endloops = 0
    while a[i-t:i] in rules['31']:
        i -= t
        endloops += 1

    while a[i-f:i] in rules['42']:
        i -= f
        begloops += 1

    if i == 0 and endloops >= 1 and begloops > endloops:
        total += 1

print(total)


# ALL combinations can be broken down into the initial length of the strings, which was 
# calculated above. For example, let's say we have a rule '5' that gives combinations ['aa', 'bb'].
# Then the rule '5 5' would give: ['aaaa', 'aabb', 'bbaa', 'bbbb']. If we now break down each 
# of these combinations into 2 groups each, we would recover the original ['aa', 'bb']. 
#
# Next, let's see the new rule '8': 42 | 42 8. This rule loops infinitely into itself. Let's write
# out the next few loops:
# 0th loop: 42 | 42 8
# 1st loop: 42 | 42 42 | 42 42 8
# 2nd loop: 42 | 42 42 | 42 42 42 | 42 42 42 42 | 42 42 42 42 8
# The pattern is clear. Rule '8' gives the combinations: 42, 42 42, 42 42 42, ... and so on. 
#
# Let's do the same for rule '11': 42 31 | 42 11 31. Writing out the next few loops:
# 0th loop: 42 31 | 42 11 31
# 1st loop: 42 31 | 42 42 31 31 | 42 42 11 31 31 
# 2nd loop: 42 31 | 42 42 31 31 | 42 42 42 31 31 31 | 42 42 42 42 31 31 31 31 | 42 42 42 42 11 31 31 31 31
# A similar pattern emerges. Rule '11' gives the combinations: 42 31, 42 42 31 31, 42 42 42 31 31 31, ....
#
# Rule '0' is simply 8 11. The combinations are endless as both rules '8' and '11' produce infinite 
# combinations. Some of these are listed below:
# 42 42 31
# 42 42 42 31 31 
# 42 42 42 42 42 31
# Some features of these combinations stay constant. First, each combination begins with 42 and ends with 31. 
# Second, each combination must have at least ONE more 42 than 31. This is simply a consequence of the way
# the rules are designed. 
#
# The code is written with all of this in mind. Producing hypothetical combinations is completely 
# unnecessary as they are endless and inefficient. Instead, the code looks at the MESSAGES and uses one 
# important fact: each message contains a subgroup of the possible combinations found in rules '42' and '31'.
# A string can be hundreds of characters long but can always be broken down into constiuents corresponding
# to these rules. This is beautiful as it means we only need the combinations in '42' and '31' and 
# can ignore producing all other combinations. The code then checks whether each subgroup belongs in '42' or 
# '31' and also ensures that each message meets the requirements for valid combinations: (a) there are more
# 42s than 31s and (b) each message ends with 31. If all subgroups match the rules within these requirements, 
# the code validates them and adds them to a counter. Simple!