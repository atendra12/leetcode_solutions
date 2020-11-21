class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ## how many numbers are smaller
        num_alt = nums.copy()
        num_alt.sort()
        output = []
        for item in nums:
            output.append(num_alt.index(item))
        return output
        