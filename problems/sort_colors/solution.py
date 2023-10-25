class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        zero_pt = 0
        one_pt = 0
        two_pt = len(nums) -1

        while one_pt <= two_pt:
            if nums[one_pt] == 1:
                one_pt +=1
            else:
                ## need to swap with either side
                if nums[one_pt] == 0:
                    ## swap with left
                    nums[zero_pt], nums[one_pt] = nums[one_pt], nums[zero_pt]
                    if zero_pt == one_pt:
                        one_pt += 1
                    zero_pt +=1
                else:
                    ## swap with right
                    nums[two_pt], nums[one_pt] = nums[one_pt], nums[two_pt]
                    two_pt -=1
        
        
















        
        