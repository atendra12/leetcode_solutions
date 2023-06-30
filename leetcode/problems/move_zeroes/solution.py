class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ## Single Element list
        length = len(nums)
        if length == 1:
            return nums
        
        first = 0
        second = 1

        while(second < length):
            if nums[first] == 0 and nums[second] == 0:
                second += 1
            else:
                if nums[first] == 0:
                    temp = nums[first]
                    nums[first] = nums[second]
                    nums[second] = temp
                    first += 1
                    second += 1
                else:
                    first += 1
                    second += 1
        return nums


