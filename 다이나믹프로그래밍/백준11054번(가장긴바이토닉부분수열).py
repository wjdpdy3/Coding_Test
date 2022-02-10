# https://www.acmicpc.net/problem/11054

n = int(input())
s = list(map(int, input().split()))

increase = [0 for _ in range(n)]
decrease = [0 for _ in range(n)]
result = [0 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if s[i] > s[j] and increase[i] < increase[j]:
            increase[i] = increase[j]
    increase[i] += 1

for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if s[i] > s[j] and decrease[i] < decrease[j]:
            decrease[i] = decrease[j]
    decrease[i] += 1

for i in range(n):
    increase[i] = increase[i] + decrease[i] -1
print(max(increase))

