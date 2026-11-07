class Solution(object):
    def grayCode(self, n):
        res = []
        for x in range(0, 2**n):
            res.append(x ^ (x >> 1))
        return res