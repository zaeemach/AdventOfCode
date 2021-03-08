# --- Day 6: Custom Customs ---
data = open("input.txt", "r").read().split('\n\n')

def yes_ans(a):
    total = 0
    
    for x, y in enumerate(a):
        a[x] = "".join(set(y.replace('\n', '')))
        total += len(data[x])

    print(total)

yes_ans(data)


# --- Day 6: Part Two ---
INCOMPLETE