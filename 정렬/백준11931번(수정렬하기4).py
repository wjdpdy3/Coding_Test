# https://www.acmicpc.net/problem/11931
import sys
input = sys.stdin.readline

n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))
numbers.sort(reverse=True)

for number in numbers:
    print(number)
