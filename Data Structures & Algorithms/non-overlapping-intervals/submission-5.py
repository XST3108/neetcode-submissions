class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:



        #贪心，根据end排序，遍历，如果遇到当前和上一个重复，就count+=1，
        if len(intervals) <= 1:
            return 0

        intervals.sort(key=lambda x:x[1])

        res = []
        res.append(intervals[0])
        count = 0

        for i in range(1,len(intervals)):
            cur_start = intervals[i][0]

            #[1,2],[2,3]
            if cur_start < res[-1][1]:
                count +=1
            else:
                res.append(intervals[i])

        return count






























        # intervals.sort(key= lambda x:x[0])
        # count = 0

        # if not intervals or len(intervals) == 1:
        #     return 0

        # prev_end = intervals[0][1]

        # for i in range(1, len(intervals)):
        #     s,e  = intervals[i]

        #     if s < prev_end:
        #         count += 1
        #         prev_end = min(prev_end, e)
        #     else:
        #         prev_end = e

        # return count

        
