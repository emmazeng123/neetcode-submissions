class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p, s in zip(position,speed)]
        
        stack = [] 
        #reverse sort 
        for p, s in sorted(pair)[::-1]:
            # stack adds speed to reach destination
            stack.append((target - p) / s)
            # pop the position furthest from target if 
            # the furthest collides with the neighbor 
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)