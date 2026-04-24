"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        timeline = {}

        for i in intervals:

            s, e = i.start, i.end
            
            for j in range(s, e):
                try:
                    if timeline[j] == 1:
                        return False
                except KeyError:
                    timeline[j] = 1

        return True
                
