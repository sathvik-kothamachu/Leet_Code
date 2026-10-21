class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n=len(nums)
        missing=n*(n+1)//2-sum(nums)
        return missing
        