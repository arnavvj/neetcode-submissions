class Solution:

    def recRob(self, nums_) -> int:

        if len(nums_) == 0:
            return 0

        if len(nums_) == 1:
            self.robFrom[1] = nums_[0]
            return nums_[0]
        
        if len(nums_) == 2:
            self.robFrom[2] = max(nums_)
            return max(nums_)

        self_skip_rob = 0
        try:
            self_skip_rob = self.robFrom[len(nums_[1:])]
        except KeyError:
            self_skip_rob = self.recRob(nums_[1:])
            
        no_self_skip_rob = 0
        try:
            no_self_skip_rob = self.robFrom[len(nums_[2:])]
        except KeyError:
            no_self_skip_rob = self.recRob(nums_[2:])

        ans = max(
            nums_[0] + no_self_skip_rob,

            self_skip_rob
        )

        self.robFrom[len(nums_)] = ans

        return ans
        
    def rob(self, nums: List[int]) -> int:
        
        self.robFrom = {}

        return self.recRob(nums)