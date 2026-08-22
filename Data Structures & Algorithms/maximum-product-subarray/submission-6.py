
"""

[ -2, 4, 3, -5]

 -24 -60 -15 -5      min
120  12   3    -5      max
        


"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        
        minmem = [None for n in nums]
        maxmem = [None for n in nums]

        minmem[-1] = nums[-1]
        maxmem[-1] = nums[-1]

        ans = max(minmem[-1], maxmem[-1])

        for i in range(len(nums) - 2, -1, -1):
            
            minmem[i] = min(
                nums[i],
                nums[i] * minmem[i+1],
                nums[i] * maxmem[i+1]
            )

            maxmem[i] = max(
                nums[i],
                nums[i] * minmem[i+1],
                nums[i] * maxmem[i+1]
            )

            ans = max(
                ans,
                minmem[i],
                maxmem[i]
            )

        return ans



        