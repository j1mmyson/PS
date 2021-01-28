num = int(input())

for i in range(num):
    testCase = input()
    loop = int(testCase[0])
    text = testCase[2:]
    for t in text:
        for i in range(loop):
            print(t, end='')
    print()