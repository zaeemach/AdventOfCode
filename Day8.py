# --- Day 8: Handheld Halting ---
data = open("input.txt", "r").read().splitlines()

for i in range(0, len(data)):
    data[i] = data[i].split(' ')
    data[i][1] = int(data[i][1])

a = 0
acc = 0
counter = []

while True:
    init = data[a][0]
    value = data[a][1]
    counter.append(a)
    if init == 'nop':
        a += 1
    if init == 'acc':
        a += 1
        acc += value
    if init == 'jmp':
        a += value
    if set(counter)&{a}:
        break
print(acc)

# --- Day 8: Part Two ---
data = open("input.txt", "r").read().splitlines()

for i in range(0, len(data)):
    data[i] = data[i].split(' ')
    data[i][1] = int(data[i][1])

for x in data:
    if x[0] == 'nop':
        x[0] = 'jmp'
    elif x[0] == 'jmp':
        x[0] = 'nop'

    a = 0
    acc = 0
    counter = []

    while x[0] != 'acc' and x != ['jmp', 0]:
        init = data[a][0]
        value = data[a][1]
        counter.append(a)
        if init == 'nop':
            a += 1
        if init == 'acc':
            a += 1
            acc += value
        if init == 'jmp':
            a += value
        if set(counter)&{a} or a == len(data):
            break

    if a == len(data):
        print(x)
        break

    if x[0] == 'nop':
        x[0] = 'jmp'
    elif x[0] == 'jmp':
        x[0] = 'nop'