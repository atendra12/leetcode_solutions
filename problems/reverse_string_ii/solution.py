class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        # base cases
        if len(s) < k : return s[::-1]
        if len(s) <2*k : return s[:k][::-1] + s[k:]
        return s[:k][::-1] + s[k:2*k] + self.reverseStr(s[2*k:],k) 
        
        """
        ## looping takes most of the time
        output = []
        input_string = list(s)
        iterations = len(input_string)//2*k
        start = 0
        while(iterations > 0):
            temp_string = input_string[start:start+k][::-1]
            output += temp_string + input_string[start+k:start+2*k]
            start += 2*k
            iterations = iterations -1
        rem_string = input_string[start:]
        if(len(rem_string)<= k):
            rem_string.reverse()
            output += rem_string
        if(k<len(rem_string)<2*k):
            temp = rem_string[:k][::-1]
            output += temp + rem_string[k:]
        return "".join(output)
        """
    
            
        