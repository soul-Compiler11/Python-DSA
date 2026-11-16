class Solution(object):
    def digitSum(self, s, k):
        while len(s) > k:
            new_s = ""
            for i in range(0, len(s), k):
                group = s[i:i+k]
                group_sum = sum(int(digit) for digit in group)
                new_s += str(group_sum)
            s = new_s
        return s