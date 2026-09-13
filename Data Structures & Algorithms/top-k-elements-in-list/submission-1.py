from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # STEP 1: Count frequencies using your exact dictionary logic
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
                
        # STEP 2 & 3: Make the bucket list and fill it
        # We make a list of empty lists. The slots represent the counts.
        freq_buckets = []
        for i in range(len(nums) + 1):
            freq_buckets.append([])  # Adds an empty list [] to each slot
            
        # Put each unique number into its matching frequency slot
        for num in dic:
            count = dic[num]              # Get the count for this number
            freq_buckets[count].append(num)  # Drop it into that index slot
            
        # STEP 4: Loop through the list backwards to grab the top K elements
        result = []
        
        # We start at the very last index (highest count) and walk down to 0
        for i in range(len(freq_buckets) - 1, 0, -1):
            bucket = freq_buckets[i]
            
            # Loop through all numbers sitting in this specific bucket
            for num in bucket:
                result.append(num)
                
                # The moment we have gathered K elements, we are done!
                if len(result) == k:
                    return result
