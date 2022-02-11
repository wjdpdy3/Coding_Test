# https://www.acmicpc.net/problem/11399

n = int(input())
p = list(map(int, input().split()))

p.sort()
sum = 0
result = 0
for person in p:
    sum += person
    result += sum
print(result)