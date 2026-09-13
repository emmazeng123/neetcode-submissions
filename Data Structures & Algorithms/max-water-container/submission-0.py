class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1 
        h = 0
        max = 0

        while l < r: 
            if heights[l] < heights[r]:
                h = heights[l]
                length = r - l
                area = h*length
                l+=1
            elif heights[l] > heights[r]:
                h = heights[r]
                length = r - l
                area = h*length
                r-=1
            else:
                h = heights[l]
                length = r - l
                area = h*length
                l+=1
            if area > max:
                max = area        
        return max
        