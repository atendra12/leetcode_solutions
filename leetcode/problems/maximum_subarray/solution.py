class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        cons_sum = nums[start]
        best = nums[start]
        for i in range(1,len(nums)):
            if(nums[i] > cons_sum+nums[i]):
                start = i
                cons_sum = nums[start]
            else:
                cons_sum += nums[i]
            if(cons_sum > best):
                best = cons_sum
        return best
    
        
        