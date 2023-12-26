class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        binaryset = set()
        for index in range(len(s) - k + 1):
            binaryset.add(s[index : index + k])
        
        return len(binaryset) == 2 ** k
        


        