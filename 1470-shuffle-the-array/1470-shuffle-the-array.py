class Solution(object):
    def shuffle(self, nums, n):
        arr = []
        ind = 0
        for i in range(0, n):
            arr.append(nums[i])
            arr.append(nums[i+n])
        return arr