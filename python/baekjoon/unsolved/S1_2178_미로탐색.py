import sys

n, m = map(int, sys.stdin.readline().split())
n, m = n-1, m-1

data = sys.stdin.read().splitlines()
maze = []
for row in data:
    temp = []
    for i in row:
        temp.append(int(i))
    maze.append(temp)

print(maze)


start = [0, 0]
end = [n, m]