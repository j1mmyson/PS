import sys

def getNumberOfSide(n):
    three = 4
    one = (n-2)*(n-2) + (n-2)*(n-1)*4

    two = (2*n-3)*4

    return one, two, three

def getMinOfSum(dice):
    a, b, c, d, e, f = [i for i in dice]
    mOne = min(dice)
    mTwo = min([a+b, a+c, a+d, a+e, c+e, e+d, d+b, b+c, f+c, f+b, f+e, f+d])
    mThree = sum(dice)
    for i in [0, 5]:
        for j in [1, 4]:
            for k in [2, 3]:
                mThree = min(mThree, dice[i]+dice[j]+dice[k])
    return mOne, mTwo, mThree

n = int(sys.stdin.readline().rstrip())
dice = sys.stdin.readline().rstrip().split(' ')
for i, v in enumerate(dice):
    dice[i]= int(v)

if n == 1:
    answer = sum(dice)
    print(answer - max(dice))
else:
    one, two, three = getNumberOfSide(n)
    mOne, mTwo, mThree = getMinOfSum(dice)
    answer = one*mOne + two*mTwo + three*mThree 

    print(answer)