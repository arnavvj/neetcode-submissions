class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1


        while(l <= r):

            m = (l + r) // 2

            if nums[m] == target:
                return m

            
            if nums[l] <= target < nums[m]:
                r = m - 1
            elif nums[m] < target <= nums[r]:
                l = m + 1
            else:
                break

        return -1
"""
[0, 1,2,3,4,5]
[-1,0,2,4,6,8], target = 4
 l    m     r

[0, 1,2,3,4,5]
[-1,0,2,4,6,8], target = 4
        l m r

[0, 1,2,3,4,5]
[-1,0,2,4,6,8], target = 4
        lr
"""


"""

[ 0,1,2,3,4,5]
[-1,0,2,4,6,8] target=3
  l   m     r


[ 0,1,2,3,4,5]
[-1,0,2,4,6,8] target=3
        l m r



"""