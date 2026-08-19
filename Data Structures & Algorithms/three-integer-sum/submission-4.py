class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort(key = lambda x : x)
        ans = []

        for i in range (0, len(nums)-2):

            if i > 0:
                if nums[i] == nums[i-1]:
                    continue

            j, k = i+1, len(nums)-1
            
            while (j<k):
                change1, change2 = False, False
                if nums[i] + nums[j] + nums[k] == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    j +=1
                    k -= 1
                    change1, change2 = True, True
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                    change2 = True
                else:
                    j += 1
                    change1 = True
                
                while (change1 and j<k and nums[j-1] == nums[j]):
                    j += 1
                while (change2 and j<k and nums[k] == nums[k+1]):
                    k -= 1                
        
        return ans