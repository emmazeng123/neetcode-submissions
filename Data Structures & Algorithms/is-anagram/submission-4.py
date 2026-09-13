class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dic = {}

        for letter in s:
            if letter in s_dic:
                s_dic[letter] += 1 
            else:
                s_dic[letter] = 1
        
        t_dic = {} 

        for letter in t:
            if letter in t_dic:
                t_dic[letter] += 1 
            else:
                t_dic[letter] = 1


        if t_dic == s_dic:
            return True
        else:
            return False

    

            
        
        
        



        
        



        
