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
# day 7 median of two sorted arrays
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merged = sorted(nums1 + nums2)
        n = len(merged)
        if n % 2 == 1:
            return merged[n // 2]
        else:
            mid1 = merged[n // 2 - 1]
            mid2 = merged[n // 2]
            return (mid1 + mid2) / 2.0
    