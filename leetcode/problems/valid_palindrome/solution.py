class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        ## remove all the other characters... only alpha...convert case -- used re and sub function 
        ## reverse the string
        ## same string
        if(not s):
            return True
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)
        size = len(s)
        flag = 0
        for i in range(int(size/2)):
            if(s[i]==s[size-1-i]):
                continue
            else:
                flag = 1
                break
        if(flag):
            return False
        else:
            return True
        
            
            
            
        
        