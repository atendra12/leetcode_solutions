class Solution:
    def minSwaps(self, s: str) -> int:
        ## It's an string, so can't swap it -- Do we need to return the string - No
        ## Only need to return min swap count - think about that only
        ## Opening, closing brackets -- with each swap we take care of two closing bracket

        Closecount = 0
        Maxclosecount = 0

        for item in s:
            if item == '[':
                Closecount -= 1
            else:
                Closecount += 1
            Maxclosecount = max(Maxclosecount, Closecount)
        
        return (Maxclosecount + 1) // 2







        