class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ## haystak and needle --> only alpha
        if(len(needle)==0):
            return 0
        for index in range(0,len(haystack)):
            if(haystack[index] == needle[0]):
                if(haystack[index:index+len(needle)] == needle):
                    return index
            else:
                continue
        return -1
            
        
        