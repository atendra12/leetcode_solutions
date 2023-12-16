class Solution:
    def maxProduct(self, s: str) -> int:
        N = len(s)
        Hash = {} 
        for bitmask in range(1, 1 << N):
            subseq = ""
            for i in range(N):
                if bitmask & (1 << i):
                    subseq += s[i]
            if subseq == subseq[::-1]:
                Hash[bitmask] = len(subseq)
        
        res = 0
        for index in Hash:
            for another_index in Hash:
                if index & another_index == 0:
                    res = max(res, Hash[index] * Hash[another_index])
    
        return res
                










        