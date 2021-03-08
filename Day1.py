# --- Day 1: Report Repair ---
data = open("input.txt", "r").read().splitlines()
data = [int(i) for i in data]

def multiplier(sum):
    for x in data:
        if sum-x in data:
            print((sum-x)*x)
            return

multiplier(2020)  


# --- Day 1: Part Two ---
data = open("input.txt", "r").read().splitlines()
data = [int(i) for i in data]

def multiplier(sum):
    for x in data:
        for y in data:
            if sum-x-y in data:
                print(x*y*(sum-x-y))
                return
           
multiplier(2020) 