class Solution: 
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # [temp, index]
        # if doesnt find a higher temp, returns 0 in that array
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                # properly unpack the list
                stackTemp, stackIndex = stack.pop()
                # distance btw curr temp & previous 
                res[stackIndex] = i - stackIndex
            stack.append([temp,i])
        return res


        
        

        

        
    
        

        