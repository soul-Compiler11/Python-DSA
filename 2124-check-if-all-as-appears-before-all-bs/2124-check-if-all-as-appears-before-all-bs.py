class Solution(object):
    def checkString(self, s):
        found_b = False
        for char in s:
            if char == 'b':
                found_b = True
            elif char == 'a' and found_b:
                return False
        return True