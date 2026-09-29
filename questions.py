"""
Question 1: check even or odd using concepts 
the last bit determine a number is even or odd.
even -> last bit = 0
odd -> last bit = 1

n = 1235
if n & 1:
    print(f"{n} is even number")
else:
    print(f"{n} is odd")

"""
"""
Question 2: swaping of two numbers using XOR 

a = 24
b = 34 
a = a^b
b = a^b
a = a^b
print("a = ", a)
print("b =", b)
"""
"""
Question 3: Finding the unique number using XOR
every number occur twice, except one number.
25325
find the number occur only once.

arr = [2, 5, 3, 2, 5]
ans = 0
for num in arr:
    ans = ans ^ num
print("Unique number:", ans)
"""
"""
question 4: sum of digits

n = 1234
total = 0
while n > 0:
    total += n % 10
    n //= 10
print("Sum of digits:", total)
"""

"""question 5: reverse a number

n = 1234
reverse = 0 
while n > 0 :
    digt = n % 10
    reverse = reverse*10 + digt
    n //= 10
print("Reverse of number:", reverse)
"""

"""question 6: check palindrome number

n = 12321
original = n
reverse = 0
while n > 0:
    digit = n % 10 
    reverse = reverse*10 +digit
    n //=10
if original == reverse:
    print(f"{original} is a palindrome number")
else:
    print(f"{original} is not a palindrome number")
"""

"""question 7: count the number of digits in a number

n = 1234
count = 0
while n > 0 :
    n //= 10
    count +=4
print("Number of digits:", count)
"""

"""queston 8: check armstrong number
"""
n = 153
original = n
total = 0
while n > 0:
    digit = n % 10
    total += digit ** 3
    n //= 10
if original == total:
    print(f"{original} is an armstrong number")
else:
    print(f"{original} is not an armstrong number")
