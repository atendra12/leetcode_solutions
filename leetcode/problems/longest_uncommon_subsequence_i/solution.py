class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        # longest uncommon subseq
        # strings - a,b
        if(a==b):
            return -1
        else:
            return max(len(a),len(b))
        
        