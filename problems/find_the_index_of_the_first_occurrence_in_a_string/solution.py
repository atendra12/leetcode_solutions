class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length = len(needle)
        for index in range(len(haystack)):
            substr = haystack[index:index+length]
            if substr == needle:
                return index
        
        return -1
        