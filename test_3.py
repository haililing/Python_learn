def is_palindrome(n):
    a , b = 0 , n
    while n > 0:
        a = a * 10 + n % 10
        n = n // 10

    return a == b

output = filter(is_palindrome, range(1,100))
print(list(output))
