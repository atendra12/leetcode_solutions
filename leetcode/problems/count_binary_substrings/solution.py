class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ## we know that o and 1 need to be in group
        ## lets count these group and put into an array
        ## take min of two adjecent and sum it to get the answer
        
        cnt = 1
        arr = []
        for i in range(len(s)-1):
            if(s[i+1] == s[i]):
                cnt += 1
            else:
                arr.append(cnt)
                cnt = 1
        arr.append(cnt)
        result = 0
        if(len(arr) < 1):
            return result
        else:
            for i in range(len(arr)-1):
                result += min(arr[i],arr[i+1])
            return result
        