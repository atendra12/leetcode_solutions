class Solution:
    def isValid(self, s: str) -> bool:
        ### first thing to check if both the characters are available
        ### second thing to check if characters are inserted into order
        ### their vice- versa are orderd in another way
        
        opening_char = {'(':0,'{':0,'[':0}
        closing_char = {')':0,'}':0,']':0}
        
        open_brac = '()'
        curely_brac = '{}'
        close_brac = '[]'
        
        acceptable = [open_brac,curely_brac,close_brac]
        
        if(s in acceptable or len(s)==0):
            return True
        else:
            new_s = s.replace(open_brac,'').replace(curely_brac,'').replace(close_brac,'')
            if(s == new_s):
                return False
            else: 
                return self.isValid(new_s)
            
            
            
            
        
        
        
        
        
        

        
        
        