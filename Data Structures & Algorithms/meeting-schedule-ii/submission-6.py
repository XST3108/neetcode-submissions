"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:


        #遍历input的intervals，吧statr和end拆分开，搞成单独的event

        events = []

        for interval in intervals:
            events.append((interval.start,1))
            events.append((interval.end,-1))

        events.sort()

        cur = 0
        res = 0

        #events: [(0,1),(40,-1)]
        for _,delta in events:
            cur +=  delta
            res = max(cur,res)

        return res






















        


        # heap = []
        # res = 0
        # intervals.sort(key = lambda x:x.start)

        # #heap store all rooms' end time

        # for interval in intervals:

        #     start = interval.start
        #     end = interval.end
        #     #need a new room
        #     if heap and start < heap[0]:
        #         res += 1
        #         heapq.heappush(heap, end)

        #     elif not heap:
        #         heapq.heappush(heap, end)
        #         res += 1
            
        #     else:
        #         #no need for a new room
        #         heapq.heappop(heap)
        #         heapq.heappush(heap, end)

        # return res

        

            
