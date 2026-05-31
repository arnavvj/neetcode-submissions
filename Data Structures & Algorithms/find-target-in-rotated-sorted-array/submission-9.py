class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        i = 0
        j = len(nums) - 1

        while (i<=j):

            m = (i+j)//2

            if nums[m] == target:
                return m
            if i == j:
                break

            # FIRST LETS CHECK LEFT
            if nums[i] <= nums[m]:   # normal situation

                if nums[i] <= target <= nums[m]:  # found slot, move left
                    j = m
                    continue
                else:
                    i = m+1

            else:   # left is rotated
                
                # in rotated, if target can either be lesser than both or greater than both; 
                # then this is the place to be
                if nums[i] >= nums[m] >= target or target >= nums[i] >= nums[m]:
                    j = m
                    continue
                else:   # move to the other side
                    i = m+1


            # NEXT CHECK RIGHT
            if nums[m+1] <= nums[j]: # normal situation

                if nums[m+1] <= target <= nums[j]:  # found slot, move right
                    i = m+1
                    continue
                else:
                    j = m

            else:   # right is rotated
                
                # in rotated, if target can either be lesser than both or greater than both; 
                # then this is the place to be
                if nums[m+1] >= nums[j] >= target or target >= nums[m+1] >= nums[j]:
                    i = m+1
                    continue
                else:   # move to the other side
                    j = m


        return -1





"""
i        m        j
4, 5, 6, 7, 0, 1, 2

0  1  2  3  4  5  6


"""