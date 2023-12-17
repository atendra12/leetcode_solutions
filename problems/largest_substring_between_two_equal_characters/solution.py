class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ## b/w two equal char -- max length of substring
        index = {}
        for i in range(len(s)):
            if s[i] in index:
                index[s[i]].append(i)
            else:
                index[s[i]] = [i]
        long_count = -1
        for key in index.keys():
            length = max(index[key]) - min(index[key]) - 1
            if(length > long_count):
                long_count = length
        return long_count
        
        
        