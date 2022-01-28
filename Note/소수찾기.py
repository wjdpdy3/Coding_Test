def is_prime_number(num):
    if num ==1 :
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

n = 10
print(is_prime_number(n))
