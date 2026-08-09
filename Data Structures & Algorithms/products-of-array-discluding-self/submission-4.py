class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left = [None for n in nums]
        left[0] = 1
        right = [None for n in nums]
        right[-1] = 1

        for i in range(1, len(nums)):
            
            left[i] = nums[i-1] * left[i-1]

            right[-1 - i] = nums[-i] * right[-i]

        ans = [l * r for l,r in zip(left, right)]
        
        return ans