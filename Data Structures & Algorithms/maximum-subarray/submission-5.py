class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        ans = [nums[0]]

        max_sum = ans[-1]

        for i in range (1, len(nums)):
            ans.append(max(
                nums[i],
                ans[i-1] + nums[i]
            ))

            max_sum = max(max_sum, ans[-1])

        return max_sum