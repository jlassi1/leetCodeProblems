class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for index, num in enumerate(nums):
            if target-num in nums[index+1:]:
                new = nums[index+1:]
                return(index, new.index(target-num)+index+1)

      