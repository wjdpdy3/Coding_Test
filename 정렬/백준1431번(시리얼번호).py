# https://www.acmicpc.net/problem/1431

def sum_numbers(x):
    s=0
    for i in range(len(x)):
        if 48 <= ord(x[i]) <= 57:
            s += int(x[i])
    return s

n = int(input())
serials = []
for _ in range(n):
    serials.append(input())

serials.sort(key=lambda x:(len(x), sum_numbers(x),x))

for s in serials:
    print(s)
