class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        nums_sum = sum(nums)

        high = len(nums)
        expected = high * (high+1) / 2

        return int(expected - nums_sum)