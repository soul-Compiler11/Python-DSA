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
"""

""" question 9: largest digit in a number 
n = 2594
largest = 0
while n > 0:
    digit = n % 10
    if digit > largest:
        largest = digit
    n //= 10
print("Largest disgit in the number is: ", largest) 
"""

"""question 10: smallest digit in a number
n = 2590
smallest = 9
while n > 0:
    digit = n % 10
    if digit < smallest:
        smallest = digit
    n //= 10
print("Smallest digit in the number is: ", smallest)
"""

"""question 11 : decimal to binary conversion 
n = 123
binary = ""
while n > 0:
    digit = n % 2
    binary = str(digit) + binary
    n //= 2
print("Binary conversion is : ", binary)
"""

"""queston 12: product of digit 

n = 1234
product = 1
while n > 0:
    digit = n % 10
    product *= digit
    n //= 10
print("product of digits in the number is : ", product)
"""

"""question 13: remove zero from a number in reverse order
n = 100002000300405
while n > 0:
    digit = n % 10
    if digit != 0:
        print(digit, end=" ")
    n //= 10
"""

"""question 14: lcm of two numbers

def lcmOfTwoNumbers(x, y):
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

num1 = 54
num2 = 24

print("The L.C.M. is", lcmOfTwoNumbers(num1, num2))
"""

"""question 15:  hcf of two numbers

def hcfOfTwoNumbers(x, y):
    if x < y:
        smaller = x
    else:
        smaller = y

    for i in range(1, smaller + 1):
        if (x % i == 0) and (y % i == 0):
            hcf = i
    return hcf

num1 = 45
num2 = 60
print("The hcf is", hcfOfTwoNumbers(num1, num2))
"""

"""question 16: check duck number or not
n = 1047
has_zero = False
while n > 0:
    digit = n % 10
    if digit == 0:
        has_zero = True
        print("duck")
        break
    n //= 10
"""
"""question 17: prime number or not
num = 407
if num == 0 or num == 1:
    print(num, "is not a prime number")
elif num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
else:
   print(num,"is not a prime number")
"""

""" question 18  binary to decimal conversion
n = 1101
decimal = 0
power = 0
while n > 0:
    digit = n % 10
    decimal += digit * (2 ** power)
    n //= 10
    power += 1
print("Decimal conversion is: ", decimal) 
"""

"""question 19: fibonacci series"""
n = 10
a, b = 0, 1
for i in range(n):
    print(a, end = " ")
    a, b = b, a + b
    