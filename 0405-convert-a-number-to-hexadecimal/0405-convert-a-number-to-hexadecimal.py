class Solution(object):
    def toHex(self, num):
        if num == 0:
            return "0"
        characters = "0123456789abcdef"
        result = ""
        while num < 0:
            num += 2**32
        while num > 0:
            result = characters[num % 16] + result
            num //= 16
        return result