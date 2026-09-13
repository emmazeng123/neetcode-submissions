from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count frequencies using dictionary
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
                
        # bucket sort 
        # make a list of empty lists

        freq_buckets = []
        for i in range(len(nums) + 1):
            freq_buckets.append([]) 
            
        for num in dic:
            count = dic[num]              
            freq_buckets[count].append(num)  
       
        result = []
        
        
        for i in range(len(freq_buckets) - 1, 0, -1):
            bucket = freq_buckets[i]
            
            for num in bucket:
                result.append(num)
                
                if len(result) == k:
                    return result
