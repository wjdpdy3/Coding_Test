n = int(input())
array=[]
for _ in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

array = sorted(array, key=lambda student:student[1]) # lambda 매개변수 : return값

for student in array:
    print(student[0], end=' ')
