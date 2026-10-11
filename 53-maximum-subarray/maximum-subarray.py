class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum=nums[0]
        left=0
        current_sum=0
        for right in range(len(nums)):
            if current_sum<0:
                current_sum=0
                left+=1
            current_sum+=nums[right]
            max_sum=max(max_sum,current_sum)
        return max_sum
            
        