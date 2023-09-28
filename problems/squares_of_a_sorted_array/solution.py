class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # l, r = 0, len(nums) -1

        # while l <=r:
        #     if nums[r]**2 < nums[l]**2:
        #         ## swap values
        #         temp = nums[r]
        #         nums[r] = nums[l]**2
        #         nums[l] = temp
        #     else:
        #         nums[r] = nums[r]**2
            
        #     r -=1
        
        # return nums

        l, r = 0, len(nums) -1
        res = [0 for i in range(len(nums))]
        index = len(nums) -1

        while index > -1:
            if nums[r]**2 < nums[l]**2:
                res[index] = nums[l]*nums[l]
                l += 1
            else:
                res[index] = nums[r]*nums[r]
                r -= 1
            
            index -=1

        
        return res
        





            


        