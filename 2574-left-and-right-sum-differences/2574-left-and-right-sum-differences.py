class Solution:
    def arraySum(self, arry: List[int], reverse = False) -> List[int]:
        ArrySum = [0]
        if reverse:
            arry = arry [::-1]
        for idx, num in enumerate(arry):
            ArrySum.append((ArrySum[idx] + arry[idx]))
        if reverse:
            ArrySum = ArrySum [::-1]
        return ArrySum
    
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        lenth = len(nums)
        if lenth < 2 or not nums:
            return [0]
        
        leftSum, rightSum = self.arraySum(nums[:-1]), self.arraySum(nums[1:], reverse=True)

        answer = [0]*lenth
        for i in range(lenth):
            answer[i] = abs(leftSum[i] - rightSum[i])
        
        return answer
    
    
    