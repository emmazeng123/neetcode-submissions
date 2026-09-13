class Solution:

    def isPalindrome(self, s: str) -> bool:
        l,r = 0,len(s) - 1 

        while (l < r):
            # ignore unique chars 
            while l < r and not self.letterNum(s[l]):
                l += 1
            while r > l and not self.letterNum(s[r]):
                r -= 1

            # compare lowercase 
            if s[l].lower() != s[r].lower():
                return False 

            l += 1
            r -= 1
        return True

    def letterNum(self,c):
            return (ord('A') <= ord(c) <= ord('Z') or 
                   ord('a') <= ord(c) <= ord('z') or 
                   ord('0') <= ord(c) <= ord('9'))


            
            
            
                


            
        
    
        