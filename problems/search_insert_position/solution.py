class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def helper(start, end):
            if start > end: 
                return start

            mid = (end + start) // 2
            if nums[mid] == target:
                return mid

            if target <  nums[mid]:
                return helper(start, mid-1)
            else:
                return helper(mid+1, end)

        return helper(0, len(nums) - 1)
