#
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == "":
            return ""
        
        tCount, window = {}, {}

        for c in t:
            tCount[c] = 1 + tCount.get(c, 0)
        
        have, need = 0, len(tCount)

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if window[c] == tCount

        
        

