class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ## Can only be A, C, G, T
        hashstring = {} ## substr: count
        res = set()
        for index in range(len(s) -9):
            substr = s[index : index + 10]
            if substr in hashstring:
                res.add(substr)
            else:
                hashstring[substr] = 1
        
        return res
            











        