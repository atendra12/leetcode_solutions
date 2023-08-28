class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        row, col = len(grid), len(grid[0])

        def dfs(r,c):
            visit.add((r,c))
            dims = [[0,-1],[0,1],[1,0],[-1,0]]
            for dr, dc in dims:
                if r+dr in range(row) and c+dc in range(col) and \
                not (r+dr,c+dc) in visit and grid[r+dr][c+dc]== '1':
                    dfs(r+dr, c+dc)

            return 
             
        island = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] =='1' and not ((i,j) in visit):
                    dfs(i,j)
                    island +=1
                    
        return island
            


        
