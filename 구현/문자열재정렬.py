s = input()
alphabet = list()
number = list()
for i in range(len(s)):
    if s[i]>='A' and s[i]<='Z':
        alphabet.append(s[i])
    else:
        number.append(int(s[i]))


alphabet.sort()
for i in range(len(alphabet)):
    print(alphabet[i],end='')
print(sum(number))

# 알파벳인지 확인할때 isalpha() 메소드 사용가능하다.
# '구분자'join(list) 함수 사용가능 => list 내에 값들을 구분자로 구분하여 하나의 문자열로 바꿔준다. 