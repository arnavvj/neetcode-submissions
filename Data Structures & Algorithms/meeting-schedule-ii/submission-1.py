"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        intervals.sort(key=lambda x: (x.start, x.end))

        rooms = {}

        ans = 0

        for i in intervals:

            add = True

            # check all rooms and find which can injest incoming slot
            for j in range(ans):
                # conflict detected in this room, check the next
                if rooms[j].start <= i.start < rooms[j].end:
                    pass

                # no conflict
                else:
                    rooms[j] = i
                    add = False
                    break

            # if no replacement, add = True
            if add:
                rooms[ans] = i
                ans += 1

        return ans