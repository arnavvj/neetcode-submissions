class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans = [[]]

        for n in nums:
            temp = []
            
            for a in ans:

                temp.append(a + [n]) # list

            ans  += temp

        return ans
        