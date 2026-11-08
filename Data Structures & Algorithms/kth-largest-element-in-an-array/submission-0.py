class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:


        #O(n + klogn)
        #O(n)

        #Min heap : Time O(nlogk) Space O(k)

        #Min heap to store k largest element. Then use heap[0] to get kth largest element
        heap = []
        
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            elif heap[0] < num:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

        return heap[0]
                #curr heap len == k  compare the top of heap with new ele ==> keep bigger one