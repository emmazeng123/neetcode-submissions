class Solution:
    def isValid(self, s: str) -> bool:
        # stores opening parenthesis 
        stack = []
        close_dic = {"]" : "[", "}": "{", ")" : "("}

        for char in s:
            # if char is a closing parenthesis 
            if char in close_dic:
                # checks if opening matches in the stack 
                if len(stack) != 0 and close_dic[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0
        


                
                