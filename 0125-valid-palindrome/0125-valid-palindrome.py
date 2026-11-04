class Solution(object):
    def isPalindrome(self, s):
        r = ''
        for i in s:
            if (i.isalnum()):
                r += i
        r = r.lower()
        if (r == r[::-1]):
            return True
        else:
            return False