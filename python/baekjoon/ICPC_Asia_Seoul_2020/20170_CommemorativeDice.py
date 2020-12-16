import sys
def gcd(a, b):
    if a < b:
        (a, b) = (b, a)
    while b != 0:
        (a, b) = (b, a % b)
    return a


red_dice = sys.stdin.readline().rstrip().split()
blue_dice = sys.stdin.readline().rstrip().split()

win = 0
total = 36
for red in red_dice:
    for blue in blue_dice:
        if int(red) > int(blue):
            win += 1

gcd = gcd(win, total)
print(int(win/gcd),"/",int(total/gcd),sep='', end='')
