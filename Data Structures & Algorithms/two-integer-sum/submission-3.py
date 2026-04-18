class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range (0, len(nums)-1):

            for j in range (i+1, len(nums)):

                if nums[i] + nums[j] == target:

                    if i < j:
                        return [i, j]
                    
                    else:
                        return [j, i]
"""

 [5, 6, 3, 4]
  ^
  0, 1, 2, 3


"""