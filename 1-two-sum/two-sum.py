class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dic={}

        for index,num in enumerate(nums):
            dic[num]=index

        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in dic and dic[diff]!=i:
                return [i, dic[diff]]
        return [] 
        
        