class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for index in range(len(nums)):
            my_dict[nums[index]] = index
        for index in range(len(nums)):
            try:
                second_index = my_dict[target-nums[index]]
                if index != second_index:
                    return index, second_index
            except:
                continue
        
      
        