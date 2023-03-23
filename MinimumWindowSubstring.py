#Solution where hashmaps are created and used to count the substring and is used to count the substring of s 
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #base statement where t cant be empty or larger than s.
        if len(t) > len(s) or t == "":
            return ""
        
        #creating hashmap and filling the count hashmap with the item count and items of t.
        tCount, sCount = {}, {}
        for c in t:
            tCount[c] = 1 + tCount.get(c, 0)
        
        #for loop that iterates through s and completes main algorithm behind program
        have, need = 0, len(tCount)
        res, length = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            sCount[c] = 1 + sCount.get(c, 0)
            if c in tCount and sCount[c] == tCount[c]:
                have += 1
            #while loop to check and update the left pointer if we have the amount char required.
            while have == need:

                if (r - l + 1) < length:
                    res = [l, r]
                    length = (r -l + 1)
                
                window[s[l]] -= 1
                if s[l] in tCount and window[s[l]] < tCount[s[l]]:
                    have -= 1
                l += 1

        l, r = res

        if length == float("infinity"):
            return ""
        else:
            return s[l:r + 1] 

