# --- Day 20: Jurassic Jigsaw ---
import re
data = open("input.txt", "r").read().split('\n\n')
data = [x.splitlines() for x in data]
tiles = {}
alltiles = {}

# Create tiles dictionary with 4 components in the order:
# first row, last row, first column, last colum.
# Create alltiles dict with all tiles and their corresponding
# tiles numbers
for x in data:
    key = int(re.search(r'\d+', x[0]).group())
    fcol = ''.join([y[0] for y in x[1:]])
    lcol = ''.join([y[-1] for y in x[1:]])
    val = [x[1], x[-1], fcol, lcol]
    tiles[key] = val
    alltiles[key] = x[1:]

# Go through tiles dictionary and compare one tile against all
# tiles to see if any of their edges line up. If they do, add 
# the tile as a neighbour to the tile being checked
nghbrs = {x: [] for x in tiles}
for k in tiles.keys():
    for nk in tiles.keys():
        # Check matches for first row
        if tiles[k][0] in tiles[nk] and nk != k:            
            nghbrs[k].append(nk)
        # Check matches for first row reversed
        if tiles[k][0][::-1] in tiles[nk] and nk != k:
            nghbrs[k].append(nk)
        # Check matches for last row
        if tiles[k][1] in tiles[nk] and nk != k:
            nghbrs[k].append(nk)
        # Check matches for last row reversed
        if tiles[k][1][::-1] in tiles[nk] and nk != k:
            nghbrs[k].append(nk)
        # Check matches for first column
        if tiles[k][2] in tiles[nk] and nk != k:
            nghbrs[k].append(nk)
        # Check matches for first column reversed
        if tiles[k][2][::-1] in tiles[nk] and nk != k:
            nghbrs[k].append(nk)
        # Check matches for last column
        if tiles[k][3] in tiles[nk] and nk != k:
            nghbrs[k].append(nk)
        # Check matches for last column reversed
        if tiles[k][3][::-1] in tiles[nk] and nk != k:
            nghbrs[k].append(nk)
corners = [x for x in nghbrs if len(nghbrs[x]) == 2]

# Part One
print('Part One: %i' % reduce(lambda x, y: x*y, corners))