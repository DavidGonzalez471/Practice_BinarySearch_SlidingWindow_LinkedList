#A binary search solution where the list is split into two and dictates based on a left sorted side and a right sorted side and split further from there
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) -1
        

        while l <= r:
            m = (r + l) //2

            if nums[m] == target:
                return m

            if nums[m] <  nums[r]:
                if nums[m] > target or nums[r] < target:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target or nums[l] > target:
                    l = m + 1
                else:
                    r = m - 1
            
        return -1
