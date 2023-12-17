class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel_list = ['a','e','i','o','u','A','E','I','O','U']
        s = s
        s = list(s)
        size = len(s)
        start = 0
        last = size-1
        while(start<last):
            if(s[start] in vowel_list and s[last] in vowel_list):
                temp = s[start]
                s[start] = s[last]
                s[last] = temp
                start = start + 1
                last = last - 1
            if(not s[start] in vowel_list):
                start = start + 1
            if(not s[last] in vowel_list):
                last = last - 1
        s = "".join(s)
        return s
                
            
                
        
    
            
            
            
        
        