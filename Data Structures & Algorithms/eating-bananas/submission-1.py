class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        #找到最小得答案k，k=0，1
        #                 False False True True
        #  第一个k（满足条件的 ==》 第一个判断True的）

        # because within one hour we can only eat one pile,(1 hour most finish 1 pile)
        # r = max(piles), l = 1

        l = 1
        r = max(piles)

        # input a k, to check whether this k can finish all pile within h
        def check(k):

            hours = 0

            for pile in piles:
                cur_hour = (pile + k - 1) // k
                hours += cur_hour
                # pile // k then upper quzheng
            if hours > h:
                return False
            else:
                return True

        #Finally return True or False


        while l <= r:

            mid = (l + r) // 2

            if check(mid):
                # F F T T T
                r = mid - 1
            else:
                # F F F T T
                l = mid + 1

        return l


            

        
        