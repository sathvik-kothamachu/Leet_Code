class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        count=0
        max_con=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            else:
                max_con=max(max_con,count)
                count=0
        max_con=max(max_con,count)
        return max_con
        