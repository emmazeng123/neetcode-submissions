class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        res = 0
        
     
        for r in range(len(s)):
            # grab whatever alphabet seen so far, if exists, increment else add to dic and increment from 0 
            count[s[r]] = 1 + count.get(s[r],0)

            # window can grow bigger as long as there is enough replacements to fill variables that are NOT the 
            # max count variable 

            # shift window by shrinking from left first before doing anything 
            # because window is invalid --> r keeps moving forward to see if theres an even bigger array 
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            # save max window size 
            res = max(res, r - l + 1)
        return res 
