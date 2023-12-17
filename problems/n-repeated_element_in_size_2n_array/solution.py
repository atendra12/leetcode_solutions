class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        from collections import Counter
        dict_A = Counter(A)
        for key in dict_A.keys():
            if(dict_A[key]>1):
                return key