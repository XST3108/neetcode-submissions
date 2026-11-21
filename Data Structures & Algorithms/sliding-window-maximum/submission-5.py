class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:


        res = []


        # monostanic queue
        q = deque()

        for i in range(k):
            if not q:
                q.append(nums[i])
            else:
                while q and q[-1] < nums[i]:
                    q.pop()
                q.append(nums[i])
        res.append(q[0])

        for i in range(k, len(nums)):
            if q[0] == nums[i-k]:
                q.popleft()
            #remove left first
            #then add new to right
            while q and q[-1] < nums[i]:
                q.pop()
            q.append(nums[i])
            res.append(q[0])

        return res





        #初始化完

        


        