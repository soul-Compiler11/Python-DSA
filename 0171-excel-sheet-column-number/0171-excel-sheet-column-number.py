from string import ascii_uppercase as asc
class Solution(object):
    def titleToNumber(self, columnTitle):
        d = {asc[i]: i+1 for i in range(len(asc))}
        s = columnTitle[::-1]
        count = 0
        for i,j in enumerate(s):
            count += d[j]*(26**i)
        return count       