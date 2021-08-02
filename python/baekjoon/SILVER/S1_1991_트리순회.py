import sys

def preOrder(node):
    print(node, end='')
    if d[node][0] != '.':
        preOrder(d[node][0])
    if d[node][1] != '.':
        preOrder(d[node][1])
    return


def inOrder(node):
    if d[node][0] != '.':
        inOrder(d[node][0])
    print(node, end='')
    if d[node][1] != '.':
        inOrder(d[node][1])
    return


def postOrder(node):
    if d[node][0] != '.':
        postOrder(d[node][0])
    if d[node][1] != '.':
        postOrder(d[node][1])
    print(node, end='')
    return


num = int(input())
d = {}

for _ in range(num):
    root, left, right = sys.stdin.readline().split()
    d[root] = [left, right]

preOrder('A')
print()
inOrder('A')
print()
postOrder('A')
