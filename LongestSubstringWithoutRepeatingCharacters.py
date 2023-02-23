#creating two pointers that slide along and check the items in the list and restarting at the next character
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = []
        p1, p2 = 0, 0
        res = 0
        while p1 <= (len(s) -1):

            if s[p1] in longest:
                longest.clear()
                p1 = p2 + 1
                p2 = p1
            longest.append(s[p1])
            res = max(res, len(longest))
            p1 += 1

        return count
    
#creates a set which has faster search times for items within, using a move r pointer and a resetting L pointer to check against and remove from the set against
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res            
