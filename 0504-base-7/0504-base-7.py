class Solution(object):
    def convertToBase7(self, num):
        result = ''
        n = num
        num = abs(num)
        if (num == 0): return '0'
        while (num > 0):
            rem = num%7
            result += str(rem)
            num = num // 7
        if (n<0):
            return '-' +result[::-1]
        else:
            return result[::-1]   