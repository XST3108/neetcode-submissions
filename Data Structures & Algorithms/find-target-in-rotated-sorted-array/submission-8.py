class Solution:
    def search(self, nums: List[int], target: int) -> int:


        

        #partially sorted

        #find exact target value

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l+r) // 2

            if nums[mid] == target:
                return mid

            elif nums[l] <= nums[mid]:

                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    #[mid, r]
                    l = mid +1

                # nums[mid]  target
                #  10            3  ==> [l,mid-1]
                
            else:
                # mid < target 
                if nums[mid] < target <= nums[r]:
                    #[mid+1, r]
                    l = mid +1
                else:
                    r = mid -1

        return -1



                






























        




        # 寻找某个固定的target值，所以用第一个模板

        # 先sort不可取

        # 因为是无顺序的 所以不能mid 大于target就往左找

        # 每次需要让mid判定trget + right？

        # 所有二分都是通过mid来判定的？？





        # l = 0
        # r = len(nums) - 1

        # while l <= r:

        #     mid = (l + r) // 2

        #     if nums[mid] == target:
        #         return mid

        #     if nums[mid] < nums[r]:

        #         if nums[mid] < target <= nums[r]:
        #             l = mid + 1
        #         else:
        #             r = mid - 1

                

        #     else:
        #         if nums[l] <= target < nums[mid]:
        #             r = mid - 1

        #         else:
        #             l = mid + 1

           

        # return -1

        


