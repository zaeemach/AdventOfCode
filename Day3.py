# --- Day 3: Toboggan Trajectory ---
data = open("input.txt", "r").read().splitlines()

def tree_counter(landscape):
    counter = 0 
    trees = 0 
    for x in data:
        if x[counter] == '#':
            trees += 1
        counter += 3 
        counter = counter%len(x)
    print(trees)

tree_counter(data)


# --- Day 3: Part Two ---
data = open("input.txt", "r").read().splitlines()

def tree_counter(landscape):
    
    counter = 0 
    trees = 0 
    multiplier = 1
    
    for x in data:
        if x[counter] == '#':
            trees += 1
        counter += 3 
        counter = counter%len(x)
    
    print(trees)
        
    multiplier *= trees
    trees = 0
    counter = 0
    
    for x in data:
        if x[counter] == '#':
            trees += 1
        counter += 1 
        counter = counter%len(x)
    print(trees)

    multiplier *= trees
    trees = 0
    counter = 0
    
    for x in data:
        if x[counter] == '#':
            trees += 1
        counter += 5 
        counter = counter%len(x)
    print(trees)

    multiplier *= trees
    trees = 0
    counter = 0
    
    for x in data:
        if x[counter] == '#':
            trees += 1
        counter += 7 
        counter = counter%len(x)
    print(trees)

    multiplier *= trees
    trees = 0
    counter = 0
    
    for x in data[::2]:
        if x[counter] == '#':
            trees += 1
        counter += 1 
        counter = counter%len(x)
    print(trees)
        
    multiplier *= trees

    print(multiplier)

tree_counter(data)