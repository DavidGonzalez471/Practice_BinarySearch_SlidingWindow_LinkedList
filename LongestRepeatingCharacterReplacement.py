#finding longest substring while being able to replace k strings.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}
        res = 0

        l = 0
        #for loop incrementing right pointer while maintaining left slider
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            #while loop sliding left pointer until within the boundaries of k
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res
#creating a maxfrequency variable that stops from consistently checking the dictionary
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}
        res = 0
        maxfreq = 0

        l = 0
        #for loop incrementing right pointer while maintaining left slider and keeping track of maxfreq
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxfreq = max(maxfreq, count[s[r]])
            
            #while loop sliding left pointer until substring - maxfreq is within the boundaries of k
            while (r - l + 1) - maxfreq > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res
