class Solution(object):
    def numOfSubarrays(self, arr):
        res = 0
        prefixsum = 0
        odd = 0
        even = 1
        for num in arr:
            prefixsum += num
            if prefixsum % 2 == 0:
                res += odd
                even += 1
            else:
                res += even
                odd += 1
        return res % (10**9 + 7)   