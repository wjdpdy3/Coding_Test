data = input()

count = [0,0]

count[int(data[0])] += 1

for i in range(1,len(data)):
    if data[i]!=data[i-1]:
        count[int(data[i])]+=1

print(min(count[0], count[1]))
