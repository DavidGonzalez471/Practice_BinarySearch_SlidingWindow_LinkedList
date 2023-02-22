#
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums2) < len(nums1):
            a, b = nums2, nums1
        else:
            a, b = nums1, nums2
        
        l, r = 0, len(a) -1
        while True:
            i = (l + r) //2
            j = half - i - 2

            aLeft = a[i]
            aRight = a[i + 1]
            bLeft = b[j]
            aRight = b[j + 1]
            
