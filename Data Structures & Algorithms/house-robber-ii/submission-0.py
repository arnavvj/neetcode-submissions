class Solution:

    def robRange(self, i, j) -> int:
        ans = 0

        if i > j:
            return 0        
        elif i == j:
            return self.rob_hist[f"{i}_{j}"]


        elif i+1 == j:
            ans = max(self.nums[i], self.nums[j])
        else:
            try:
                with_i = self.rob_hist[f"{i+2}_{j}"]
            except KeyError:
                with_i = self.robRange(i+2, j)
            try:
                wo_i = self.rob_hist[f"{i+1}_{j}"]
            except KeyError:
                wo_i = self.robRange(i+1, j)
            ans = max(
                self.nums[i] + with_i,
                wo_i
            )
        
        self.rob_hist[f"{i}_{j}"] = ans
        return ans


    def rob(self, nums: List[int]) -> int:

        j = len(nums) - 1
        self.nums = nums
        self.rob_hist = {}

        for i, n in enumerate(nums):
            self.rob_hist[f"{i}_{i}"] = n

        try:
            with_0 = self.rob_hist[f"{2}_{j-1}"]
        except KeyError:
            with_0 = self.robRange(2, j-1)

        try:
            wo_0 = self.rob_hist[f"{1}_{j}"]
        except KeyError:
            wo_0 = self.robRange(1, j)

        ans = max(
            nums[0] + with_0,

            wo_0
        )
        
        return ans


"""


  i              j
[ 2 , 9 , 8 , 3, 6 ]
                 [ 2 , 9 , 8 , 3, 6 ]

 
"""