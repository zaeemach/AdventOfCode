# --- Day 5: Binary Boarding ---
data = open("input.txt", "r").read().splitlines()
import math

def highest_ID(seats):
    
    row = 0
    column = 0
    prevID = 0
    
    for x in seats:
        rows = [0, 127]
        columns = [0, 7]
        
        for i in x:
        
            rmedian = (rows[0]+rows[1])/2
            if i == 'F':
                rows[1] = math.floor(rmedian)
                row = rows[0]
            if i == 'B':
                rows[0] = round(rmedian)
                row = rows[1]
        
            cmedian = (columns[0]+columns[1])/2
            if i == 'L':
                columns[1] = math.floor(cmedian)
                column = columns[0]
            if i == 'R':
                columns[0] = round(cmedian)
                column = columns[1]
            
        seatID = 8*row+column
        if seatID > prevID:
            prevID = seatID
    
    print(prevID)

highest_ID(data)


# --- Day 5: Part Two ---
data = open("input.txt", "r").read().splitlines()
import math

def highest_ID(seats):
    
    row = 0
    column = 0
    prevID = []
    
    for x in seats:
        rows = [0, 127]
        columns = [0, 7]
        
        for i in x:
        
            rmedian = (rows[0]+rows[1])/2
            if i == 'F':
                rows[1] = math.floor(rmedian)
                row = rows[0]
            if i == 'B':
                rows[0] = round(rmedian)
                row = rows[1]
        
            cmedian = (columns[0]+columns[1])/2
            if i == 'L':
                columns[1] = math.floor(cmedian)
                column = columns[0]
            if i == 'R':
                columns[0] = round(cmedian)
                column = columns[1]
            
        seatID = 8*row+column
        prevID.append(seatID)
    
    newID = sorted(prevID)
    missing = sum(range(newID[0], (newID[len(newID)-1]+1))) - sum(newID)
    print(missing)

highest_ID(data)