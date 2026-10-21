

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)

        if n == 0:
            return

        k %= n

        nums[n-k:] = reversed(nums[n-k:])
        nums[:n-k] = reversed(nums[:n-k])
        nums.reverse()
