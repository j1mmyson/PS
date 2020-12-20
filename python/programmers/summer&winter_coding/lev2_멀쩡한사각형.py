def gcd(a, b): # 최대공약수
    if a < b:
        (a, b) = (b, a)
    while b != 0:
        (a, b) = (b, a % b)
    return a

def solution(w,h):
    gcd_var = gcd(w, h)
    
    return w*h - (w + h - gcd_var)