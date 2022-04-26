import sys
input = sys.stdin.readline

n = int(input())
cords = []
for _ in range(n):
    cords.append(list(map(int, input().split())))

cords.sort()

result = []
x, y = cords[0]
for i in range(1, n):
    c_x, c_y = cords[i]
    if c_x <= y:
        y = max(y, c_y)

    else:
        result.append([x, y])
        x, y = cords[i]

result.append([x, y])
answer = 0
for r in result:
    answer += abs(r[0] - r[1])

print(answer)
