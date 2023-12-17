class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ## binar number addition
        ## 0 + 0 - > 0
        ## 0 + 1 or 1 + 0 -> 1
        ## 1 + 1 = 10
        ## take two pointers from right end side and do the sum
        ## a right idea but became worried --> as idea of calculating carry was little unknown
        ## adding the string was unknow too**
        
        res = ''
        carry = 0
        aA = list(a)
        bA = list(b)
        while aA or bA or carry:
            if aA:
                carry += int(aA.pop())
            if bA:
                carry += int(bA.pop())
            
            res = str(carry%2) + res
            carry //= 2
            
        return res
        
        
        
        
            
        
            
            
            
        