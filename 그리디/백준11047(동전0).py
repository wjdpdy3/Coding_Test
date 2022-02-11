# https://www.acmicpc.net/problem/11047

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

coins.reverse()
cnt = 0
for coin in coins:
    if coin <= k:
        cnt += k // coin
        k %= coin

print(cnt)