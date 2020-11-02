class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # num1 > string, non negative int
        # num2 > string, non negative int
        #return sum of both numbers the numbers
        
        ### let's add like binary numbers
        ### reminder after 10 -- %10, // for quo
        sum_string = ''
        length_1 = len(num1)
        length_2 = len(num2)
        carry = 0
        while(length_1>0 or length_2>0 or carry>0):
            length_1 = length_1 - 1
            length_2 = length_2 - 1
            if(length_1>=0):
                carry = carry + int(num1[length_1])
            if(length_2>=0):
                carry = carry + int(num2[length_2])
            sum_string = str(carry % 10) + sum_string
            carry = carry//10
            #print(sum_string)
        return sum_string
            
            
            
            
        
        