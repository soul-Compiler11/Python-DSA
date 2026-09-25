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