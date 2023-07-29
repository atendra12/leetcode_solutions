class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) ==0:
            return 0
        l, r = 0 ,1 # l = start of substring, r= end of substring with no duplicates
        maxsubstr = set(s[l])
        maxlength = len(maxsubstr)

        while (r < len(s) and l <=r):
            if s[r] not in maxsubstr:
                maxsubstr.add(s[r])
                r +=1
                maxlength = max(maxlength,len(maxsubstr))
            else:
                maxsubstr.remove(s[l])
                l +=1
        
        return maxlength



                






