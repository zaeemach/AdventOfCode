# --- Day 12: Rain Risk ---
import re
directions = open('input.txt').read().splitlines()

# Initial variables 
initShip = [0,0,0,0]
initCurr = 1

# Each indice corresponds to a direction. The variable
# below initializes them so that they correspond to a
# a circular pattern -- this will help when rotating
deg = {'N':0, 'E':1, 'S':2, 'W':3}

# Function definining Manhattan distance for any position
# with 4 coordinates in the order specified by deg variable
def mnhttnDis(ship):
    return abs(ship[0]-ship[2]) + abs(ship[1]-ship[3])

# Function for part one -- initCurr corresponds to initial
# direction the ship is facing, which is East
def finalShip(ship, curr):
    for x in directions:
        x = re.findall(r'[A-Z]+|\d+', x)
        drc = x[0]
        mag = int(x[1])
        if drc == 'R':
            mag = mag/90
            curr = (curr + mag)%4
        elif drc == 'L':
            mag = -1*mag/90
            curr = (curr + mag)%4
        elif drc == 'F':
            ship[curr] += mag
        else:
            ship[deg[drc]] += mag
    return ship

# Function for part two, uses all initial values from part
# one except initCurr, which is replaced by initWp for the
# waypoint
initWp = [1,10,0,0]
def wpShip(ship, wp):
    for x in directions:
        x = re.findall(r'[A-Z]+|\d+', x)
        drc = x[0]
        mag = int(x[1])
        pos = [0,1,2,3]
        if drc == 'R':
            mag = -1*mag/90
            pos = [(mag+x)%4 for x in pos]
            wp = [wp[i] for i in pos]
        elif drc == 'L':
            mag = mag/90
            pos = [(mag+x)%4 for x in pos]
            wp = [wp[i] for i in pos]
        elif drc == 'F':
            add = [mag*x for x in wp]
            ship = [sum(y) for y in zip(ship, add)]
        else:
            wp[deg[drc]] += mag
    return ship

# Part One
print('Part One: %i' % mnhttnDis(finalShip(initShip,initCurr)))

# Part Two
print('Part Two: %i' % mnhttnDis(wpShip(initShip,initWp)))


# Both functions above take advantage of modulo to correctly
# account for changes in direction. It allows to move forward 
# and backward in a circular manner in the list without using 
# actual degrees. Below, I demonstrate its use in each function.
#
# Part One
# The problems starts at position 1, which corresponds to East. 
# If we rotate right by 90 degrees, then we should be moving to 
# position 2/South. If we move 180 degrees instead, we're at
# position 3/West and so on. 90 degrees, then, corresponds to 
# one unit of positional change. This is the same as saying:
# 90 deg/90 --> 1 unit change
# 180 deg/90 --> 2 units change
# 270 deg/90 --> 3 units change
# The total possible positions are 0,1,2,3 which are respresented 
# by the indices so that positions 0,1,2,3 = N,E,S,W. 
# To move circularly, modulo is implemented so that W goes back to N 
# when moving right and loops back to W when moving left.
#
# Part Two
# This one's slightly more complex. We start with defining a new 
# var within the function: pos = [0,1,2,3]. The waypoint is at 
# [1,10,0,0]. When the waypoint rotates right, its positions 
# change such that pos = [3,0,1,2]. This corresponds to the new
# waypoint position at [0,1,10,0]. So the code first changes the 
# positions and then uses the change to rewrite the new waypoint
# coordinates. 