#
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        k = max(piles)

        while l <= r:
            m = l + (r - l) //2

            count = 0
            for p in piles:
                count += math.ceil(p / m)
            if count <= h:
                k = min(k ,m)
                r = m -1
            else:
                l = m + 1

        return k
