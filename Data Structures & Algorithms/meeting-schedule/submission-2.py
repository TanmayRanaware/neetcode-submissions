"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # o(n) for mapping and o(nlogn) for sorting
        intervals=sorted(map(lambda interval: (interval.start,interval.end), intervals),
                        key=lambda interval:interval[1] )

        for i in range(len(intervals)):
            for j in range(i+1, len(intervals)):
                small_st, small_en=intervals[i]
                big_st, big_en=intervals[j]
                assert small_en<=big_en
                if big_st<small_en:
                    return False
        return True            
