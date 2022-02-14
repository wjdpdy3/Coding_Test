# https://www.acmicpc.net/problem/2847

n = int(input())
scores = []
for _ in range(n):
    scores.append(int(input()))
scores.reverse()

result = 0
for i in range(1, n):
    if scores[i] >= scores[i-1]:
        target = scores[i-1]-1
        result += scores[i] - target
        scores[i] = target

print(result)