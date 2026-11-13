class Solution(object):
    def strStr(self, haystack, needle):
        if needle in haystack:
            return haystack.index(needle)
        return -1
        for i in range(len(haystack)):
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
                else:
                    return i