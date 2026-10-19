class Solution(object):
    def isPowerOfTwo(self, n):
        binary = bin(n).replace('0b', '')
        if (n>=0 and binary.count('1') == 1):
            return True
        else:
            return False