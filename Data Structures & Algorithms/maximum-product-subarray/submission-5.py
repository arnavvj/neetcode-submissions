class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        mins = [1 for n in nums]
        maxs = [1 for n in nums]

        mins[-1] = nums[-1]
        maxs[-1] = nums[-1]

        ans = nums[-1]

        for i in range(len(nums)-2, -1, -1):
            mins[i] = min(
                nums[i],
                nums[i] * mins[i+1],
                nums[i] * maxs[i+1]
            )

            maxs[i] = max(
                nums[i],
                nums[i] * mins[i+1],
                nums[i] * maxs[i+1]
            )

            ans = max(
                ans,
                mins[i],
                maxs[i]
            )

        return ans

