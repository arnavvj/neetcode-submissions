class Solution:

    def recJump(self, nums: List[int], start) -> bool:

        if start >= len(nums) - 1:
            return True

        if nums[start] == 0:
            return False

        for i in range(nums[start], 0, -1):

            possible = self.recJump(nums, start + i)

            if possible == True:
                return True

        return False


    def canJump(self, nums: List[int]) -> bool:
        
        start = 0
        
        if len(nums) <= 1:
            return True
        elif nums[start] == 0:
            return False


        for i in range(nums[start],  0, -1):

            possible = self.recJump(nums, start + i)

            if possible == True:
                return True

        return False

"""

[1, 2, 0, 1, 0]
 0  1  2  3  4
 ^ 
    
"""