class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:


        #这里坐标，平方和，就是距离，heap里肯定要存tuple，（比较对象 距离， 返回标记对象 坐标）
        #heap里面还能（，（））这么嵌套的存吗，但是这里最终要的坐标是list，那么heap里能存list吗，还是（，【】）
        

        #要k个最小的dis，那么最小堆，存所有points，最后弹k次  klogn

        #最大堆，比如1000个元素，要第二小的元素，最大堆，保留k个元素，最后弹k次  nlogk

        #Min heap store whole points（n）  heapy， k‘s smallest point  pop k time the k is k’s smallest， 

        #
        heap = []

        for x,y in points:
            dis = x*x + y*y
            if len(heap) < k:
                
                heapq.heappush(heap, (-dis, [x,y]))
            elif -heap[0][0] > x*x + y*y:
                heapq.heappop(heap)
                heapq.heappush(heap, (-dis, [x,y]))
            #len maxheap >= k  smallest k points

        res = []

        while heap:
            res.append(heapq.heappop(heap)[1])

        return res