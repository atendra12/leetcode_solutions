class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        return [nums[index+1] for index in range(0,len(nums)-1,2) for _ in range(nums[index])]
        