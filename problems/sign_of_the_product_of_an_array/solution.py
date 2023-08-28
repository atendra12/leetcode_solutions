class Solution:
    def arraySign(self, nums: List[int]) -> int:
        prod = 1
        for item in nums:
            if item ==0:
                return 0
            if item < 0:
                prod = -1 * prod
        return prod