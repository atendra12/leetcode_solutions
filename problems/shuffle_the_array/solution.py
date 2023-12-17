class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        output = []
        for index in range(n):
            output.append(nums[index])
            output.append(nums[index+n])
        return output
        
        
        