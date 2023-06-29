class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        results = set()
        for item in nums:
            if item in results:
                return True
            else:
                results.add(item)
        return False
