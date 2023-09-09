class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # allNums = set([i for i in range(1,len(nums)+1)])
        # nums = set(nums)
        # result = []
        # for item in nums:
        #     allNums.remove(item)
        
        # return allNums

        for n in nums:
            index = abs(n)-1
            nums[index] = - abs(nums[index])

        result = []
        for index, item in enumerate(nums):
            if item > 0:
                result.append(index+1)

        return result


            




        