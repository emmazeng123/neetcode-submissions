# split -> read DONT read -> split 

class Solution:
    def encode(self, strs: List[str]) -> str:
       result = ""
       for word in strs:
        result += str(len(word))+"#"+word
       return result 
    
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] != "#":
                j += 1
            # convert length back to int 
            length = int(s[i:j])

            # past the # --> past # pos + length 
            word = s[j+1 : (j+1)+length]
            result.append(word)
            # i is the new length if word 
            i = (j + 1) + length
        return result
        

    
                    
        

    


            



