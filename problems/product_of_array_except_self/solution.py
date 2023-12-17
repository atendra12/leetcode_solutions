class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left = [0]*length
        right = [0]*length
        result = [0]*length
        for index in range(0,length):
            right_pt = length-1-index
            if index == 0:
                left[index] = 1
                right[right_pt] = 1
            else:
                left[index] = left[index-1]*nums[index-1]
                right[right_pt] = right[right_pt+1]*nums[right_pt+1]
        
        for index in range(0,length):
            result[index] = left[index]*right[index]

        return result
            
        



        





