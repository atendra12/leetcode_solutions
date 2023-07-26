class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        first = 0
        last = len(numbers) - 1 
        while(first < last):
            sum_value = numbers[first] + numbers[last]
            if sum_value == target:
                return [first+1,last+1]
            elif sum_value > target:
                last -= 1
            else:
                first += 1
         

