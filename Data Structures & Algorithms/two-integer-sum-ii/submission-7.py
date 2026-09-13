class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l = 0
        r = len(numbers)-1

        while r > l:
            if target-numbers[l] < numbers[r]:
                r-=1 
            if numbers[l]+numbers[r] < target:
                l+=1
            if numbers[l]+numbers[r] == target:
                return [l+1,r+1]
            
        

            
        

            
            