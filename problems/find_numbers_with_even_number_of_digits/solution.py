class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for item in nums:
            if(len(str(item))%2 == 0):
                count += 1
            else:
                continue
        return count
        