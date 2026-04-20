class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            # bin(i) :  built-in utility that converts in -> binary representation 
            #           returns as a string
            
            ans.append(bin(i).count('1'))

        return ans