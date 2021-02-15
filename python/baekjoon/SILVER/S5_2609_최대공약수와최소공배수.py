def gcd(a, b):
    gcdNum = 0
    for i in range(1, a+1):
        if (a%i == 0) and (b%i == 0):
            gcdNum = i
    return gcdNum
    

def lcm(a, b):
    return a * b // gcd(a,b)

a, b = map(int, input().split())

if a > b:
    temp = a
    a = b
    b = temp

print(gcd(a, b), lcm(a, b))
