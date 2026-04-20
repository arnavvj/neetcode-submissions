class Solution:

    def hammingWeight(self, n: int) -> int:
        ans = 0

        while(n!=0):

            if n%2 == 1:
                ans += 1
                n -= 1
        
            n = int(n/2)

        return ans

    def countBits(self, n: int) -> List[int]:

        ans = []

        for i in range(n+1):

            if i == 0:
                ans.append(0)
            elif i == 1:
                ans.append(1)
            else:
                ans.append(self.hammingWeight(i))

        return ans
