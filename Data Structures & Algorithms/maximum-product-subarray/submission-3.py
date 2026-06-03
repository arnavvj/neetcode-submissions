class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        ans = float('-inf')
        n = len(nums)

        for i in range(n):

            ans = max(ans, nums[i])
            pdt = nums[i]

            for j in range(i+1, n):
                pdt *= nums[j]
                ans = max(ans, pdt)

        return ans


        