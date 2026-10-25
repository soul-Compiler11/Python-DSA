class Solution(object):
    def countPrimes(self, n):
        truth = [True] * n

        if n < 2:
            return 0

        truth[0], truth[1] = False, False

        i = 2
        while i * i < n:
            if truth[i]:
                for j in range(i * i, n, i):
                    truth[j] = False
            i += 1

        return truth.count(True)