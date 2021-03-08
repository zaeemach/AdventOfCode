# --- Day 11: Seating System ---
import itertools

seats = {}
with open('input.txt') as f:
    x = 0
    for line in f:
        coords = {(x,y): state for y, state in enumerate(list(line.strip())) if state != '.'}
        seats.update(coords)
        x += 1

neighbours = list(set(itertools.permutations([-1,-1,0,1,1], 2)))

newStates = {}
while seats != newStates:
    seats = dict(seats,**newStates)
    for coord in seats:
        nghbrs = [zip(coord, i) for i in neighbours]
        nghbrs = [(sum(x), sum(y)) for [x,y] in nghbrs if (sum(x), sum(y)) in seats]
        occupied = len([seats[x] for x in nghbrs if seats[x] == '#'])
        if seats[coord] == 'L' and occupied == 0:
            newStates[coord] = '#'
        if seats[coord] == '#' and occupied >= 4:
            newStates[coord] = 'L'

occupied = len([v for k,v in newStates.iteritems() if v == '#'])
print(occupied)



# --- Day 11: Part Two ---
import itertools

seats = {}
with open('input.txt') as f:
    x = 0
    for line in f:
        coords = {(x,y): state for y, state in enumerate(list(line.strip())) if state != '.'}
        seats.update(coords)
        x += 1
        rows = x
        cols = len(line.strip())

neighbours = list(set(itertools.permutations([-1,-1,0,1,1], 2)))

def occ(coord):
    occupied = 0
    for n in neighbours:
        a = tuple([sum(x) for x in zip(coord, n)])
        while a not in seats:
            a = tuple([sum(x) for x in zip(a, n)])
            if not 0 <= a[0] < rows or not 0 <= a[1] < cols:
                break
        if a in seats and seats[a] == '#':
            occupied += 1
    return occupied


newStates = {}
while seats != newStates:
    seats = dict(seats,**newStates)
    for coord in seats:
        occupied = occ(coord)
        if seats[coord] == 'L' and occupied == 0:
            newStates[coord] = '#'
        if seats[coord] == '#' and occupied >= 5:
            newStates[coord] = 'L'

occupied = len([v for k,v in newStates.iteritems() if v == '#'])
print(occupied)

