class Solution:
    def firstUniqChar(self, s: str) -> int:
        #if(s.strip()==""):
        #    return -1
        # what about blank string
        for letter in range(len(s)):
             if(s.count(s[letter]) < 2):
                    return letter
        return -1
                