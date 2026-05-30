class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x: (x[0], x[1]))

        ans = 0

        if len(intervals) == 0:
            return ans

        i = 1
        while i < len(intervals):

            # overlap case
            if intervals[i - 1][0] <= intervals[i][0] < intervals[i - 1][1]:

                # remove the interval with the larger end
                if intervals[i - 1][1] <= intervals[i][1]:
                    intervals.pop(i)
                    ans += 1

                    # do NOT increment i
                    # because new intervals[i] must be compared with intervals[i-1]

                else:
                    intervals.pop(i - 1)
                    ans += 1

                    # do NOT increment i here either
                    # after popping i-1, old intervals[i] shifts left
                    # now it is at intervals[i-1], so we need to compare again

                    if i > 1:
                        i -= 1

            # no overlap case
            elif intervals[i - 1][0] <= intervals[i][0] >= intervals[i - 1][1]:
                i += 1

        return ans