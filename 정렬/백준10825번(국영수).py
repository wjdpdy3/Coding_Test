# https://www.acmicpc.net/problem/10825
import sys
input = sys.stdin.readline

n = int(input())
grades = []
for _ in range(n):
    name, korean, english, math = input().split()
    grades.append([name,int(korean),int(english),int(math)])
grades.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))

for grade in grades:
    print(grade[0])