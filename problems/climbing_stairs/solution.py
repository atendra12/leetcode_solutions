class Solution:
    def climbStairs(self, n: int) -> int:
        ## Recursive + Memo
        # if n == 1:
        #     return 1
        
        # res = [-1 for i in range(n+1)]
        # def helper(n):
        #     if n < 0:
        #         return 0
            
        #     if n == 0 or n == 1:
        #         return 1
            
        #     if res[n] != -1:
        #         return res[n]
        #     else:
        #         res[n] = helper(n-1) + helper(n-2)
        #         return res[n]
        
        # helper(n)
        # return res[n]

        ## Tabulation
        # if n == 1:
        #     return 1

        # res = [1,1]
        # for j in range(2,n+1):
        #     res.append(res[j-1] + res[j-2])
        
        # return res[n]

        ## Space Optmization

        if n==1:
            return 1
            
        var1 = 1
        var2 = 1

        for j in range(2,n+1):
            temp = var1 + var2
            var1 = var2
            var2 = temp
        
        return var2
        


            





        
        