class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        r = 0
        count = 0
        maxCount = 0

        while r < len(s):
            if s[r] not in charSet:
                charSet.add(s[r])
                count += 1
                maxCount = max(maxCount, count)
                r += 1
            else:
                charSet.remove(s[l])
                l += 1
                count -= 1

        return maxCount


        



