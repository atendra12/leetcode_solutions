class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        index = 0
        count = 0
        hashzero = {}
        res = 0
        while index < len(nums):
            if nums[index] != 0:
                if count > 0:
                    hashzero[count] = hashzero.get(count, 0) + 1
                count = 0
                index += 1
                continue
            else:
                count += 1
                index += 1

        if index == len(nums) and count > 0:
            hashzero[count] = hashzero.get(count, 0) + 1

        for key in hashzero:
            res += hashzero[key] * int((key * (key +1))/2)
        
        return res



            
                
                                                                                   



        