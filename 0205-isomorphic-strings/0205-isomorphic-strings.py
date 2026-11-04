class Solution(object):
    def isIsomorphic(self, s, t):
        if (len(s) != len(t)):
            return False
        mapping = {}
        for i,j in zip(s, t):
            mapping[i] = j
        if (len(set(mapping.values())) != len(mapping.values())):
            return False
        newStr = ''
        for i in s:
            newStr += mapping[i]
        if (newStr == t):
            return True
        else:
            return False