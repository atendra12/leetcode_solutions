class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # first, second  = 0, 0
        # while second < len(nums) and first < len(nums):
        #     ## keep moving second pointers until reaches non zero element
        #     if nums[second] == 0:
        #         second +=1
        #         continue
        #     if nums[first] != 0:
        #         first +=1
        #         continue
            
        #     ## swap values
        #     if first < second:
        #         nums[first] = nums[second]
        #         nums[second] = 0
        #     else:
        #         second +=1

        first, second  = 0, 0
        while second < len(nums) and first < len(nums):
            if first < second and nums[first] == 0 and nums[second] != 0:
                nums[first] = nums[second]
                nums[second] = 0
                first +=1
                second +=1
            elif nums[first] != 0:
                first +=1
            else:
                second +=1
            


            
            
            


        



            






        