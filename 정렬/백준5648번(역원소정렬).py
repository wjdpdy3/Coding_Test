# https://www.acmicpc.net/problem/5648
import sys
input = sys.stdin.readline
sentence = list(input().split())
n = int(sentence[0])
if len(sentence)>1:
    numbers = sentence[1:]
cnt = len(sentence)-1

while True:
    if cnt==n:
        break
    sentence = list(input().split())
    for s in sentence:
        numbers.append(s)
    cnt += len(sentence)


for i in range(len(numbers)):
    numbers[i] = "".join(reversed(numbers[i]))
    numbers[i] = int(numbers[i].lstrip('0'))
numbers.sort()
for number in numbers:
    print(number)

