class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = dict()
        for index, item in enumerate(nums):
            rem = target - item
            if rem in result.keys():
                return index, result[rem]
            else:
                result[item] = index



        