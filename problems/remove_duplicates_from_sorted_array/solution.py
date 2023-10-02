class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur, nextPt = 1, 1

        while nextPt < len(nums):
            if nums[cur-1] == nums[nextPt]:
                nextPt +=1 ## keep increasing to find out non duplicate values
            else:
                ### nums is unique, not duplicate
                if nextPt != cur:
                    ##reaplce
                    nums[cur], nums[nextPt] = nums[nextPt], nums[cur]
                
                nextPt +=1
                cur +=1
        
        return cur



            






        