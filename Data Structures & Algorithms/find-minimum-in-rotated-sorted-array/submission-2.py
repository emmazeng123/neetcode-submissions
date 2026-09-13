class Solution:
    def findMin(self, nums: List[int]) -> int:
        tracker = nums[0]
        l = 0
        r = len(nums) - 1 

        while (l <= r):
            if (nums[l] < nums[r]):
                tracker = min(tracker,nums[l])
                break
            mid = (l + r) // 2 
            tracker = min(tracker,nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1 
            else:
                r = mid - 1 
        return tracker 
