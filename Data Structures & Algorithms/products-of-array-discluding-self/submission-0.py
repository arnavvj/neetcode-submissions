class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans = []

        count_0, pdt_non_0 = 0, 1

        for n in nums:
            if n == 0:
                count_0 += 1
            else:
                pdt_non_0 *= n


        if count_0 == 0:
            for n in nums:
                ans.append(int(pdt_non_0 / n))

        elif count_0 == 1:
            for n in nums:
                if n == 0:
                    ans.append(pdt_non_0)
                else:
                    ans.append(0)

        else:
            for n in nums:
                ans.append(0)

        
        return ans