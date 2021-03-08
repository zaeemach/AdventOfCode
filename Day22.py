# --- Day 22: Crab Combat ---
import re
cards = {}
with open('input.txt') as f:
    f = f.read().split('\n\n')
    f = [x.split(':') for x in f]
    for i in range(2):
        p = re.findall(r'\d+', f[i][1])
        p = [int(x) for x in p]
        cards[f[i][0]] = p

while [] not in cards.values():
    play = sorted([cards['Player 1'][0], cards['Player 2'][0]])
    play = play[::-1]
    for plyr in cards:
        if play[0] in cards[plyr]:
            winner = cards[plyr]
            cards[plyr].remove(play[0])
            cards[plyr].extend(play)
        else:
            cards[plyr].remove(play[1])

points = range(1,len(winner)+1)
score = zip(points, winner[::-1])
score = sum([x[0]*x[1] for x in score])
print(score)


# --- Day 22: Part Two ---