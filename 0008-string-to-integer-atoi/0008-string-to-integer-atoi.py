import re
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