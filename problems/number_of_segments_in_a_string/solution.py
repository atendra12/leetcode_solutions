class Solution:
    def countSegments(self, s: str) -> int:
        ## segments --> non space charaters
        #if(s.strip()==""):
        #    return 0
        return len(s.split())
        