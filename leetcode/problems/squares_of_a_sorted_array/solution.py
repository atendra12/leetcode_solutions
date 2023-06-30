class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        length = len(nums)
        first, last = 0, length -1
        k = length - 1
        result = [0]*length
    
        ## Handle empty
        if length == 0:
            return nums

        while(k>=0):
            if nums[last] > abs(nums[first]):
                result[k] = nums[last]*nums[last]
                last -= 1
            else:
                result[k] = nums[first]*nums[first]
                first += 1
            k -= 1

        return result


            


        
