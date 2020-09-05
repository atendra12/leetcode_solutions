class Solution:
    def romanToInt(self, s: str) -> int:
        word_to_num = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}        
        prev_val = word_to_num[s[0]]
        #exceptions = ['IV','IX','XL','XC','CD','CM']
        #exceptions_value = [4,9,40,90,400,900]
        total_sum = 0
        #i = 0
        for i in s:
            if(word_to_num[i] > prev_val):
                total_sum = total_sum + (word_to_num[i] - 2*prev_val)            
            else:
                total_sum = total_sum + word_to_num[i]
            prev_val = word_to_num[i]
        return total_sum        
        #while( i < len(s)):
        #    try:                
        #        index = exceptions.index(s[i:i+2])
        #        total_sum = total_sum + exceptions_value[index]                  
        #        i = i + 2
        #    except:
        #        total_sum = total_sum + word_to_num[s[i]]
        #        i = i + 1
        #return total_sum
        
        