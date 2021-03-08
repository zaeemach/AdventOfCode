# --- Day 13: Shuttle Search ---
import re
notes = open('input.txt').read().splitlines()

# Create dictionary of buses with keys being IDs and values being their
# positions if they were in a list
buses = {int(x): i for i,x in enumerate(notes[1].split(',')) if x != 'x'}

# Part One: create a dictionary with differences between the timestamp and 
# each bus ID -- find the minimum in this list and multiply it wit its ID
timestamp = int(notes[0])
diff = {x-timestamp%x: x for x in buses}
multiplier = min(diff)*diff[min(diff)]

# Part Two: full theory below -- first find the 'reference' bus that we
# will be using, which is the first one. Next, use the algorithim on each
# remaining ID to generate the final answer 
checked = [x for x in buses if buses[x] == 0]
i = checked[0]
del buses[i]
for ID in buses:
    pos = buses[ID]%ID
    while i%ID != ID-pos:
        i += reduce(lambda x, y: x*y, checked)
    checked.append(ID)

# Part One
print('Part One: %i' % multiplier)

# Part Two
print('Part Two: %i' % i)


# Theory: let's start with set (3, 7). Say we need to find a number 'x' such 
# that it is completely divisible by 3 but leaves a remainder of 1 when 
# the modulus is calculated. This is the same as saying:
# 'x' % 3 = 0
# 'x' % 7 = 1
# Running a while loop similar to the one in part two says that the FIRST
# occurence of this condition being met is at number x = 15. What about the 
# occurence and the one after? The first thing to note is the next occurence 
# must always be fully divisble by 3. This is ensured by setting x += 3. So 
# now we have 15, 18, 21... Now we also need the next occurrence to give 7
# a remainder of 1. This is ensure by setting x += 7. 
# Now we have two requirements on x = 15: x += 3 and x += 7. These requirements
# can beautifully be woven into one requirement: x += 3*7! 
# Now we can generate the next few occurrences:
# i: 15
# ii: 15 + (3*7) = 36
# iii: 15 + 2(3*7) = 57
# And so forth. Let's say we now have a new condition: each number should give
# a value of 3 when x % 9 is calculated. To find the next condition, we run the 
# the same while loop. This time, we increment each possible occurence by (3*7) 
# because this ensures the number we find for 9 ALSO still meets the conditions
# for 3 and 7. Running the loop gives 57. Checking this confirms the requirements:
# 57 mod 3 = 0, 57 mod 7 = 1, 57 mod 9 = 3
# Let's say we have a fourth condition: x mod 4 must equal 2. We yet again run
# the same loop, this time incrementing by (3*7*9) so that all previous conditions
# are met. Running the loop gives 246. Checking each condition again confirms
# that all requirements are met. The code simply takes advantage of this beautiful
# pattern. Note how this prevents the need to check each number. Further, the larger
# the remainders and the numbers get, the larger the increments become, further
# optimizing which numbers are checked.
#
# One more point to note involves edge cases like this: 19,x,x,x,x,3. This says
# that x mod 3 = 5. But this cannot be so because if 3 occurred 5 spaces later, 
# it MUST have occurred in between, namely 3 positions ago: 19,x,3,x,x,3. But 
# code does not give us this infomation. So how do we tell it that we want 
# x mod 3 = 2, which is the same as saying x mode 3 == 5? We can simply do:
# 5 mod 3 = 2. This ensures each position is rewritten as the FIRST INSTANCE
# away from x. The code will then flow smoothly! 