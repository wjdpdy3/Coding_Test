# https://www.acmicpc.net/problem/2565

n = int(input()) # 전깃줄의 개수
data = []
dp = [0 for _ in range(n)]
for _ in range(n):
    data.append(list(map(int, input().split())))
data.sort(key=lambda x:x[0])
new_data = [i[1] for i in data]

for i in range(n):
    for j in range(i):
        if new_data[i] > new_data[j] and dp[i]<dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(n-max(dp))

