class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        overallSum = 0
        n = len(nums)
        for i in range(n + 1):
            overallSum += i
        return overallSum - sum(nums)