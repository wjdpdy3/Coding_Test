# https://www.acmicpc.net/problem/1541

s = input()
num = ""
result = 0
op = '+'
for i in range(len(s)):
    if s[i] == '+':
        if op == '+':
            result += int(num)
            num = ""
        elif op == '-':
            result -= int(num)
            num = ""
        continue
    elif s[i] == '-':
        if op == '+':
            result += int(num)
            num = ""
        elif op == '-':
            result -= int(num)
            num = ""
        op = '-'
        continue
    num += s[i]
if op == '+':
    result += int(num)
elif op == '-':
    result -= int(num)
print(result)