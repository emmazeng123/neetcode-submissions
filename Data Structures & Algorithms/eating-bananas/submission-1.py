class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1 
        r = max(piles)
        monsterbananaspeed = 0

        while l <= r:
            mid = (l+r) // 2
            k = mid
            hours = 0

            # sum hours of eating speed 
            for p in piles:
                hours += math.ceil(p/k)

            # check validility of k
            if hours <= h:
                # update eating speed 
                monsterbananaspeed = k
                r = mid - 1 
            else:

                l = mid + 1
        return monsterbananaspeed


        
        
            
