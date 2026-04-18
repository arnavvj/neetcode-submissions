class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) < 2:
            return 0

        i, j = 0, 1
        prof = float('-inf')

        while (j < len(prices)):
            
            if prices[j] > prices[i]:

                if prices[j] - prices[i] > prof:
                    prof = prices[j] - prices[i]
                
            else:
                i = j

            j += 1

        return prof if prof > 0 else 0

