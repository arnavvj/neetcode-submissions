class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        map = {}
        for n in nums:
            map[n] = 1
        
        starts = []
        for n in nums:
            if n-1 not in map:
                starts.append(n)

        ans = 0
        for s in starts:
            l = 1
            next = s+1
            while(True):
                if next in map:
                    l += 1
                    next += 1
                else:
                    ans = max(ans, l)
                    break
        
        return ans





        
