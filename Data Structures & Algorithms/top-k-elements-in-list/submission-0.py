class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
        occ = {}
        for n in nums:
            try:
                occ[n] += 1
            except KeyError:
                occ[n] = 1

        ranks = sorted(occ.items(), key = lambda x : x[1], reverse = True)

        return [ranks[r][0] for r in range (k)]