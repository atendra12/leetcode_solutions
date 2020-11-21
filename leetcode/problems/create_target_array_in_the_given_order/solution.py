class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target_array = []
        for i in range(len(index)):
            target_array = target_array[0:index[i]]+ [nums[i]] + target_array[index[i]:]
        return target_array
    
            
            
        
            
        
        
        
        