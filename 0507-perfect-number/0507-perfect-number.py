class Solution(object):
    def checkPerfectNumber(self, num):
        sum = 0
        for i in range(1, int(num**0.5) + 1):
            if (num % i == 0):
                sum += i
                if (i * i != num):
                    sum += num //i
        return sum - num == num