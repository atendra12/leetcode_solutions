class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        first = second = 0
        while first < len(s) and second < len(t):
            if s[first] == t[second]:
                first +=1
                second +=1
            else:
                second +=1
        
        return True if first == len(s) else False

        