"""
# day 6 roman to integer
class Solution(object):
    def romanToInt(self, s):
        res = 0
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        

        for i in range(len(s)):
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
                res -= values[s[i]]
            else:
                res += values[s[i]]

        return res
"""
"""
# day 7 median of two sorted arrays
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums = sorted(nums1 + nums2)
        n = len(nums)
        if n % 2 == 0:
            return (nums[n // 2 - 1] + nums[n // 2]) / 2.0
        else:
            return nums[n // 2]
"""
"""
# day 8 reverse integer
class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x *= sign
        reversed = 0

        while x != 0:
            digit = x % 10
            reversed = reversed * 10 + digit
            x //= 10

        reversed *= sign

        # Check for overflow
        if reversed < -2**31 or reversed > 2**31 - 1:
            return 0

        return reversed
"""
"""
# day 9 largest common prefix
class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        prefix = strs[0]

        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix
"""
"""
# day 10 integer to roman
class Solution(object):
    def intToRoman(self, num):
        values = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]

        Res = ""
        for value, symbol in values:
            while num >= value:
                Res += symbol
                num -= value

        return Res
"""

"""
# day 11 string to integer (atoi)

class Solution(object):
    def myAtoi(self, s):
        s = s.strip()
        if not s:
            return 0

        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        res = 0
        for char in s:
            if char.isdigit():
                res = res * 10 + int(char)
            else:
                break

        res *= sign

        # Clamp the result to the 32-bit signed integer range
        res = max(-2**31, min(res, 2**31 - 1))

        return res
"""
"""
# day 12 longest palindromic substring
class Solution(object):
    def longestPalindrome(self, s):
        def expandAroundCenter(s, left, right):
            substring = ""
            max_length = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_length:
                    max_length = right - left + 1
                    substring = s[left:right +1]
                left -=1
                right += 1
            return substring

        result = ''
        for i in range(len(s)):
            odd = expandAroundCenter(s, i, i)
            even = expandAroundCenter(s, i, i + 1)

            if len(odd) > len(result):
                result = odd
            if len(even) > len(result):
                result = even

        return result
"""

# day 13 single number
"""
class solution(object):
    def singleNumber(self, nums):
        ans = 0
        for num in nums:
            ans ^= num
        return ans
"""

# day 13 running sum of 1d array
"""
class Solution(object):
    def runningSum(self, nums):
        for i  in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
        return nums
"""

# day 13 shuffle the array
"""
class Solution(object):
    def shuffle(self, nums, n):
        arr = []
        for i in range(0, n):
            arr.append(nums[i])
            arr.append(nums[i+n])
        return arr
"""

# day 13 concatenation of array
"""
class Solution(object):
    def getConcatenation(self, nums):
        return nums + nums
"""

#  day 14 valid parenthesis
"""
class solution(object):
    def isValid(self, s):
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack
"""

# day 15 length of last word
"""
class Solution(object):
    def lengthOfLastWord(self, s):
        word = s.strip().split(' ')
        if not word:
            return 0
        return len(word[-1])
"""
# day 15 sqrt(x)
"""
class Solution(object):
    def mySqrt(self, x):
        if x < 2:
            return x

        left, right = 1, x // 2
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1

        return right
"""

# day 16 plus one
"""
class Solution(object):
  def plusOne(self, digits):
    n = len(digits)
    for i in range(n-1, -1, -1):
      if digits[i] < 9:
        digits[i] += 1
        return digits
      digits[i] = 0
    return [1] + digits
"""

# day 16 climbing stairs
"""
class Solution(object):
    def climbStairs(self, n):
        if n <= 2:
            return n
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b
"""

# day 17 sum of square of special elements
"""
class Solution(object):
    def sumOfSquares(self, nums):
        n = len(nums)
        total = 0
        for i in range(len(nums)):
            if n % (i + 1) == 0:
                total += nums[i] ** 2
        return total
"""

#  day 18 number of 1 bits
"""
class Solution(object):
    def hammingWeight(self, n):
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count
"""

# day 18 valid anagram
"""
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        counts = {}
        for char in s:
            counts [char] = counts.get(char, 0) + 1
        for char in t:
            if char not in counts or counts[char] == 0:
                return False
            counts[char] -= 1
        return True
"""

#  day 19 generate parenthesis
"""
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def backtrack(path, open_count, close_count):
            # Base case: a complete combination
            if len(path) == 2 * n:
                result.append(path)
                return

            if open_count < n:
                backtrack(path + "(", open_count + 1, close_count)

            if close_count < open_count:
                backtrack(path + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return result
"""

# day 19 happy number
"""
class solution(object):
    def isHappy(self, n):
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            total = 0
            while n > 0:
                digit = n % 10
                total += digit ** 2
                n //= 10
            n = total
        return True
"""

# day 20 excel sheet column title
"""
class Solution(object):
    def convertToTitle(self, columnNumber):
        capitals = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
        result = []
        while columnNumber > 0:
            result.append(capitals[(columnNumber-1)%26])
            columnNumber = (columnNumber-1) // 26
        result.reverse()
        return ''.join(result)
"""

# day 20 excel sheet coumn number
"""
from string import ascii_uppercase as asc
class Solution(object):
    def titleToNumber(self, columnTitle):
        d = {asc[i]: i+1 for i in range(len(asc))}
        s = columnTitle[::-1]
        count = 0
        for i,j in enumerate(s):
            count += d[j]*(26**i)
        return count
"""

#  day 21 add binary
"""
class Solution(object):
    def addBinary(self, a, b):
        return bin(int(a,2) + int(b,2)).replace('0b', '')
"""

# day 21 power of two
"""
class solution(object):
    def isPowerOfTwo(self, n):
        binary = bin(n).replace('0b', '')
        if (n>=0 and binary.count('1') == 1):
            return True
        else:
            return False
"""

# day 22 base 7
"""
class Solution(object):
    def convertToBase7(self, num):
        result = ''
        n = num
        num = abs(num)
        if (num == 0): return '0'
        while (num > 0):
            rem = num%7
            result += str(rem)
            num = num // 7
        if (n<0):
            return '-' +result[::-1]
        else:
            return result[::-1]
"""

# day 23 add digits
"""
class Solution(object):
    def SumOfDigits(num):
        summ = 0
        for i in str(num):
            summ += int(i)
        return summ
    def addDigits(self, num):
        while(len(str(num)) != 1):
            num = self.SumOfDigits(num)
        return num
"""

# day 24 missing number
"""
class Solution(object):
    def missingNumber(self, nums):
        nums_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in nums_set:
                return number
"""

#  day 25 count days spent together
class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        start = max(arriveAlice, arriveBob)
        end = min(leaveAlice, leaveBob)
        if start > end:
            return 0
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def day_of_year(date):
            month, day = map(int, date.split('-'))
            return sum(days[:month-1]) + day
        return day_of_year(end) - day_of_year(start) + 1