# https://www.acmicpc.net/problem/18310
import sys
input = sys.stdin.readline

n = int(input())
houses = list(map(int, input().split()))
houses.sort()

print(houses[(n-1) // 2])
