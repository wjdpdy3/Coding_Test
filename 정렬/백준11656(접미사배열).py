# https://www.acmicpc.net/problem/11656

s = input()
data = []
for i in range(len(s)):
    data.append(s[i:])
for d in sorted(data):
    print(d)
