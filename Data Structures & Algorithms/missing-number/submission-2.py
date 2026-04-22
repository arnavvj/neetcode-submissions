class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        exp = [i for i in range(len(nums) + 1)]

        return sum(exp) - sum(nums)