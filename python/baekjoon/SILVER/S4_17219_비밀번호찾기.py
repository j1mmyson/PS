import sys

n, m = map(int, sys.stdin.readline().split())

d = {}

for _ in range(n):
    url, pw = sys.stdin.readline().split()
    d[url] = pw

for _ in range(m):
    url = sys.stdin.readline().strip()
    print(d[url])