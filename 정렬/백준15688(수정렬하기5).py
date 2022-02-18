# https://www.acmicpc.net/problem/15688
import sys
input = sys.stdin.readline

n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))
numbers.sort()
for n in numbers:
    print(n)

