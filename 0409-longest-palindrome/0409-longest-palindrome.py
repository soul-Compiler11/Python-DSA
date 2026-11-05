class Solution(object):
    def longestPalindrome(self, s):
        length = 0
        count = {}
        for i in s:
            if (i not in count):
                count[i] = 1
            else:
                count[i] += 1
        for k,v in count.items():
            length += v // 2 * 2
            if (length % 2 == 0 and v % 2 == 1):
                length += 1
        return length