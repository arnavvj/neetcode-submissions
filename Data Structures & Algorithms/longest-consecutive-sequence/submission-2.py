class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) < 2:
            return len(nums)

        _map = {}
        _starts = []

        for n in nums:
            try:
                _map[n] += 1
            except KeyError:
                _map[n] = 1

        for k in _map.keys():
            try:
                if _map[k-1]:
                    continue
            except KeyError:
                _starts.append(k)

        ans = 0
        for s in _starts:
            temp = s

            while(True):
                try:
                    if _map[temp+1]:
                        temp += 1
                except KeyError:
                    ans = max(ans, temp-s)
                    break

        return ans + 1


        

"""
  0   1    2   3    4   5   6   7
[ 2 , 20 , 4 , 10 , 3 , 4 , 5 ]
                    i
                                j


"""