# https://www.acmicpc.net/problem/11501
# 1. 주식 하나를 산다.
# 2. 원하는 만큼 가지고 있는 주식을 판다.
# 3. 아무것도 안한다.


import sys
input = sys.stdin.readline


T = int(input())

for _ in range(T):
    day = int(input())
    data = list(map(int, input().split()))

    value = 0
    max = 0
    for i in range(day-1, -1, -1):
        if data[i] > max:
            max = data[i]
        else:
            value += max-data[i]
    print(value)