class Solution(object):
    def findTheDifference(self, s, t):
        count_s, count_t = 0, 0
        for i in s:
            count_s += ord(i)
        for i in t:
            count_t += ord(i)
        return chr(count_t - count_s)    