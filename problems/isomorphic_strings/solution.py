class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        StoT, TtoS = {}, {}

        for index in range(len(s)):
            if (s[index] in StoT and t[index] != StoT[s[index]]) or \
                (t[index] in TtoS and s[index]!= TtoS[t[index]]):
                return False

            StoT[s[index]] = t[index]
            TtoS[t[index]] = s[index]
        
        return True

        
            
            






