# --- Day 23: Crab Cups ---
inputStr = '538914762'
label = [int(x) for x in inputStr]

curr = label[0]
l = len(label)
rounds = 100
for k in range(rounds):
    i = label.index(curr)
    trio = [label[(i+1)%l], label[(i+2)%l], label[(i+3)%l]]
    dest = curr - 1
    label = [x for x in label if x not in trio]
    while dest in trio:
        dest = dest - 1
    if dest not in label:
        dest = max(label)
    j = label.index(dest)
    label = label[:j+1] + trio + label[j+1:]
    curr = label[(label.index(curr)+1)%l]

i = label.index(1)
label = label[i+1:]+label[:i]
print(''.join([str(x) for x in label]))



# --- Day 23: Part Two ---