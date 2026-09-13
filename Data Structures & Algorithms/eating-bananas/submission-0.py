class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = r                          # max speed always works

        while l <= r:
            k = (l + r) // 2
            total = 0
            for pile in piles:
                total += math.ceil(pile / k)
            if total <= h:               # k works
                ans = k                  # remember it
                r = k - 1                # try slower
            else:                        # too slow
                l = k + 1
        return ans
