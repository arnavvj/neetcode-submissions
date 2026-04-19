class Solution:
    def recurrCheck(self, nums, target):
        
        ans = []

        for i,n in enumerate(nums):
            
            if target - n > 0:
                #print(nums, n, target)
                comb = self.recurrCheck(nums[i:], target - n)
                #print(comb)
                if comb:
                    for c in comb:
                        c.append(n)
                        ans.append(c)
                else:
                    continue

            elif target - n == 0:
                #print(nums, n, target)
                comb = [n]
                #print(comb)
                ans.append(comb)

            else:
                #print(nums, n, target)
                #print("deadend")
                continue
        
        #print("ans:", ans)
        return ans
        

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        ans = []

        for i,n in enumerate(nums):
            if target - n > 0:
                #print(nums, n, target)
                comb = self.recurrCheck(nums[i:], target - n)
                #print(comb)
                if comb:
                    for c in comb:
                        c.append(n)
                        ans.append(c)
                else:
                    continue

            
            elif target - n == 0:
                #print(nums, n, target)
                comb = [n]
                #print(comb)
                ans.append(comb)

            else:
                #print(nums, n, target)
                #print("deadend")
                continue

        #print("ANS:", ans)
        return ans

