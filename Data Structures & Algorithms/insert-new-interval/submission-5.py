class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # insert into main list
        intervals += [newInterval]

        # sort it wrt first number of every sub list
        intervals.sort(key=lambda x: x[0])

        # perform merge
        i = 0
        while(i < len(intervals)-1):

            if intervals[i][0] <= intervals[i+1][0] <= intervals[i][1]:

                intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
                _ = intervals.pop(i+1)

            else:
                i += 1

        return intervals