class Solution(object):
    def SumOfDigits(self, num):
        summ = 0
        for i in str(num):
            summ += int(i)
        return summ
    def addDigits(self, num):
        while len(str(num)) != 1:
            num = self.SumOfDigits(num)
        return num
        