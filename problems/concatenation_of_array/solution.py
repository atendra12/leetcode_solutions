class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #return nums + nums
        result = []
        for index in range(2):
            result += nums

        return result 
        