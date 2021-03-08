# --- Day 17: Conway Cubes --- 
import itertools
pocket = open("input.txt", "r").read().splitlines()

# Generate list of all possible coordinates for neighbouring cubes.
# Cube whose neighbours we're checking will always relatively be at (0,0,0). 
# Only two zeroes to prevent (0,0,0) as a combination in list.
nghbrs = list(itertools.permutations([-1,-1,-1,0,0,1,1,1], 3))
nghbrs = list(set(nghbrs))

# Initialize the grid that will contain all coordinates
grid = {}

# Add initial values from pocket dimension to grid
for i, seg in enumerate(pocket):
    y = i
    z = 0
    for j, coord in enumerate(seg):
        x = j
        tup = (x,
         y, z)
        grid[tup] = coord

# Generates coordinates for all neighbors and returns as dictionary
# Will also include neighbours already in grid -- these will be overidden
# with the original values
def neighbours(grid):
    ngbhrGrid = {}
    for coord in grid:
        for n in nghbrs:
            nghbr = zip(coord, n)
            nghbr = tuple([sum(x) for x in nghbr])
            ngbhrGrid[nghbr] = '.'
    return ngbhrGrid

# Takes each coord and generates checks its 26 neighbours. If the
# coord state changes, adds it to a new dictionary. Returns new
# dictionary with new states/changes
def newStates(grid):
    newStates = {}
    for coord in grid:
        actives = 0
        for n in nghbrs:
            nghbr = zip(coord, n)
            nghbr = tuple([sum(x) for x in nghbr])
            if nghbr in grid and grid[nghbr] == '#':
                actives += 1
        if grid[coord] == '#' and not 2 <= actives <= 3:
            newStates[coord] = '.'
        if grid[coord] == '.' and actives == 3:
            newStates[coord] = '#'
    return newStates

for i in range(6):
    # Add only new neighboring coordinates to grid
    newNghbr = neighbours(grid)
    grid = dict(newNghbr,**grid)

    # Replace coord values in grid with new states
    newGrid = newStates(grid)
    grid = dict(grid,**newGrid)

# Sum all active states left over and print result
totalActives = sum(1 for val in grid.values() if val == '#')
print(totalActives)

# --- Day 17: Part Two --- 
import itertools
pocket = open("input.txt", "r").read().splitlines()

# Add one more instance of each number and output a list with 4 dimensions 
nghbrs = list(itertools.permutations([-1,-1,-1,-1,0,0,0,1,1,1,1], 4))
nghbrs = list(set(nghbrs))

# Initialize the grid that will contain all coordinates
grid = {}

# Add initial values from pocket dimension to grid, this time including
# the fourth dimension 'w'
for i, seg in enumerate(pocket):
    y = i
    z = 0
    w = 0
    for j, coord in enumerate(seg):
        x = j
        tup = (x, y, z, w)
        grid[tup] = coord

# Generates coordinates for all neighbors and returns as dictionary
# Will also include neighbours already in grid -- these will be overidden
# with the original values
def neighbours(grid):
    ngbhrGrid = {}
    for coord in grid:
        for n in nghbrs:
            nghbr = zip(coord, n)
            nghbr = tuple([sum(x) for x in nghbr])
            ngbhrGrid[nghbr] = '.'
    return ngbhrGrid

# Takes each coord and generates checks its 26 neighbours. If the
# coord state changes, adds it to a new dictionary. Returns new
# dictionary with new states/changes
def newStates(grid):
    newStates = {}
    for coord in grid:
        actives = 0
        for n in nghbrs:
            nghbr = zip(coord, n)
            nghbr = tuple([sum(x) for x in nghbr])
            if nghbr in grid and grid[nghbr] == '#':
                actives += 1
        if grid[coord] == '#' and not 2 <= actives <= 3:
            newStates[coord] = '.'
        if grid[coord] == '.' and actives == 3:
            newStates[coord] = '#'
    return newStates


cycles = 6
for i in range(cycles):
    # Add only new neighboring coordinates to grid
    newNghbr = neighbours(grid)
    grid = dict(newNghbr,**grid)

    # Replace coord values in grid with new states
    newGrid = newStates(grid)
    grid = dict(grid,**newGrid)

totalActives = sum(1 for val in grid.values() if val == '#')
print(totalActives)