class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ## equal means repetition of elements
        
        repeat = {}
        num = 0 ## number of good paris
        for item in nums:
            if item in repeat:
                if(repeat[item]==1):
                    num += 1
                else:
                    num += repeat[item]
                repeat[item] += 1                
            else:
                repeat[item] = 1                
        return num
        
        
        
        