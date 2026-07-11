class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # [1,2,4,6]
        #      ^
        
        # [1,1,_,_]

        # [48,24,6,1]
        #  0,1,2,3 --> 4  
        
        left = [1]
        for i in range(1, len(nums)):
            left.append(left[-1] * nums[i-1])

        right = [1]
        for i in range(len(nums)-2, -1, -1):
            right = [nums[i+1] * right[0]] + right


        ans = []

        for i in range(0, len(nums)):
            ans.append(left[i] * right[i])

        return ans

        