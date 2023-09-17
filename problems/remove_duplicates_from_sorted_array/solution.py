class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r, count = 0, 0, 1

        while r < len(nums):
            if nums[l] < nums[r]:
                l += 1
                count += 1
                nums[l] = nums[r]
            r+=1
        
        return count






