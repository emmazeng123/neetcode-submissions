class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            # left sequence is sorted
            if nums[mid] >= nums[l]:
                if nums[l] > target or target >= nums[mid]:
                    l = mid + 1
                    
                else:
                    r = mid - 1

            # right sequence is sorted
            else:
                if target <= nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1

