class Solution:
    def find(self, nums, target):
        res = []
        i, j = 0, len(nums) - 1

        while i < j:
            total = nums[i] + nums[j]

            if total == target:
                res.append([nums[i], nums[j]])

                # Skip duplicate left values
                while i < j and nums[i] == nums[i + 1]:
                    i += 1

                # Skip duplicate right values
                while i < j and nums[j] == nums[j - 1]:
                    j -= 1

                i += 1
                j -= 1

            elif total < target:
                i += 1
            else:
                j -= 1

        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []

        nums.sort()

        i = 0
        while i < len(nums) - 2:
            # Skip duplicate nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue

            pairs = self.find(nums[i + 1:], -nums[i])

            for pair in pairs:
                pair.append(nums[i])
                ans.append(pair)

            i += 1

        return ans




"""

[-1,0,1,2,-1,-4]

  0.  1.  2. 3. 4. 5.  len = 6
[-4, -1, -1, 0, 1, 2]


"""