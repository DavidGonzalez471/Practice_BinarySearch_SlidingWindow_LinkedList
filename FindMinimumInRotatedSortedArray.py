# using binary search where if right pointer is less than middle you move up left pointer and otherwise the right pointer will move
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) -1
        minimum = float('inf')

        while l <= r:
            m = (l + r) //2
            minimum = min(minimum, nums[m])

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
        return minimum
