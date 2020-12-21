import sys

def gcd(a, b): # 최대공약수
    if a < b:
        (a, b) = (b, a)
    while b != 0:
        (a, b) = (b, a % b)
    return a

[so, people] = sys.stdin.readline().rstrip().split(' ')
so, people = int(so), int(people)

so = so % people

gcd = gcd(so, people)

answer = people - gcd
print(answer)

