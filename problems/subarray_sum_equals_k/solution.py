class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSumHash = {0:1}
        sumTillnow = 0
        res = 0

        for item in nums:
            sumTillnow += item
            res += prefixSumHash.get(sumTillnow - k, 0)
            prefixSumHash[sumTillnow] = prefixSumHash.get(sumTillnow, 0) + 1
        
        return res




        
        
        