class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) -1
        maxArea = 0
        while left < right:
            Area = min(height[left],height[right]) * (right-left)
            maxArea = max(Area,maxArea)
            if height[left] >= height[right]:
                right = right- 1
            else:
                left = left + 1
        return maxArea
                
        
        