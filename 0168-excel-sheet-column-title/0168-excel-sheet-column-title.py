class Solution(object):
    def convertToTitle(self, columnNumber):
        capitals = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
        result = []
        while columnNumber > 0:
            result.append(capitals[(columnNumber-1)%26])
            columnNumber = (columnNumber-1) // 26
        result.reverse()
        return ''.join(result)