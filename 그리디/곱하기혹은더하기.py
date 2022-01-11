s = input()

result = int(s[0])
for i in range(1,len(s)):
    result = max(result+int(s[i]), result*int(s[i]))

print(result)


# <풀이>
# 두수 중에서 하나라도 0또는 1인경우 곱하기보다는 더하기를 수행하는것이 효율적이다
# for문 안의 코드를
# num = int(data[i])
# if num<=1 or result<=1:
#     result+=num
# else:
#     result *= num
