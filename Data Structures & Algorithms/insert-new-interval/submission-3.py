class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # Find loc to insert new interval
        i, j, insert = 0, 0, True
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
        if insert == True:
            intervals = intervals[:j] + [newInterval] + intervals[j:]

        else:
            k = j
            for i in range(j, len(intervals)):

                k = j
                if intervals[i][0] == newInterval[0]:
                    if intervals[i][1] > newInterval[1]:
                        break
                else:
                    break
            intervals = intervals[:k] + [newInterval] + intervals[k:]

        
        # merging process begins
        i = 0
        while(i < len(intervals) - 1):

            if intervals[i][0] <= intervals[i+1][0] <= intervals[i][1]:
                intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
                _ = intervals.pop(i+1)

            else:
                i += 1

        return intervals
            