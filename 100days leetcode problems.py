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
