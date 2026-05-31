class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        i, j = 0, len(nums)-1

        while(i < j-1):

            mid = (i+j) // 2

            target = min(nums[i], nums[mid], nums[mid+1], nums[j])

            # go left
            if nums[i] == target or nums[mid] == target:
                j = mid

            # go right
            else:
                i = mid + 1

        return min(nums[i], nums[j])

