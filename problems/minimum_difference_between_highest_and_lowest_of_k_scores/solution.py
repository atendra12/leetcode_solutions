class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        ## one of learning is if you are not able to solve think about sorting array as well

        nums.sort()
        start, end = 0, k-1
        minVal = float('inf')

        while end < len(nums):
            minVal = min(minVal,nums[end] - nums[start])
            start, end = start + 1, end +1
        
        return minVal


            
        

        


        