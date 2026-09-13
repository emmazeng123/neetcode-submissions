class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} 

        for i in range(len(nums)):
            needed  = target - nums[i]
            if needed in seen:
                if seen[needed] < i:
                    return [seen[needed],i]
                else:
                    return [i,seen[needed]]
                return
            else:
                seen[nums[i]] = i

                
        
        