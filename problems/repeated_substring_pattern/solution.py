class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ## if a pattern of length k starting repeating
        ## if by swamping s will remain same
        ## now this k can go from 1 to len(s)//2
        for i in range(1,len(s)//2+1):
             if(s==s[i:] + s[:i]):
                    return True
        return False
        
        
        