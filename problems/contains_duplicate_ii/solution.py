class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        windowset = set()
        left = 0

        for right in range(len(nums)):
            if right - left > k:
                windowset.remove(nums[left])
                left +=1
            
            if nums[right] in windowset:
                return True

            windowset.add(nums[right])
        
        return False

