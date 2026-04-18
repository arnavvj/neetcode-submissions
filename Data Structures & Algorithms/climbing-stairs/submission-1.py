ways = {
    1: 1,
    2: 2
}

class Solution:

    def recClimb(self, i: int) -> int:

        try:

            return ways[i]

        except KeyError:

            ans = 0

            try:
                ans += ways[i-1]
            except KeyError:
                ans += self.recClimb(i-1)

            try:
                ans += ways[i-2]
            except KeyError:
                ans += self.recClimb(i-2)
            
            ways[i] = ans
        
            return ans



    def climbStairs(self, n: int) -> int:
        
        try:
            return ways[n]
        
        except KeyError:
            ans = 0

            try:
                ans += ways[n - 1]
            except KeyError:
                ans += self.recClimb(n - 1)
                
            try:
                ans += ways[n - 2]
            except KeyError:
                ans += self.recClimb(n - 2)

        
            return ans




"""

4
    3
        2
            1


4: 1,1,1,1 and 2,1,1 and 1,2,1 and 1,1,2 and 2,2

3: 1,1,1 and 2,1 and 1,2    ->3

2: 1,1 and 2                -> 2

1: 1                        -> 1
"""