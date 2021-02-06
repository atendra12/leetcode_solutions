class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        merged = []
        for item in intervals:
            if (not merged or (merged[-1][1] < item[0])):
                merged.append(item)   
            else:
                merged[-1][1] = max(merged[-1][1],item[1])
        return merged
                
            
                
                
            
                
            
        
        
        