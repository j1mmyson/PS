import sys

n = int(input())
fn = 1
for i in range(1, n+1):
    fn *= i

fn = str(fn)
answer = 0

while(fn != '' and fn[-1] == '0'):
    fn = fn[:-1]
    answer += 1

print(answer)