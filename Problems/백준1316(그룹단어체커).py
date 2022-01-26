n = int(input())
cnt = 0

for _ in range(n):
    sentence = input()
    check = True
    for i in range(len(sentence)-1):
        if sentence[i] != sentence[i+1]:
            if sentence[i] in sentence[i+1:]:
                check = False
    if check:
        cnt+=1

print(cnt)
