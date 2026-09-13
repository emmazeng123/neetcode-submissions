class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0 

        for r in range(len(s)):
            # if key exists, get the key and increment
            # if doesnt exist, return 0 
            count[s[r]] = 1 + count.get(s[r],0)
            # window size - max substring len > replacements 
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res



