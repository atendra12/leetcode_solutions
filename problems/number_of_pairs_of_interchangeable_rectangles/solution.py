class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        RatioHash = defaultdict(int)
        for width, height in rectangles:
            RatioHash[width/height] += 1
        
        res = 0
        for val in RatioHash.values():
            res += (val * (val-1)) // 2
        
        return res


        