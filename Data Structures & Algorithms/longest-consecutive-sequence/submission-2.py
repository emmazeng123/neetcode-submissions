class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # build a set 
        numset = set(nums)
        maxnum = 0

        for num in nums:
            curr = num
            # beginning of seq 
            if num-1 not in numset:
                length = 1
                # count the values in sequence 
                while curr+1 in numset:
                    length += 1
                    curr+=1
                if maxnum < length:
                    maxnum = length
        return maxnum


