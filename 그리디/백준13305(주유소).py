# https://www.acmicpc.net/problem/13305
import sys
input = sys.stdin.readline

city = int(input())
roads = list(map(int, input().split()))
costs = list(map(int, input().split()))

result = 0
min_cost = costs[0]

for i in range(city-1):
    if costs[i] < min_cost:
        min_cost = costs[i]
    result += min_cost * roads[i]
print(result)
