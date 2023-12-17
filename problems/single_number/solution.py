class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        dict_nums = Counter(nums)
        for key in dict_nums.keys():
            if(dict_nums[key]==1):
                return key
        
            
        