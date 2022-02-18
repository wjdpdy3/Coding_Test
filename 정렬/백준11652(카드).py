# https://www.acmicpc.net/problem/11652
import sys
input = sys.stdin.readline

n = int(input())
dict = {}

for _ in range(n):
    n = int(input())
    if n not in dict.keys():
        dict[n] = 1
    else:
        dict[n] += 1


# -를 사용하여 내림차순 정렬!!
s_dict = sorted(dict.items(), key=lambda item:(-item[1],item[0]))
print(s_dict[0][0])