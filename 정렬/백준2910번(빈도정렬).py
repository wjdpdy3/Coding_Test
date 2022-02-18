# https://www.acmicpc.net/problem/2910
import sys
input = sys.stdin.readline

n,c = map(int, input().split())
dict = {}
numbers = list(map(int, input().split()))
for number in numbers:
    if number in dict.keys():
        dict[number] += 1
    else:
        dict[number] = 1
s_dict = sorted(dict.items(), key=lambda item:-item[1])
for key, value in s_dict:
    for j in range(value):
        print(key, end=' ')