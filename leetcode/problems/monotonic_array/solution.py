class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        size = len(A)
        if(A[0] > A[size-1]):
            dec_flag = 1
        else:
            dec_flag = 0
        for index in range(size-1):
            if(dec_flag):
                if(A[index] >= A[index+1]):
                    continue
                else: return False
            else:
                if(A[index] <= A[index+1]):
                    continue
                else: return False
        return True
                    