class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        reminderhash = {0: -1} # {reminder: index}
        prefixsum = 0
        for index, item in enumerate(nums):
            prefixsum += item
            key = prefixsum % k
            if key in reminderhash.keys():
                if (index - reminderhash[key]) > 1:
                    return True
            else:
                reminderhash[key] = index
        
        return False
        



       
        

        