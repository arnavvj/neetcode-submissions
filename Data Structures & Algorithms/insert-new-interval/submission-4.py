class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # Find loc to insert new interval
        i, j = 0, 0
        while(True):
            
            try:

                if intervals[i][0] > newInterval[0]:
                    j = i
                    break
                elif intervals[i][0] == newInterval[0]:
                    j = i
                    insert = False
                    break

                i += 1
                if i == len(intervals):
                    j = i
                    break

            except IndexError:
                break

        # insert new interval
        intervals = intervals[:j] + [newInterval] + intervals[j:]

        
        # merging process begins
        i = 0
        while(i < len(intervals) - 1):

            if intervals[i][0] <= intervals[i+1][0] <= intervals[i][1]:
                intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
                _ = intervals.pop(i+1)

            else:
                i += 1

        return intervals
            