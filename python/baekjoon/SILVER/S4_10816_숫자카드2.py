import sys

data = sys.stdin.read().splitlines()

given_card = data[1].split()
card_list = data[3].split()

d = {}

for card in given_card:
    if d.get(card):
        d[card] += 1
    else:
        d[card] = 1

for i in card_list:
    if d.get(i):
        print(d[i], end = ' ')
    else:
        print(0, end=' ')
