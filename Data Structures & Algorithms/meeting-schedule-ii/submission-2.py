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

        # room number : interval
        rooms = {}

        # room number and answer
        ans = 0

        for i in intervals:

            # for every interval decide whether to add or adjust
            add = True

            # check all rooms and find which can injest incoming slot
            for j in range(ans):
                # conflict detected in this room, check the next
                if rooms[j].start <= i.start < rooms[j].end:
                    pass

                # no conflict found for a room. Insert slot and break
                else:
                    rooms[j] = i
                    add = False
                    break

            # if no replacement, then add = True, else skip
            if add:
                rooms[ans] = i
                ans += 1

        return ans