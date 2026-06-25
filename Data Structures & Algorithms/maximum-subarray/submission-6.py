class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        msa = [0 for n in nums]
        msa[-1] = nums[-1]

        ans = msa[-1]

        for i in range(len(nums)-2, -1, -1):

            msa[i] += max(
                nums[i],
                nums[i] + msa[i+1]
            )

            ans = max(ans, msa[i])

        return ans
        