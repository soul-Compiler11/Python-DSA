"""
Question 1: check even or odd using concepts 
the last bit determine a number is even or odd.
even -> last bit = 0
odd -> last bit = 1
"""
n = 1235
if n & 1:
    print(f"{n} is even number")
else:
    print(f"{n} is odd")

"""
Question 2: swaping of two numbers using XOR 
"""
a = 24
b = 34 
a = a^b
b = a^b
a = a^b
print("a = ", a)
print("b =", b)

"""
Question 3: Finding the unique number using XOR
every number occur twice, except one number.
25325
find the number occur only once.
"""
arr = [2, 5, 3, 2, 5]
ans = 0
for num in arr:
    ans = ans ^ num
print("Unique number:", ans)