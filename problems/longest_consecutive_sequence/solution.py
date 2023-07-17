class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_values = set(nums)
        longest = 0
        for number in nums:
            if (number -1) not in unique_values:
                length = 0
                while (number +length) in unique_values:
                    length +=1
                longest = max(longest,length)
        return longest


