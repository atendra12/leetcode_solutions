class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        key = None
        for item in nums:
            if cnt == 0:
                cnt = 1
                key = item
            else:
                if item == key:
                    cnt += 1
                else:
                    cnt -= 1
        return key

