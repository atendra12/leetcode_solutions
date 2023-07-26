class Solution:
    def maxArea(self, height: List[int]) -> int:
        first = 0
        last = len(height) - 1
        max_Area =(last - first)* min(height[last],height[first])
        while (first < last):
            if height[last] < height[first]:
                last -= 1
            else:
                first +=1
            area = (last - first)* min(height[last],height[first])
            if area > max_Area:
                max_Area = area
        return max_Area
            


        