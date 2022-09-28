class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif  x < 10:
            return True
        xList = []
        for i in str(x):
            xList.append(i)
        inv = xList[::-1]
        if xList == inv:
            return True
        else:
            return False
       