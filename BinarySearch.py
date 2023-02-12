#binary search in python splits list in half checks if number is greater or less than and removes half the list from consideration can only be done on sorted lists
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) -1 

        while l <= r:
            m = l + (r - l) //2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
        
        return -1
