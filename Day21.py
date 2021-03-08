# --- Day 21: Allergen Assessment ---
import re
foods = open('input.txt', 'r').read().splitlines()
# Re-write so that first element corresponds to allergens and second corresponds to 
# associated ingredients
foods = [[re.search(r'\(contains\s([^)]+)', x).group(1).split(', '),x.split(' (')[0].split(' ')] for x in foods]

allrgns = {}
totalings = []
# Keep mapping out intersections between one group of allergends and ALL other allergens,
# returning list will contain only a few possibilities or the final answer. Add this to 
# a dictionary, which will then be analyzed to find the corresponding ingredients 
for x in foods:
    allrgn = x[0]
    ingrdnts = x[1]
    totalings.extend(ingrdnts)
    for y in foods:
        if set(allrgn)&set(y[0]):
            allrgn = list(set(allrgn)&set(y[0]))
            ingrdnts = list(set(ingrdnts)&set(y[1]))
    allrgns[allrgn[0]] = ingrdnts
    allergens.extend(ingrdnts)

totalings = [x for x in totalings if not any(x in val for val in allrgns.values())]
print(len(totalings))


# --- Day 21: Part Two ---
known = [x[0] for x in allrgns.values() if len(x) == 1]
for x in known:
    for k in allrgns.keys():
        v = allrgns[k]
        if len(v) != 1:
            newval = list(set(v)-set([x]))
            allrgns[k] = newval
            if len(newval) == 1 and newval[0] not in known:
                known.extend(newval)

dangerousList = sorted([k for k in allrgns.keys()])
dangerousList = ','.join([allrgns[x][0] for x in dangerousList])
print(dangerousList)