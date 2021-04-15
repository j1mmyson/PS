import sys

global x
global y
global xx

x = {'A': 0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7}
xx = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
y = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def kingMove(king, stone, m):
    global x
    global xx
    global y

    kx = king[0]
    ky = int(king[1])

    if m == 'R':
        pass
    elif m == 'L':
        pass
    elif m == 'B':
        pass
    elif m == 'T':
        pass
    elif m == 'RT':
        pass
    elif m == 'LT':
        pass
    elif m == 'RB':
        pass
    elif m == 'LB':
        pass

def stoneMove(stone, m):


[king, stone, t] = sys.stdin.readline().rstrip().split(' ')

t = int(t)