class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda x: (x[0], x[1]) )

        ans = 0

        if len(intervals) == 0:
            return ans

        i = 1
        while (i < len(intervals)):

            # case [1,2] [1,4] [2,5] 
            # remove [1,4] bc after sort, it has higher chance of merging with next
            # since we've to remove minimum, we remove the worst 
            # i.e. once it goes remaining are more likely to gel well with e/o
            if intervals[i-1][0] <= intervals[i][0] < intervals[i-1][1]:
                if intervals[i-1][1] <= intervals[i][1]:
                    intervals.pop(i)
                else:
                    intervals.pop(i-1)
                ans += 1
                

            # case [1,2] [2,3] OR [1,2] [4,5] 
            # good to go
            elif intervals[i-1][0] <= intervals[i][0] >= intervals[i-1][1]:
                i += 1

        return ans


"""
Cases after sorting:

    i-1     |-------------|
    i       |------------------|


    i-1     |-------------|
    i           |-------------|


    i-1     |-------------|
    i               |-----|


    i-1     |-------------|
    i           |-----|

"""



