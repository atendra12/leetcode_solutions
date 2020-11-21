class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ### if empty
        running_sum= []
        if(len(nums)==0):
            return running_sum
        running_sum.append(nums[0])
        for index in range(1,len(nums)):
            running_sum.append(running_sum[index-1] + nums[index])
        return running_sum