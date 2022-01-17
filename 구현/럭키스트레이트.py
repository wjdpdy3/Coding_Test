n = input()
left_sum = 0
right_sum = 0

for i in range(int(len(n)/2)):
    left_sum+=int(n[i])
    right_sum+=int(n[i+int(len(n)/2)])

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")


