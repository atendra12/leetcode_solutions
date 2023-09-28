class Solution:
    def arrangeCoins(self, n: int) -> int:
        # i = 1
        # while n >= i:
        #     n = n - i
        #     i += 1
            
        # return i-1

        l, r = 1, n
        res = 1

        while l < r:
            mid = (l + r) // 2

            if mid*(mid+1)//2 == n:
                return mid

            if mid*(mid+1)//2 > n:
                ## left
                r = mid
            elif mid*(mid+1)//2 < n:
                # right 
                res = mid
                l  = mid + 1

        return res    





        