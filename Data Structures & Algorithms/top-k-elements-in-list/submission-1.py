class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        for num in nums:
            count[num] = count.get(num,0) + 1

        #key:value => num: freq

        heap = []

        for num, freq in count.items():
            if len(heap) < k:
                #not full
                heapq.heappush(heap, (freq, num))
            else:
                # full
                #min heap,
                if freq > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (freq,num))

        
        res = []

        for freq, num in heap:
            res.append(num)

        return res






































        # 先建表，key就是元素的值，value就是出现频率（建立一个频率表）

        # 创建个长度len。nums + 1的数组，里面每个元素先存【】


        






        # for hash map 遍历哈希表，把每个key 给append进对应数组的index







        # hash_map = {}

        # bucket = [[] for _ in range( len(nums) + 1 )]

        # for key,frequent hash_map.items():
        #     bucket[frequent].append(key)


        # res = []

        # for i in bu


        
        # 这样对吗，后面怎么从bucket取top2呢


        

        


        # 先建表，for循环，if 当前元素在表里，value += 1 给value的值加1
        # 如果不在，就把当前值 = 1 加入到表里

        # 这样我们就得到了一个hash表，key是num，value是对应出现的频率

        # 下一步我们就要找出频率前k个元素

        # 创建个bucket的数组，

        # 现在我们有了这个bucket的数组，然后怎么把里面topk的元素拿出来放到最终的res 数组中呢

        # res


        


        # 2. 数组部分

        # 我们需要用一个新的数组，这个数组的index就是出现的频率，[[100,2],[],[],[2]]








        # 我现在的想法是把nums里面的元素遍历存储到hashmap里面，然后对应的value就是出现的次数

        # 那么我得到了这个hashmap之后，再sort出value最大的前两个对应的key

        # 这个思路对吗，如果对的话，如何实现“再sort出value最大的前两个对应的key”这部分的代码呢