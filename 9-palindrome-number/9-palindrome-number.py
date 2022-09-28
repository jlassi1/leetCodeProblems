class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif  x < 10:
            return True
        y = str(x)
        xList = []
        for i in y:
            xList.append(i)
        if len(xList) %2 == 0:
            mid = len(xList)  // 2
            inv = xList[mid:]
            if xList[:mid] == inv[::-1]:
                return True
            else:
                return False
        else:
            mid = len(xList)  // 2
            inv = xList[mid+1:]
            if xList[:mid] == inv[::-1]:
                return True
            else:
                return False