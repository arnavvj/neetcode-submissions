class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left, right = [1], [1]

        for i in range (1, len(nums)):

            left.append(nums[i-1] * left[-1])
            
            right = [nums[len(nums) - i] * right[0]] + right


        for i in range (0,len(left)):
            left[i] *= right[i]

        return left


        

"""

right =  [ 120 60 20 5 1 ]

nums =   [ 1 2 3 4 5  ]

left =   [ 1 1 2 6 24 ]

"""