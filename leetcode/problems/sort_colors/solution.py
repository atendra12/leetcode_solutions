class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        first_pt = 0 
        second_pt = first_pt 
        third_pt = length - 1
        # if length==2:
        #     if nums[0] > nums[1]:
        #         nums[0], nums[1] = nums[1], nums[0]

        #while(second_pt+1 <= third_pt and length>1):
        while(second_pt+1 <= third_pt):
            if nums[first_pt] == 0 and nums[second_pt]==0:
                first_pt+= 1
                second_pt+=1
            elif (nums[first_pt]== 0):
                first_pt+= 1
            elif nums[second_pt] == 1:
                second_pt+=1
            elif nums[third_pt] == 2:
                third_pt-=1
            if nums[second_pt] == 2:
                ## swap with third_pt
                if nums[third_pt] !=2:
                    nums[second_pt], nums[third_pt] = nums[third_pt], nums[second_pt]
                    third_pt-=1
            if nums[second_pt] == 0:
                ## swap with first_pt
                if nums[first_pt]!=0:
                    nums[second_pt], nums[first_pt] = nums[first_pt], nums[second_pt]
                    first_pt+= 1