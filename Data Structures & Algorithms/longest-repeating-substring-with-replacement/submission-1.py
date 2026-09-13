class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0 

        for r in range(len(s)):
            # add s[r] to the window and increment its count
            # if it doesn't exist yet, start its count at 0, then add 1
            count[s[r]] = 1 + count.get(s[r], 0)

            # window size - most frequent char count
            # = number of replacements needed
            #
            # if replacements needed > k, the current window is invalid
            while k < (r - l + 1) - max(count.values()) :

                # remove the leftmost character from the window
                # and shrink the window from the left
                count[s[l]] -= 1
                l += 1

            # curr window is valid, so save its length if it's
            # the longest valid window we've seen
            res = max(res, r - l + 1)

        return res


