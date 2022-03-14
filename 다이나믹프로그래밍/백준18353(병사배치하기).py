# https://www.acmicpc.net/problem/18353
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
decrease = [0]*n

for i in range(n):
    for j in range(i):
        if data[i] < data[j] and decrease[i] < decrease[j]:
            decrease[i] = decrease[j]
    decrease[i] += 1

print(n-max(decrease))
