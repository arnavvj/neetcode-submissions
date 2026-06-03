class Solution:

    def recLengthOfLIS(self, prev, nums, start_i):

        if (prev, start_i) in self.lis:
            return self.lis[(prev, start_i)]

        ans = 0

        for i in range(start_i, len(nums)):

            if prev < nums[i]:

                count = 1 + self.recLengthOfLIS(
                    nums[i],
                    nums,
                    i + 1
                )

                ans = max(ans, count)

        self.lis[(prev, start_i)] = ans

        return ans


    def lengthOfLIS(self, nums: List[int]) -> int:

        self.lis = {}

        ans = 0

        for i in range(len(nums)):

            count = 1 + self.recLengthOfLIS(
                nums[i],
                nums,
                i + 1
            )

            ans = max(ans, count)

        return ans