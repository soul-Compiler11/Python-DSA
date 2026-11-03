class Solution(object):
    def minMoves(self, nums):
        mx = max(nums)
        return sum(mx - x for x in nums) 