"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        #只要有重复的，就return false
        #不需要用到合并后的区间 不用res
        intervals.sort(key=lambda x:x.start)
        for i in range(1,len(intervals)):
            curr_start = intervals[i].start
            curr_end = intervals[i].end
            if curr_start < intervals[i-1].end:
                return False

        return True




















        # if not intervals or len(intervals) == 1:
        #     return True

        # intervals.sort(key=lambda x:x[0])

        # prev_end = intervals[0][1]

        # for s,e in intervals[1:]:
        #     if s<e:
        #         return False

        #     else:
        #         prev_end = e

        # return True
        


        


