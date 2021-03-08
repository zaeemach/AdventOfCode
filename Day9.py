# --- Day 9: Encoding Error ---
data = open("input.txt", "r").read().splitlines()
data = list(map(int, data))

for i in range(25, len(data)):
    var = False
    l = i-25
    u = i-1
    for j in range(l, u):
        if (data[i]-data[j]) in data[l:i]:
            var = True
            break
    if not var:
        print(data[i])
        break

# --- Day 9: Part Two ---
for i in range(0, len(data)):
    sums = data[i]
    l = i+1
    for j in range(l, len(data)):
        if sums < err:
            sums += data[j]
            interval = data[i:j+1]
        if sums >= err:
            break
    if sums == err:
        total = min(interval)+max(interval)
        print(total)
        break