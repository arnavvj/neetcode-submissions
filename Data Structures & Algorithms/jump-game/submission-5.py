class Solution:

    def recJump(self, nums, pos):

        if pos == len(nums) - 1:
            return True

        if self.jump_ind[pos] != None:
            return self.jump_ind[pos]

        ans = False

        for step in range(1, nums[pos]+1):

            ans = ans or self.recJump(nums, pos + step)
            if ans:
                break

        self.jump_ind[pos] = ans
        return ans

        
        

    def canJump(self, nums: List[int]) -> bool:

        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False

        self.jump_ind = [None for n in nums]

        ans = False

        i = 0

        for step in range(1, nums[i]+1):

            ans = ans or self.recJump(nums, i + step)
            if ans:
                return ans

        return ans
