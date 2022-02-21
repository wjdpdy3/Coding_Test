# https://www.acmicpc.net/problem/2295
n = int(input())

u = set()
for i in range(n):
    u.add(int(input()))
a_b_sums = set()
for i in u:
    for j in u:
        a_b_sums.add(i+j)

ans = set()
for i in u:
    for j in u:
        if (i-j) in a_b_sums:
           ans.add(i)
ans = sorted(ans, reverse=True)
print(ans[0])
