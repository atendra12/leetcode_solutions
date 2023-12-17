class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        N = len(grid[0])
        top, bottom = grid[0].copy(), grid[1].copy()
        for index in range(1, N):
            top[index] += top[index-1]
            bottom[index] += bottom[index-1]
        
        res = float('inf')
        for index in range(N):
            ## at Index it will go down
            topValue = top[N-1] - top[index]
            if index >0:
                bottomvalue = bottom[index-1]
            else:
                bottomvalue = 0
            secondbotVal = max(topValue, bottomvalue)
            res = min(secondbotVal, res)
        
        return res








        










        