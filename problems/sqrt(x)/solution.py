class Solution:
    def mySqrt(self, x: int) -> int:
        ## it will be b/w 1 and X
        ## start with x/2

        # def helper(start, end):
        #     if start > end:
        #         return 0

        #     mid = (end + start) //2

        #     if (mid+1)*(mid+1) > x and (mid)*(mid) <= x:
        #         return mid
            
        #     if (mid-1)*(mid-1) > x:
        #         ## search left
        #         return helper(start, mid-1)
        #     else:
        #         ## search right
        #         return helper(mid+1, end)

        # return helper(0, x)

        l, r = 0, x
        res = 0

        while l <= r:
            mid = (l + r) //2

            if mid**2 == x:
                return mid
            
            if mid**2 > x:
                ## Go left 
                r = mid - 1
            else:
                ## go right
                res = mid
                l = mid + 1

        return res  
        










        